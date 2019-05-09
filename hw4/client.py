import requests
import hashlib
import sys
import threading
import string
import queue
import os
import time
import pprint

password = sys.argv[1]                                                          # this is the password to crack
length = len(password)                                                          # this is the length of the password
threads = int(sys.argv[2])                                                      # number of threads to utilize, (1 - 10)
hashed_password = hashlib.md5(password.encode()).hexdigest()                    # this is the hashed password
start = time.time()                                                             # start time
ports = ['500{}'.format(i) for i in range(threads)]                             # list of ports available

def request(hashed_password, prefix, length, worker, port):
    '''
    :param hashed_password: This is the hashed password we are trying break
    :param prefix: letter to start searching
    :param length: maximum length of the real password
    :return:
    '''
    try:

        r = requests.get(url="http://127.0.0.1:{}/passwordcracker".format(port), json={"password": hashed_password,
                                                                                        "prefix": prefix,
                                                                                        'length': length})
    # thread was terminated
    except requests.exceptions.ConnectionError:
        del jobs[worker]
        del ports[worker]
        return

    data = r.text
    status = r.status_code

    if data != 'No answer':
        end = round(time.time()-start,4)
        print(data)
        answer = {"time": '{} secs'.format(end), 'status': status}
        pprint.pprint(answer)
        os._exit(1)

# put all letters in a queue to split work.
letters = queue.Queue()
for i in string.printable:
    letters.put(i)

# Put threads in the list
jobs = []
for i in range(threads):

    # get a letter from the queue
    prefix = letters.get()
    t = threading.Thread(target=request, args=(hashed_password, prefix, length, i, ports[i]))
    t.daemon = True
    jobs.append(t)

# Start all of the threads
for i in jobs:
    i.start()

# look out for the password crack while restarting threads
while True:

    # if exhaust all characters, then quit
    if not letters:
        os._exit(1)

    # scan the jobs list for any complete jobs, if complete, restart thread with next prefix
    for i,j in enumerate(jobs):
        if j.is_alive():
            continue
        else:
            # get the next prefix
            prefix = letters.get()
            worker = i
            port = ports[i]
            t = threading.Thread(target=request, args=(hashed_password, prefix, length, worker, port))
            t.daemon = True
            jobs[i] = t
            t.start()


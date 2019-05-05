import requests
import hashlib
import sys
import threading


password = '&bc'         # this is the password to crack
length = len(password)   # this is the length of the password
threads = 2             # number of threads to run
hashed_password = hashlib.md5(password.encode()).hexdigest() # this is the hashed password

def request(hashed_password, length, threads, worker):

    '''
    :param hashed_password: This is the hashed password we are trying break
    :param length: maximum length of the real password
    :param threads: total number or threads to run concurrently
    :param worker: worker number
    :return:
    '''

    r = requests.get(url="http://127.0.0.1:5001/passwordcracker", json={"password": hashed_password,
                                                                    'length': length,
                                                                    'threads': threads,
                                                                    'worker': worker})

    data = r.text
    status = r.status_code

    print(data,status)

jobs = []


for i in range(threads):
    t = threading.Thread(target=request, args=(hashed_password, length, threads, i,))
    jobs.append(t)
    t.start()
    t.join()


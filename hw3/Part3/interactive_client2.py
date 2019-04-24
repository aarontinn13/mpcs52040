import sys
import pickle
import datetime
import zmq
import time
import threading

HOST=sys.argv[1]
PORT=int(sys.argv[2])
PUB_PORT=int(sys.argv[3])
USERNAME=sys.argv[4]

# print the history
lists = []
infile = open('messages.pickle', 'rb')
while True:
    try:
        lists.append(pickle.load(infile))
    except EOFError:
        break
infile.close()
for i in lists:
    print(i)

def listen():
    '''will listen on a different thread'''
    while True:
    #recieve the subscribed message
        message = subscribe.recv().decode()
        print(message)
        time.sleep(1)


#set up the context
context = zmq.Context()

# set up the post socket
post = context.socket(zmq.REQ)
post.connect("tcp://{}:{}".format(HOST, PORT))

# set up the subscribe socket
subscribe = context.socket(zmq.SUB)
subscribe.connect("tcp://{}:{}".format(HOST, PUB_PORT))

# set up the subscribe keyword
subscribe.setsockopt_string(zmq.SUBSCRIBE, '')

# start listening
t = threading.Thread(target=listen)
t.start()

# loop to continuously enter input
while True:
    # get the input from terminal
    input_message = sys.stdin.readline().strip('\n')
    FULL_MESSAGE = '{}: {} ({})'.format(USERNAME, input_message, datetime.datetime.now())

    # send the message to the server
    post.send_string(FULL_MESSAGE)

    #unclog the reply
    post.recv()




import socket
import sys
import pickle
import datetime
import zmq

HOST=sys.argv[1]
PORT=int(sys.argv[2])
PUB_PORT=int(sys.argv[3])
USERNAME=sys.argv[4]

# print the history
lists = []
infile = open('messages.pickle', 'rb')
while 1:
    try:
        lists.append(pickle.load(infile))
    except EOFError:
        break
infile.close()
for i in lists:
    print(i)

# open connection to the server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as post:

    # connect to server/PORT
    post.connect((HOST, PORT))

    # connect to server/PUB_PORT
    context = zmq.Context()
    pub = context.socket(zmq.SUB)
    pub.connect('tcp://{}:{}'.format(HOST, PUB_PORT))
    pub.setsockopt_string(zmq.SUBSCRIBE, '')

    while True:

        print('yes???')

        # get the message, prepare it, and submit to server
        message = sys.stdin.readline().rstrip('\n')
        print('yes2???')
        message = '{}: {} ({})'.format(USERNAME, message, datetime.datetime.now())
        print('yes3???')

        post.sendall(pickle.dumps(message))

        print('yes4???')
        # receive the updated messages
        lists = pub.recv()

        # print the updated ledger of messages
        for i in pickle.loads(lists):
            print(i)

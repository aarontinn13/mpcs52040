import zmq
import sys
import pickle
import time

HOST=sys.argv[1]
PORT=int(sys.argv[2])
PUB_PORT=int(sys.argv[3])

# load history
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


# set up the context
context = zmq.Context()

# set up recieve socket
recieve = context.socket(zmq.REP)
recieve.bind("tcp://{}:{}".format(HOST, PORT))

# set up publish socket
publish = context.socket(zmq.PUB)
publish.bind("tcp://{}:{}".format(HOST, PUB_PORT))

while True:
    # Wait for next request from client
    message = recieve.recv()
    recieve.send_string('')
    message = message.decode()
    print(message)

    # store data in pickle file
    with open(r"messages.pickle", 'ab') as file:
        pickle.dump(message, file)

    publish.send_string(message)
    time.sleep(1)
import zmq
import sys
import pickle
import socket

HOST=sys.argv[1]
PORT=int(sys.argv[2])
PUB_PORT=int(sys.argv[3])

print('Loading History...\n')
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
print('\n...History Loaded')

# open connection to writer
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as post:

    # set up pub sockets
    context = zmq.Context()
    pub = context.socket(zmq.PUB)
    pub.bind('tcp://{}:{}'.format(HOST, PUB_PORT))

    # bind post socket
    post.bind((HOST, PORT))

    # listen to poster
    post.listen()

    while True:

        print('yes???')

        # retrieve information from client
        conn, addr = post.accept()

        # load the data and print it
        data = pickle.loads(conn.recv(1024))
        print('{}'.format(data))

        # store data in pickle file
        with open(r"messages.pickle", 'ab') as file:
            pickle.dump(data, file)

        # store the data in the list
        lists.append(data)

        # send the updated list to the Publish Port
        pub.send(pickle.dumps(lists))

        print('pass')
import socket
import sys
import pickle

HOST=sys.argv[-2]
PORT=int(sys.argv[-1])

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

# open connection
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

    # bind socket
    s.bind((HOST, PORT))

    # listen
    s.listen()

    while True:

        # retrieve information from client
        conn, addr = s.accept()

        # load message
        data = pickle.loads(conn.recv(1024))
        print('{}'.format(data))

        # store data in pickle file
        with open(r"messages.pickle", 'ab') as file:
            pickle.dump(data, file)


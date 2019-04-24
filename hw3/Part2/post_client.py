import socket
import sys
import pickle
import datetime

HOST=sys.argv[1]
PORT=int(sys.argv[2])
USERNAME=sys.argv[3]
MESSAGE=' '.join(sys.argv[4:])
FULL_MESSAGE='{}: {} ({})'.format(USERNAME, MESSAGE, datetime.datetime.now())


# open connection
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

    # connect to server
    s.connect((HOST, PORT))

    # send message to server
    print(FULL_MESSAGE)
    s.sendall(pickle.dumps(FULL_MESSAGE))

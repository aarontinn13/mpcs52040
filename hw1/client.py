import socket
import sys
import pickle

HOST = '127.0.0.1'
PORT = int(sys.argv[-2])
try:
    MESSAGE = eval(sys.argv[-1])
except NameError:
    MESSAGE = str((sys.argv[-1]))

# open connection
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

    # connect to server
    s.connect((HOST, PORT))

    # send message to server
    print('Message to Server: {}\n'.format(MESSAGE))
    s.sendall(pickle.dumps(MESSAGE))

    # retrieve response from server, decode and print
    data = pickle.loads(s.recv(1024))
    print('Response from Server: ', data)



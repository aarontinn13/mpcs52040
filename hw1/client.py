import socket
import sys
import pickle

HOST = '127.0.0.1'
# PORT only, Hardcoded Object
if len(sys.argv) == 2:
    PORT = int(sys.argv[-1])
    MESSAGE = ["This", 'is', 'a', 'Message'] # Hardcoded List obj

# PORT and String given
elif len(sys.argv) == 3:
    PORT = int(sys.argv[-2])
    MESSAGE = str(sys.argv[-1])

else:
    exit("Too many or not enough arguments given")

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



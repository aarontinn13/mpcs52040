import socket
import pickle
import time

HOST='172.17.0.1'
PORT=1234
n=5

# open connection
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

    # connect to server
    s.connect((HOST, PORT))

    # send message to server
    print('n: {}\n'.format(n))
    s.sendall(pickle.dumps(n))

    print('{} seconds remain'.format(n))
    for i in range(n-1, 0, -1):
        time.sleep(1)
        print('{} seconds remain'.format(i))

    # retrieve response from server, decode and print
    data = pickle.loads(s.recv(1024))
    print('\nResponse from Server: ', data)

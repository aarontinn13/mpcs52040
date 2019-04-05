import socket
import sys
import pickle

HOST = '127.0.0.1'
PORT = int(sys.argv[-2])
try:
    RESPONSE = eval(sys.argv[-1])
except NameError:
    RESPONSE = str((sys.argv[-1]))

# open connection
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

    # bind socket
    s.bind((HOST, PORT))

    # listen
    print('Listening...\n')
    s.listen()

    # retrieve information from client
    conn, addr = s.accept()

    with conn:

        # receive message, decode and print
        data = pickle.loads(conn.recv(1024))
        print('Message from Client: {}\n'.format(data))

        # send response to client
        print('Response to Client: {}'.format(RESPONSE))
        conn.sendall(pickle.dumps(RESPONSE))



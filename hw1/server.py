import socket
import sys
import pickle

HOST = '127.0.0.1'

# PORT only, Hardcoded Object
if len(sys.argv) == 2:
    PORT = int(sys.argv[-1])
    RESPONSE = ["This", 'is', 'a', 'Response'] # Hardcoded List obj

# PORT and String given
elif len(sys.argv) == 3:
    PORT = int(sys.argv[-2])
    RESPONSE = str(sys.argv[-1])
else:
    exit("Too many arguments given")

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



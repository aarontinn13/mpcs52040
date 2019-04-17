import socket
import pickle
import threading
import time

HOST='0.0.0.0'
PORT=1234

def response(conn, n,count):
    print("sleeping for {} sec for client {}".format(n,count))
    for i in range(n - 1, 0, -1):
        time.sleep(1)
        print('{} seconds remain for client {}'.format(i, count))
    print("finished sleeping for client {}".format(n,count))
    print('Response to client {}: \"Received\"'.format(count))
    conn.sendall(pickle.dumps('Received'))


# open connection
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

    #number of clients
    count = 0

    # bind socket
    s.bind((HOST, PORT))

    # listen
    s.listen()
    print('Listening...\n')

    while True:

        # retrieve information from client
        conn, addr = s.accept()

        # receive message, decode and print
        n = pickle.loads(conn.recv(1024))
        print('Message from Client {}: {}'.format(count, n))

        t = threading.Thread(target=response, args=(conn, n,count,))
        t.start()

        count += 1


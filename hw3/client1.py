import zmq
import sys

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect ("tcp://127.0.0.1:7777") #post socket

while True:
    message = sys.stdin.readline()
    socket.send_string(message)
    #  Get the reply.
    message = socket.recv()
    print("Received reply {}".format(message))
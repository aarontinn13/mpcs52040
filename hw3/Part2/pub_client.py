import sys
import zmq
import pickle

HOST=sys.argv[1]
PUB_PORT=int(sys.argv[2])

print('Loading History...\n')
# load history
lists = []
infile = open('messages.pickle', 'rb')
while 1:
    try:
        lists.append(pickle.load(infile))
    except EOFError:
        break
infile.close()
for i in lists:
    print(i)
print('\n...History Loaded')

context = zmq.Context()
s = context.socket(zmq.SUB)
s.connect('tcp://{}:{}'.format(HOST,PUB_PORT))
s.setsockopt_string(zmq.SUBSCRIBE, '')

while True:

    print(s.recv_string())
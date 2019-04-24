Specs:

    Python 3.7
    Ubuntu 18.04

How to Run:

    # run the server
    python post_server.py <IP> <PORT>

    # run the client
    python post_client.py <IP> <PORT> <NAME> <MESSAGE>

Example:

    python post_server.py 127.0.0.1 7777
    python post_client.py 127.0.0.1 7777 Kyle "Hello"
    python post_client.py 127.0.0.1 7777 Tyler "Hey"
    python post_client.py 127.0.0.1 7777 Kyle "What's up?"
    python post_client.py 127.0.0.1 7777 Tyler "Not much"
    python post_client.py 127.0.0.1 7777 Kyle "Okay"
    python post_client.py 127.0.0.1 7777 Tyler "Nice"

Description:

    messages.pickle - stores the history of all the incoming messages for various server sessions
    post_server.py  - server that receives all incoming messages from post_client.py and prints them and stores them into messages.pickle
    post_client.py  - client that will send messages to the server and prints them


Comments:

    Everything works fine.
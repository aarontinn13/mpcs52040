Specs:

    Python 3.7
    Ubuntu 18.04

How to Run:

    # run the server
    python interactive_server.py <IP> <POST_PORT> <PUB_PORT>

    # run client 1
    python interactive_client.py <IP> <POST_PORT> <PUB_PORT> <NAME>

    # run client 2
    python interactive_client2.py <IP> <POST_PORT> <PUB_PORT> <NAME>

Example:

    python interactive_server.py 127.0.0.1 7777 7778
    python interactive_client.py 127.0.0.1 7777 7778 Tyler
    python interactive_client2.py 127.0.0.1 7777 7778 Kyle

    ...start typing on both client terminals

Description:

    messages.pickle         - stores the history of all the incoming messages for various server sessions
    interactive_server.py   - server that receives all incoming messages from clients and prints them and stores them into messages.pickle
    interactive_client.py   - client that will also send and receive messages
    interactive_client2.py  - client that will also send and receive messages

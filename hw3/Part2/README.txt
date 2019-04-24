Specs:

    Python 3.7
    Ubuntu 18.04

How to Run:

    # run the server
    python pub_server.py <IP> <POST_PORT> <PUB_PORT>

    # run the listener client
    python pub_client.py <IP> <PUB_PORT>

    # run the poster client
    python post_client.py <IP> <PUB_PORT> <NAME> <MESSAGE>

Example:
    
    python pub_server.py 127.0.0.1 7777 7778
    python pub_client.py 127.0.0.1 7778
    python post_client.py 127.0.0.1 7777 Kyle "Hello"
    python post_client.py 127.0.0.1 7777 Tyler "Hey"
    python post_client.py 127.0.0.1 7777 Kyle "What's up?"
    python post_client.py 127.0.0.1 7777 Tyler "Not much"
    python post_client.py 127.0.0.1 7777 Kyle "Okay"
    python post_client.py 127.0.0.1 7777 Tyler "Nice"
    
Description:

    messages.pickle - stores the history of all the incoming messages for various server sessions
    pub_server.py   - server that receives all incoming messages from post_client.py and prints them and stores them into messages.pickle
    post_client.py  - client that will send messages to the server and print at the same time
    pub_client.py   - client that will listen and print stuff from the server

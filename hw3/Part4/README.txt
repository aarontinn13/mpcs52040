Specs:

    Python 3.7
    Ubuntu 18.04

How to Run:

    # run the server
    python mc_server.py <IP> <POST_PORT> <PUB_PORT>

    # run client 1
    python mc_client.py <IP> <POST_PORT> <PUB_PORT> <CHANNEL> <NAME>

    # run client 2
    python mc_client2.py <IP> <POST_PORT> <PUB_PORT> <CHANNEL> <NAME>

    # run client 3
    python mc_client3.py <IP> <POST_PORT> <PUB_PORT> <CHANNEL> <NAME>


Example:

    python interactive_server.py 127.0.0.1 7777 7778
    python interactive_client.py 127.0.0.1 7777 7778 ALL Tyler
    python interactive_client2.py 127.0.0.1 7777 7778 MPCS Kyle
    python interactive_client3.py 127.0.0.1 7777 7778 RANDOM Aaron

    ...start typing on all client terminals

Description:

    ALL_messages.pickle    - stores the history of all the incoming messages for various server sessions
    MPCS_messages.pickle   - stores the history of incoming messages in MPCS channel for various server sessions
    RANDOM_messages.pickle - stores the history of incoming messages in RANDOM channel for various server sessions
    mc_server.py           - server that receives all incoming messages from clients and prints them and stores them into their respective channel file
    mc_client.py           - client that will also send and receive messages in current channel (if ALL, then will receive from all channels)
    mc_client2.py          - client that will also send and receive messages in current channel (if ALL, then will receive from all channels)
    mc_client3.py          - client that will also send and receive messages in current channel (if ALL, then will receive from all channels)


Comments:

    Everything works fine.
    Currently have 3 channel pickle files, you can add more channels however history will not be saved.

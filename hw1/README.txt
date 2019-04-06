-- Specs:

    Ubuntu 18.04
    Python 3.6



-- How to Use:

    1.) Start the Server to Listen for connection

        python server.py <PORT> <MESSAGE | NONE>

    2.) Start the Client to Connect

        python client.py <PORT> <MESSAGE | NONE>




-- Example passing a string:

    python server.py 1234 'pong'

        Listening...

        Message from Client: ping

        Response to Client: pong

    python client.py 1234 "ping"

        Message to Server: ping

        Response from Server:  pong


-- Example passing a list object:

    python server.py 1234

        Listening...

        Message from Client: ["This", 'is', 'a', 'Message']

        Response to Client: ["This", 'is', 'a', 'Response']


    python client.py 1234

        Message to Server: ["This", 'is', 'a', 'Message']

        Response from Server:  ["This", 'is', 'a', 'Response']

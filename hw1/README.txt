-- Specs:

    Ubuntu 18.04
    Python 3.6



-- How to Use:

    1.) Start the Server to Listen for connection

        python server.py <PORT> <MESSAGE or OBJECT>

    2.) Start the Client to Connect

        python client.py <PORT> <MESSAGE or OBJECT>




-- Example passing a string:

    python server.py 1234 'pong'

        Listening...

        Message from client: ping

        Response to Server: pong

    python client.py 1234 "ping"

        Message to Server: ping

        Response from Server:  pong


-- Example passing a list object:

    python server.py 1234 [1,2,3]

        Listening...

        Message from client: [1, 2, 3]

        Response to Server: [1, 2, 3]


    python client.py 1234 [1,2,3]

        Message to Server: [1, 2, 3]

        Response from Server:  [1, 2, 3]

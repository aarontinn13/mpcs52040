#!/bin/bash

#create an image named server in the current directory
sudo docker run -p 1234:1234 -it server python server.py

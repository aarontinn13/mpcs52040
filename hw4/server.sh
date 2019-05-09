#!/bin/bash

#create 10 servers
for i in {0..9}
do
   gnome-terminal -x bash -c "python cracker_service.py 500$i; exec bash"
done


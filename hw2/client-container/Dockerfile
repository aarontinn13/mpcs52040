# get the latest ubuntu base image
FROM ubuntu:latest

# Copy the current directory file 'post_server.py' into the container at /.
COPY client.py /.

# get python3
RUN apt-get update \
  && apt-get install -y python3-pip python3-dev \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install --upgrade pip

# expose port
EXPOSE 1234

FROM ubuntu:18.04
RUN apt-get update && \
    apt-get install python3-pip python3-dev -y && \
    ln -s /usr/bin/python3 /usr/local/bin/python && \
    pip3 install --upgrade pip && \
    rm /var/lib/apt/lists/* -vrf
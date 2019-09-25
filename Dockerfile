FROM i386/ubuntu:16.04

RUN apt-get  update 
RUN apt-get -y install python wget git libpoe-component-pcap-perl
ADD ./setup.sh /tmp/setup.sh
ADD ./keygen.py /root/keygen.py
ADD ./link.py /root/link.py
RUN /bin/sh /tmp/setup.sh

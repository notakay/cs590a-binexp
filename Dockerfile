# sudo docker build -t test:0.1 .
# sudo docker run --rm --name test0.1 -it test:0.1
# sudo docker exec -it test0.1 /bin/bash

FROM ubuntu:xenial

RUN apt update
RUN apt install -y sudo build-essential gcc-multilib coreutils python3 gdb vim nano socat

RUN useradd -d /home/ctf/ -m -p ctf -s /bin/bash ctf
RUN echo "ctf:ctf" | chpasswd

WORKDIR /opt

ADD zero /opt/zero
WORKDIR /opt/zero
RUN make zero

ADD one /opt/one
WORKDIR /opt/one
RUN make one

ADD two /opt/two
WORKDIR /opt/two
RUN make two

ADD three /opt/three
WORKDIR /opt/three
RUN make three

EXPOSE 10000
EXPOSE 10001
EXPOSE 10002
EXPOSE 10003

WORKDIR /opt
COPY socat.sh /opt
RUN chmod +x /opt/socat.sh

# Still buggy, running in detached mode, or simply executing
# another shell will drop user in root
# script force switches to user ctf
ENTRYPOINT sh /opt/socat.sh

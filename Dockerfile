# sudo docker build -t test:0.1 .
# sudo docker run --rm --name test0.1 -it test:0.1
# sudo docker exec -it test0.1 /bin/bash

FROM ubuntu:xenial

RUN apt update
RUN apt install -y sudo build-essential gcc-multilib coreutils python3 gdb vim nano socat git

RUN useradd -d /home/ctf/ -m -p ctf -s /bin/bash ctf
RUN echo "ctf:ctf" | chpasswd

WORKDIR /opt

RUN git clone https://github.com/notakay/cs590a-binexp
RUN mv cs590a-binexp chal

WORKDIR /opt/chal/zero
RUN make zero

WORKDIR /opt/chal/one
RUN make one

WORKDIR /opt/chal/two
RUN make two

WORKDIR /opt/chal/three
RUN make three

EXPOSE 10000
EXPOSE 10001
EXPOSE 10002
EXPOSE 10003

WORKDIR /opt/chal
RUN chmod +x /opt/chal/socat.sh

# Still buggy, running in detached mode, or simply executing
# another shell will drop user in root
# script force switches to user ctf
ENTRYPOINT sh /opt/chal/socat.sh

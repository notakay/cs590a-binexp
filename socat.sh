#!/bin/sh

socat TCP-LISTEN:10000,reuseaddr,fork EXEC:"./zero/zero.o" &
socat TCP-LISTEN:10001,reuseaddr,fork EXEC:"./one/one.o" &
socat TCP-LISTEN:10002,reuseaddr,fork EXEC:"./two/two.o" &
socat TCP-LISTEN:10003,reuseaddr,fork EXEC:"./three/three.o" &

su - ctf

$@

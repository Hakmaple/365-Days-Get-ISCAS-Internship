from pwn import *
elf = ELF('./ret2libc')
rop = ROP(elf)
print(rop.ret)  
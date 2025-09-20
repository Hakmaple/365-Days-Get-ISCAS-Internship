from pwn import *

# 生成测试 payload
payload = cyclic(100)
p = process('./vuln')
p.sendline(payload)
p.wait()  # 让程序崩溃
core = p.corefile  # 获取崩溃信息
eip = core.eip
offset = cyclic_find(eip)  # 计算实际偏移量
print(f"Actual offset: {offset}")
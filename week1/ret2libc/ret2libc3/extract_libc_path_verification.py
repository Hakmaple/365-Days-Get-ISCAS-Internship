from pwn import *

# 加载目标二进制
elf = ELF('./ret2libc3')

print("二进制文件:", elf.path)
print("依赖的libc路径:", elf.libc.path)  # 自动获取的libc路径
print("libc基址(未设置):", hex(elf.libc.address))

# 手动验证
print("\n手动验证:")
print("ELF对象的libc属性类型:", type(elf.libc))
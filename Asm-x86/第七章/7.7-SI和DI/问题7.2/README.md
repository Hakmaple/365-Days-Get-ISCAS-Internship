# 问题 7.2
用`si`和`di`实现将字符串`welcome to masm!`复制到它后面的数据区中。
```ASM
assume cs:codesg,ds:datasg
datasg segment
    db 'welcome to masm!'
    db '----------------'
datasg ends
```

# 分析
`welcome to masm!`长度为16byte，所以其后面的数据区偏移地址为16，因此可以通过`ds:si`指向要复制的原始字符串，用`ds:di`来指向复制的目的空间，然后一个循环逐字节地写入。

实现代码如下：
```ASM
codesg segment
start: 
    mov ax,datasg
    mov ds,ax
    mov si,0
    mov di,16

    mov cx,8
s:
    mov ax,[si]
    mov [di],ax
    add si,2
    add di,2
    loop s

    mov ax,4c00H
    int 21H
codesg ends
end start
```
*Tip: 由于`ax`是十六位寄存器能够一次存储数据高位和低位字，也就是一次复制两个字节，因此只需循环 $16/2=8$ 次*

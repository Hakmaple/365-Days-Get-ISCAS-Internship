# 问题 7.3
用更少地代码，实现[问题7.2](../问题7.2/README.md)的程序

# 分析
我们可以利用`[bx+idata]的方式` (在前面的章节中，我们使用此方法写一个循环代替两个循环)

代码如下：
```ASM
codesg segment
start:
    mov ax,datasg
    miv ds,ax
    mov si,0
    mov bx,8
s:
    mov ax,0[si]
    mov 16[si],ax
    add si,2
    loop s

    mov ax,4c00h
    int 21h
codesg ends
end start
```
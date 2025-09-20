# 7.6-用[bx+idata]的方式进行数组的处理-实现方式对比

## 问题：
在`codesg`中填写代码，将`codesg`中定义的第一个字符串转化为大写，第二个字符串转化为小写。

```ASM
assume cs:codesg, ds:datasg
datasg segment
    db 'BaSiC'
    db 'MinIX'
datasg ends

codesg segment
    start:
codesg ends

end start
```

## 新旧方式实现对比
#### 用[bx]的方式定位字符串中的字符
old_method.asm
```ASM
assume cs:codesg, ds:datasg

datasg segment
    db 'BaSiC'
    db 'MinIX'
datasg ends

codesg segment
start:
    mov ax, datasg
    mov ds, ax
    mov bx, 0

    mov cx, 5
s1:
    mov al, [bx]
    and al, 11011111b  ; 转换为大写
    mov [bx], al
    inc bx
    loop s1

    mov bx, 5
    mov cx, 5
s2:
    mov al, [bx]
    or al, 00100000b   ; 转换为小写
    mov [bx], al
    inc bx
    loop s2

    mov ax, 4c00h      ; 程序退出（DOS功能调用）
    int 21h
codesg ends

end start
```

#### 用[bx+idata]的方式定位字符串中的字符
原理：观察`codesg`中的两个字符串，虽然它们的起始地址不同，但是都可以通过`[偏移量+bx]`方式在同一个循环中定位这两个字符串中的字符，虽然上述两字符串在内存中的起始地址不一样，但是其中的每一个字符从起始地址开始的“相对地址”的变化是相同的。

new_method.asm
```ASM
assume cs:codesg, ds:datasg
datasg segment
    db 'BaSiC'
    db 'MinIX'
datasg ends

codesg segment
    start:
        mov bx, 0
        mov cx, 5
    s:
        ; 处理 'BaSiC'（转大写）
        mov al, [bx]
        and al, 11011111b
        mov [bx], al

        ; 处理 'MinIX'（转小写）
        mov al, [5 + bx]
        or al, 00100000b
        mov [5 + bx], al

        inc bx
        loop s
codesg ends

end start
```

#### 用C语言进行描述上面的程序
```C
#include <stdio.h>

int main() {
    char str1[5] = {'B', 'a', 'S', 'i', 'C'};  
    char str2[5] = {'M', 'i', 'n', 'I', 'X'};  
    int i;

    for (i = 0; i < 5; i++) str1[i] &= ~0x20;  // 等价于 AND AL, 11011111b
    for (i = 0; i < 5; i++)  str2[i] |= 0x20;   // 等价于 OR AL, 00100000b

    printf("Result: ");
    for (i = 0; i < 5; i++) printf("%c", str1[i]);  
    for (i = 0; i < 5; i++) printf("%c", str2[i]);  
    printf("\n"); // 将两个字符串连起来
    return 0;
}
```


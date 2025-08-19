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
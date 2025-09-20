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
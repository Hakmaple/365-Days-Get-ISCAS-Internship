assume cs:codesg,ds:datasg
datasg segment
    db 'welcome to masm!'
    db '----------------'
datasg ends

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
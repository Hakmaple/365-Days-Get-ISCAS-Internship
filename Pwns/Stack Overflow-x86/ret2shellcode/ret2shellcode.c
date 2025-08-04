#include <stdio.h>
#include <stdlib.h>

int main() {
    mmap(0x804d000, 0x1000, 7, 0x21, -1, 0);

    char *p = (char *)0x804d000;
    char str[0x20];

    read(0, p, 0x1000);

    read(0, str, 0x50);

    return 0;
}

// gcc ret2shellcode.c -no-pie -fno-stack-protector -g
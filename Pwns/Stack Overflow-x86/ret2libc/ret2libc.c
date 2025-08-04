#include <stdio.h>

int main() {
    char str[0x20];
    puts("There is something amazing here, do you know anything?\n");
    read(0, str, 0x100);
    return 0;
}

// gcc ret2libc.c -no-pie -fno-stack-protector -g
// 施工ing

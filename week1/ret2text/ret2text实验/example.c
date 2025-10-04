#include <stdio.h>
#include <string.h>

void secure() {
    system("/bin/sh");
}

void vulnerable() {
    char buf[16];
    gets(buf);
    printf("Input: %s\n", buf);
}

int main() {
    vulnerable();
    return 0;
}

// gcc -m32 -fno-stack-protector -z execstack -no-pie -o example example.c
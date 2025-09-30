#include <stdio.h>
#include <string.h>

void pwn() {
    printf("Pwn!");
    system("/bin/sh");
}

void vuln() {
    char buffer[64];
    printf("There is something amazing here, do you know anything?\n");
    gets(buffer);
    printf("Maybe I will tell you next time !");
}

int main() {
    vuln();
    return 0;
}

// gcc -m32 -fno-stack-protector -z execstack -no-pie vuln.c -o vuln
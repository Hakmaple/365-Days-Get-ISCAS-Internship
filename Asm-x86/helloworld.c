#include <stdio.h>

int main(){
    printf("hello world!");
    return 0;
}

// gcc -S helloworld.c -o helloworld.s -masm=intel
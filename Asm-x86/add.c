#include<stdio.h>

int add(int a, int b){
    return a + b;
} 

int main(){
    printf("%d", add(2, 3));
    return 0;
}

// gcc -S add.c -o add.s -masm=intel
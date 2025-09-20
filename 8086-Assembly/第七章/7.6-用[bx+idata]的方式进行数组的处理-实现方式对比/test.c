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
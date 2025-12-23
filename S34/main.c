#include<stdio.h>

void main()
{
    char str[100] = "12345678912345678901234578901234567890";
    char* pch;

    for(int i=0; str[i]; i++)
        pch[i] = str[i];

    for(int i=0; pch[i]; i++)
        printf("%c\n", pch[i]);
    
}
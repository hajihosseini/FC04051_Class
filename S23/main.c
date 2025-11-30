#include<stdio.h>

unsigned int power2(int n)
{
    // ...
    //while
}

void print_binary_proper(unsigned int n)
{
    int bits = sizeof(n) * 4;
    unsigned int lastbitOn = power2(bits);
    int b = n & lastbitOn;
    if (b > 0)
        printf("1");
    else
        printf("0");
    n = n * 2;
}

void print_binary(int n)
{
    int i = 0;
    while(i < (sizeof(n) * 8))
    {
        int b = n % 2;
        printf("%d ", b);
        n = n / 2;
        i = i + 1;
    }
}


int main(int argc, char** argv)
{
    int n;
    while (1)
    {
        scanf("%d", &n);
        print_binary(n);
    }
    return 0;
}
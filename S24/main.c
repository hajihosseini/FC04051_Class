#include<stdio.h>


unsigned int get_bit(unsigned int n, int i)
{
    return (n >> i) % 2;
}

unsigned int set_bit(unsigned int n, int i)
{
    return n | (1<<i);   
}

unsigned int set_bit1(unsigned int n, int i)
{
    int x = get_bit(n, i);
    if (x == 0)
        n = n + (1<<i);
    return n;  
}

unsigned int clear_bit1(unsigned int n, int i)
{
    int j = 0;
    unsigned int result = 0;
    while (j < (sizeof(n) * 8))
    {
        if (j == i)
            continue;

        int x = get_bit(n, j);
        result = result + x * (1<<j);
    }
    return n;  
}

unsigned int clear_bit2(unsigned int n, int i)
{
    int x = get_bit(n, i);
    if (x == 1)
        n = n - 1<<i;
    return n;
}

unsigned int clear_bit3(unsigned int n, int i)
{
    unsigned int allone_but_i = 0xffffffff - (1<<i);
    return allone_but_i & n;
}

unsigned int clear_bit(unsigned int n, int i)
{
    return ~(1<<i) & n;
}

unsigned int reverse_bits(unsigned int n)
{
    unsigned int result = 0;
    int i = 0;
    int bits = sizeof(n) * 8;
    while (i < bits)
    {
        result = result + get_bit(n, i) * (1<<(bits-i-1));
    }
}

unsigned int reverse_bits_proper(unsigned int n)
{

}

unsigned int reverse_bits_prime_positions(unsigned int n)
{

}

int get_numsquare(int n)
{
    return n*n;
}



void main()
{
    int w = 0b101;
    //        100
    // & | ^ ~
}




void main2()
{
    int x = 0b1101;
    int i = (sizeof(x) * 8)-1;
    while (i >= 0 )
    {
        printf("%d ", get_bit(x, i));
        i--;
    }
}



    // int x = 13;
    // printf("%d\n", x); 
    // x = 0xd;
    // printf("%d\n", x); 

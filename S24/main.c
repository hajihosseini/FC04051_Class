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

int get_highest_bit_pos(unsigned int n)
{
    int pos=0;
    while(n>0)
    {
        n = n >> 1;
        pos++;
    }
    return pos;
}

unsigned int reverse_bits(unsigned int n)
{
    unsigned int result = 0;
    int i = 0;
    int bits = sizeof(n) * 8;
    while (i < bits)
    {
        result = result + get_bit(n, i) * (1<<(bits-i-1));
        i++;
    }
    return result;
}

unsigned int reverse_bits_proper(unsigned int n)
{
    unsigned int result = 0;
    int i = 0;
    int bits = get_highest_bit_pos(n);
    while (i < bits)
    {
        result = result + get_bit(n, i) * (1<<(bits-i-1));
        i++;
    }
    return result;
}

unsigned int reverse_bits_prime_positions(unsigned int n)
{
    unsigned int new_n;
}

unsigned int swap_bits(unsigned int n, int i, int j)
{
    if (get_bit(n, i))
        set_bit(n, j);
    if (get_bit(n, j))
        set_bit(n, i);
}


unsigned int flip_bit(unsigned int n, int i )
{
    if (get_bit(n, i))
        return clear_bit(n, i);
    else
        return set_bit(n, i);
}

unsigned int flip_bit(unsigned int n, int i )
{
    return n ^ (1<<i);
}



unsigned int reverse_bits_prime_positions_simple(unsigned int n)
{
    int len = sizeof(int) * 8;
    int i = 0;
    int p1 = 0, p2 = len-1;
    while(p1<p2)
    {
        int p1 = get_prime_from_start(0, len-1, i);
        int p2 = get_prime_from_end(0, len-1, i);
        n = swap_bits(n, p1, p2);
    }
}

unsigned int reverse_bits_prime_positions_2(unsigned int n)
{
    int upper = 31;
    int lower = 0;
    while (lower < upper)
    {
        while (!is_prime(upper))
            upper--;
        while (!is_prime(lower))
            lower++;
        n = swap_bits(n, lower, upper);
        lower++;
        upper--;
    }
    return n;
}

unsigned int reverse_bits_prime_positions_233(unsigned int n)
{
    unsigned int new_n;
    int upper = 31;
    int lower = 0;
    while (lower < upper)
    {
        while (!is_prime(upper))
        {
            new_n += get_bit(n,upper) * ( 1<<(upper));
            upper--;
        }
        while (!is_prime(lower))
        {
            new_n += get_bit(n, lower) * (1>>(lower));
            lower++;
        }
        new_n += get_bit(n,lower) * ( 1<<(upper));
        new_n += get_bit(n,upper) * ( 1>>(lower));
        lower++;
        upper--;
    }
    return new_n;
}

int get_numsquare(int n)
{
    return n*n;
}



void main()
{
    int w = 0b101;
    printf("%d\n", reverse_bits_proper(w));
    w = 0b100101;
    printf("%d\n", reverse_bits_proper(w));
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

#include <stdio.h>

int is_prime(int a) 
{
    if ((a == 0) | (a == 1))
    {
        return 0;
    }
    int i = 2;
    while (i < a)
    {
        if (a % i == 0)
        {
            return 0; 
        }
        i += 1;
    }
        return 1;
}

int getbit(unsigned int x, unsigned int i)
{
    return (x >> i) % 2;
}

int findnthprimebit_l(unsigned int x, unsigned int n)
{
    int i = sizeof(x) * 8 - 1;
    int j = 0;
    while (i >= 0)
    {
        if (is_prime(i))
        {
            j += 1;
        }
        if (j == n)
        {
            return i;
        }
        i -= 1;
    }
}

unsigned int reverse_bits_prime(unsigned int x)
{
    int s = sizeof(x) * 8;
    long unsigned int result = 0;
    int i = 0;
    int j = 1;
    while (i < s)
    {
        if ((is_prime(i)) & (i < s/2))                                                                          
        {
            int p = findnthprimebit_l(x, j);
            result += getbit(x, i) * (1 << p) + getbit(x, p) * (1 << i);
            j += 1;
        }
        else
        {
            if (is_prime(i) == 0)
            {
                result += getbit(x, i) * (1 << i);
            }
        }
        i += 1;
    }
    return result;
}

int main()
{
    printf("%u", reverse_bits_prime(13));
    return 0;
}

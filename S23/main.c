#include<stdio.h>


unsigned int get_bit(unsigned int n, int i)
{
    return (n >> i) % 2;
}

unsigned int set_bit(unsigned int n, int i)
{
    
}

unsigned int clear_bit(unsigned int n, int i)
{

}

unsigned int reverse_bits(unsigned int n)
{

}

unsigned int power2(int n)
{
    int i = 0;
    unsigned int result = 1;
    while (i<n)
    {
        result = result * 2;
        i++;
    }
    return result;
}

int get_last_bit(unsigned int n)
{
    int bits = sizeof(n) * 8;    
    unsigned int lastbitOn = power2(bits-1); // 1 << bits-1;
    unsigned int b = n & lastbitOn;
    if (b != 0)
        return 1;
    else
        return 0;
}

void print_binary_proper(unsigned int n)
{
    int bits = sizeof(n) * 8;    
    int i = 0;
    while (i < bits)
    {
        printf("%d", get_last_bit(n));
        n = n * 2; // n << 1;
        i++;
    }
}

void print_binary(int n)
{
    int i = 0;
    while(i < (sizeof(n) * 8))
    {
        int b = n % 2;
        printf("%d ", b);
        n = n / 2;  // n >> 1
        i = i + 1;
    }
}


int main(int argc, char** argv)
{
    unsigned char n = 200;
    printf("%d\n", n);

    // int n;
    // // while (1)
    // {
    //     // scanf("%d\n", &n);
    //     print_binary_proper(43);
    // }
    return 0;
}
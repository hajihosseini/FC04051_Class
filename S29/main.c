#include<stdio.h>


void print_jagged_array2(char **buf, int len)
{
    for(int i=0; i<len; i++)
    {
        printf("%s\n", buf[i]);
    }
}

void print_jagged_array(char **ppbuf, int len)
{
    int i = 0;
    while (i < len)
    {
        printf("%s\n", *ppbuf);
        ppbuf++;
        i++;
    }
}

int sum(int** nums, int* num_count, int count)
{

}

int main(int argc, char** argv)
{
    int n1[3] = {1,2,3};
    int n2[5] = {-1, 2, 5, 4, 3};
    int n3[2] = {0, 1};
    int* nums[3] = {n1, n2, n3};
    int counts[3] = {3, 5, 2};
    int count = 3;
    int mysum = sum(nums, counts, count);
    // print_jagged_array(argv, argc);

    char buf[20] = "1234567890123456789";
    char* pbuf[20];
    for(int i=0; i<20; i++)
    {
        pbuf[i] = buf+i;
    }
    print_jagged_array(pbuf, 20);
}

void main567898765()
{
    // char buf[10]
    char buf1[10] = "ali1";
    char buf2[10] = "mari1";
    char buf3[10] = "sari1";

    char* pbuf[3] = {buf1, buf2, buf3};
    print_jagged_array(pbuf, 3);
}
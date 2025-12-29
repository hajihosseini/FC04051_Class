#include<stdio.h>
#include<stdlib.h>


int add(int a, int b)
{
    return a+b;
}

int mul(int a, int b)
{
    return a*b;
}

typedef int (*_int_2int)(int, int);

void apply(int* nums1, int* nums2, int size, _int_2int fn, int** result)
{
    *result = malloc(sizeof(int) * size);
    for(int i=0; i<size; i++)
    {
        (*result)[i] = fn(nums1[i], nums2[i]);
    }
}

void main()
{
    int list1[5] = {1, 2, 0, 5, 4};
    int list2[5] = {-1, 3, 4, -5, 1};
    int* result = NULL;
    apply(list1, list2, 5, mul, &result);
    for(int i=0; i<5; i++)
    {
        printf("%d, ", result[i]);
    }

}

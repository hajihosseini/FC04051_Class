#include <stdio.h>

int mystrlen(char* pch)
{
    int len = 0;
    while (pch[len] != 0)
        len++;
    return len;
}

int mystrlen(char* pch)
{
    int len = 0;
    while (*pch)
    {
        len++;
        pch++;
    }
    return len;
}

void str_cpy(char* pchsrc, char* pchdst, int len)
{

}

void str_append(
    char* pchstr1, int len1, 
    char* pchstr2, int len2,
    char* pchstrresult, int len)
{
    
}

void main()
{
    char name11[10] = "aliasdf";
    char name12[10] = "34132413";
    char name_result[30];
    str_append(name11, 10, name12, 10, name_result, 30);


    char name1[5] = {'a', 'l', 'i', 'e', 0 };
    int i = 0;
    char* pch = name1;
    while (i<5)
    {
        printf("%c", *pch);
        pch++;
        i++;
    }

}

void main5()
{
    char c;
    char name1[5] = {'a', 'l', 'i', 'e' };
    char name2[5] = {'m', '\0', 'r', 'y', '\0' };
    char name3[5] = {'z', 'h', 'a', 'l', '\0' };
    char name[20] = "ali is very good";

    int i = 0;
    while (i< 100)
    {
        name[16+i] = '*';
        printf("%d - %s\n", i, name);
        i++;
    }
    // printf("%s\n", name2);
    // printf("%s\n", name1);
}


    // while (i<5)
    // {
    //     printf("%d      %c\n", name[i], name[i]);
    //     i++;
    // }


void main2()
{
    int x; // 4
    long long int x2; // 8
    double d; // 8 
    float f; // 4
    char c; // 1 byte


    while (1)
    {
        char ch = 65;
        scanf("%c", &ch);
        printf("%d\n", ch);
    }
}
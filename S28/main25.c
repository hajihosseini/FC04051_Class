#include <stdio.h>

int mystrlen1(char* pch)
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


int is_equal2(char* pch1, char* pch2)
{
    for (   int i = 0;
            pch1[i] || pch2[i];
            i++    
        )
    {
            // *(pch1+i)
        if (pch1[i] != pch2[i])
            return 0;
    }
    return 1;

}

int is_equal(char* pch1, char* pch2)
{
    while (*pch1 && *pch2)
    {
        if (*pch1 != *pch2)
            return 0;
        pch1++;
        pch2++;
    }
    return *pch1 == *pch2;
}

void main()
{
    char pch_orig[20] = "12345678";
    char* pch = pch_orig;
    char pch2[20] = "12345678";
    int r = is_equal(pch_orig, pch2);

    r = 0x3457890;
    int* w = r;
    scanf("", &r)



    // char* pch = pch_orig;
    // *(pch+3) = 'a';
    // printf("%s\n", pch_orig);
}
void main10()
{
    // char name11[10] = "aliasdf";
    // char name12[10] = "34132413";
    // char name_result[30];
    // char name13413[] = "1234123";
    // char* pch2 = "23749128374";
    // str_append(name11, 10, name12, 10, name_result, 30);


    // char name1[5] = {'a', 'l', 'i', 'e', 0 };
    // int i = 0;
    // char  *pch = name1;
    // while (i<5)
    // {
    //     printf("%c", name1[i]);
    //     printf("%c", *pch);
    //     pch++;
    //     i++;
    // }

    char * pch = "1234567890";
    int i = 0;
    while (i < 5)
    {
        printf("%p, %c\n", pch, *pch);
        pch+=2;
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
#include <stdio.h>

int mylen(char* pch)
{
    int l = 0;
    while (pch[l])
        l++;
    return l;
}

void str_cpy(char* pchsrc, char* pchdst, int len)
{
    int i = 0;
    while(pchsrc[i])
    {
        pchdst[i] = pchsrc[i];
        i++;
    }
    pchdst[i] = 0;
}

void str_cpy_proper(char* pchsrc, char* pchdst, int len)
{
    int i = 0;
    while(*pchsrc && (i < len-1))
    {
        *pchdst = *pchsrc;
        pchdst++;
        pchsrc++;
        i++;
    }
    *pchdst = 0;
}

void str_cpy1(char* pchsrc, char* pchdst, int len)
{
    int i = 0;
    while (i < len)
    {
        pchdst[i] = pchsrc[i];
        i++;
    }
    pchdst[i] = 0;
}

void str_append(
    char* pchstr1, 
    char* pchstr2, 
    char* pchstrresult, int len)
{
    int i = 0;
    while(*pchstr1 && i < (len-1))
    {
        i++;
        *pchstrresult = *pchstr1;
        pchstr1++;
        pchstrresult++;
    }

    while(*pchstr2 && i < (len-1))
    {
        i++;
       *pchstrresult = *pchstr2;
        pchstr2++;
        pchstrresult++;
    }
    *pchstrresult = 0;
}

void marriage(char* pch1, char*pch2, char* pmariage)
{
    
}

void add(int a, int b, int* pc)
{
    *pc = a + b;
}


void main()
{
    int c = 0;
    add(5, 10, &c);
    printf("%d\n", c);

    char name11[60] = "12345678901234567845678945678956734567890";
    char name1[20] = "1234567890";
    char name2[20] = "asdfghjkl";
    char name_result[40];
    // str_cpy(name11, name_result, 10);
    str_append(name1, name2, name_result, 40);
    printf("%s\n%s\n%s", name_result, name1, name2);
    // str_append(name11, 10, name12, 10, name_result, 30);
}



    // char name12[10] = "34132413";
    // char name13413[] = "1234123";
    // char* pch2 = "23749128374";

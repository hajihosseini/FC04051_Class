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
// ali = "1234567890"
// mar = "abdefghijklmnop"
// ezd = "1a2b3d4e5f6g7h8i9j0klmnop"
void marriage(char* pch1, char*pch2, char* pmariage, int mar_len)
{
    int i=0;
    while(*pch1 && *pch2  && (i<mar_len-1))
    {
        *pmariage = *pch1;
        pmariage++;
        pch1++; i++;
        *pmariage = *pch2;
        pmariage++;
        pch2++; i++;
    }

    while(*pch1  && (i<mar_len-1))
    {
        *pmariage = *pch1;
        pmariage++; i++;
        pch1++;
    }

    while(*pch2  && (i<mar_len-1))
    {
        *pmariage = *pch2;
        pmariage++; i++;
        pch2++;
    }

    *pmariage = 0;
}

int min(int a, int b)
{
    return a < b ? a : b;
}
int max(int a, int b)
{
    return a > b ? a : b;
}

void marriage2(char* pch1, char*pch2, char* pmariage, int mar_len)
{
    int l1 = mylen(pch1);
    int l2 = mylen(pch2);

    for (int i=0; i<min(l1, l2); i++)
    {
        pmariage[2*i] = pch1[i];
        pmariage[2*i+1] = pch2[i];
    }

    for (int i=min(l1,l2); i<max(l1, l2); i++)
    {
        pmariage[min(l1,l2)+i] = l1 > l2 ? pch1[i] : pch2[i];
    }

    pmariage[l1+l2] = 0;
}


void marriage2(char* pch1, char*pch2, char* pmariage, int mar_len)
{
    char* pmp = pmariage;
    while(*pch1)
    {
        *pmp = *pch1;
        pmp+=2;
        pch1++;
    }
    pmp = pmariage+1;
    while (pch2)
    {
        *pmp = *pch2;
        pmp+=2;
        pch2++;
    }
}



void add(int a, int b, int* pc)
{
    *pc = a + b;
}


void main6789()
{
    char ali[20] = "1234567890";
    char mar[20] = "abdefghijklmnop";
    char ezd[14];// = "1a2b3d4e5f6g7h8i9j0klmnop"
    marriage(ali, mar, ezd, 14);
    printf("%s\n", ezd);

}

void main5678()
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

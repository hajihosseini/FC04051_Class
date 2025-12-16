#include<stdio.h>
#include<stdlib.h>

char** split(char* pch, char del, int* pcount)
{
    int i = 0;
    int count=0;
    while (pch[i])
    {
        if (pch[i] == del)
            count++;
        i++;
    }
    char ** ppresult = malloc((count+1) * sizeof(char*));
    i=0;
    count = 0;
    while (pch[i])
    {
        int j = 0;
        while(pch[i+j] != del && pch[i+j])
            j++;
        int word_len = j;
        ppresult[count] = malloc(word_len+1);
        ppresult[count][j--] = 0;
        while (j >= 0)
        {
            ppresult[count][j] = pch[i+j];
            j--;
        }
        
        i+=word_len;
        if (pch[i] == del)
            i++;
        count++;
    }
    *pcount = count;
    return ppresult;
}

void main()
{
    char* pch = "213 34 1234123 343 33333 234 1234 1234";
    int count=0;
    char** ptokens = split(pch, ' ', &count);
    for(int i=0; i<count; i++)
        printf("%s\n", ptokens[i]);
}






char* make_num_string(int n)
{
    char * buf = malloc(10*sizeof(char));
    int len =0;
    while (n > 0)
    {
        char c = n % 10;
        buf[len++] = '0' + c;
        n = n / 10;
    }
    buf[len] = 0;

    len--;

    for (int i=len; i>len/2; i--)
    {
        char c = buf[i];
        buf [i] = buf[len-i];
        buf[len-i] = c;
    }
    return buf;
}

int add(int a, int b)
{
     return a + b;
}

void main2343()
{
    int w = add(5, 4);
    char* mynum = make_num_string(123456789);
    // 
    printf("%s\n", mynum);
    free(mynum);
    printf("%d\n", 123456789);
}

void main2()
{
    int nums[10];
    for(int i=0; i<11; i++)
        nums[i] = i*100;
    

    int i = 0;
    while (i<10)
        printf("%d\n", nums[i++]);

    i = 0;
    while (i<10)
        printf("%d\n", nums[++i]);
}
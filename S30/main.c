#include <stdio.h>

void conca6t(int argc, char** argv, char* result)
{
    int i=0;
    while (i<argc)
    {
        char* argv_pch = *argv;
        while (*argv_pch)
        {
            *result = *argv_pch;
            result++;
            argv_pch++;
        }
        argv++;
        i++;
    }
    *result = 0;
}

void split(char* str, char del, char** result, int* count)
{
    int p = 0;
    *count = 0;
    for(int i = 0; str[p] ;i ++)
    {
        result[i] = &(str[p]);
        // char* segment = result[i];
        char segment[100];
        result[i] = segment;
        int j = 0;
        while (str[p] != del)
        {
            segment[j] = str[p];
            p ++;
            j ++;
        }
        segment[j] = 0;
        p ++;
        *count += 1;
    }
}

void split222s(char* pch, char del, char** result, int* pcount)
{
    int i = 0;
    *pcount = 0;
    result[(*pcount)++] = pch;
    while (pch[i] != 0)
    {
        if (pch[i] == del)
        {
            pch[i] = 0;
            result[(*pcount)++] = &(pch[i+1]);
        }
        i++;
    }
}

void concat(int argc, char** argv, char* result)
{
    int l = 0;
    for(int i=0; i<argc; i++)
        for (int j=0; argv[i][j] != 0; j++)
            result[l++] = argv[i][j];
    result[l] = 0;
}



void main()
{
    char buf[100] = "adf adf sdds 567890 hjk yuio";
    char* result[100];
    int count;
    split(buf, ' ', result, &count);
    for(int i=0; i<count; i++)
        printf("%s\n", result[i]);
}

int mai23n(int argc, char** argv)
{
    char buf[100];
    concat(argc, argv, buf);
    printf("%s\n", buf);
}
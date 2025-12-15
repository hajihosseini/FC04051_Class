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

void split(char* pch, char del, char** result, int* count)
{

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
#include<stdio.h>
#include<stdlib.h>

typedef struct _mstring 
{
    char* pch;
    int capacity;
    int size;
} mstring;

int str_len(const char* pch)
{
    int i;
    for(i=0; pch[i]; i++);
    return i;
}

void str_assign(mstring* str, const char* pch)
{
    int memsize = str_len(pch) + 1, i;
    str->pch = (char*) malloc(memsize * sizeof(char));
    for(i=0; pch[i]; i++)
        str->pch[i] = pch[i];
    str->pch[i] = 0;
    str->capacity = memsize-1;
    str->size = memsize-1;
}

void str_append(mstring* str, const char* pch)
{
    int size = str_len(pch);
    int new_size = size + str->size + 1;
    char* pchnew = (char*) malloc(new_size);
    for(int i=0; i<str->size; i++)
        pchnew[i] = str->pch[i];
    
    for(int i=0; i<size; i++)
        pchnew[i+str->size] = pch[i];
    
    pchnew[new_size-1] = 0;
    free(str->pch);
    str->pch = pchnew;
    str->capacity = new_size-1;
    str->size = new_size-1;

}

void str_remove(mstring* str, int start, int end)
{
    int rmlen = end-start+1, i;
    for(i=start; str->pch[i+rmlen]; i++)
        str->pch[i] = str->pch[i+rmlen];
    str->pch[i] = 0;
    str->capacity -= rmlen;
    str->size -= rmlen;
    
}
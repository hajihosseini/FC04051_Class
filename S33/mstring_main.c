#include <stdio.h>
#include "mstring.h"

int mstrcmp(const char* pch1, const char* pch2)
{
    int i=0;
    while (pch1[i] && pch2[i]) 
    {
        if (pch1[i] != pch2[i])
            return 0;
        i++;
    }
    return pch1[i] == pch2[i];
}


#define ASSERT(x) if (x) printf("succeess"); else printf("fail")
#define CHECK(x) if (x) printf("succeess"); else printf("fail")

void main()
{
    int x = 5;
    ASSERT( x == 5 );
    mstring s;    //0123456789
    str_assign(&s, "123456789123456789");
    str_remove(&s, 4, 8);
    CHECK(mstrcmp(s.pch, "1234123456789"));
    CHECK(s.capacity == 13);
    CHECK(s.size == 13);
    free(s.pch);    
}
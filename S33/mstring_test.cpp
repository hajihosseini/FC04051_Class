#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include "doctest.h"
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

TEST_CASE("assign test") {
    char* pch;
    mstring s;
    str_assign(&s, "123456789");
    CHECK(mstrcmp(s.pch, "123456789"));
    CHECK(s.capacity == 9);
    CHECK(s.size == 9);
    free(s.pch);
}

TEST_CASE("append test") {
    mstring s;
    str_assign(&s, "123456789");
    str_append(&s, "asdfghjkl");
    CHECK(mstrcmp(s.pch, "123456789asdfghjkl"));
    CHECK(s.capacity == 18);
    CHECK(s.size == 18);
    free(s.pch);
}


TEST_CASE("remove test") {
    mstring s;    //0123456789
    str_assign(&s, "123456789123456789");
    str_remove(&s, 4, 8);
    CHECK(mstrcmp(s.pch, "1234123456789"));
    CHECK(s.capacity == 13);
    CHECK(s.size == 13);
    free(s.pch);
}
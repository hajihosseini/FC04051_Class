#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include "doctest.h"
#include "mylist.h"

TEST_CASE("append test") {
    list mlist;
    list_append(&mlist, 1.1);
    CHECK(mlist.size == 1);
    CHECK(mlist.items[0] == 1.1);
}

TEST_CASE("pop test") {
    list mlist;
    list_append(&mlist, 1.1);
    list_append(&mlist, 1.2);
    list_append(&mlist, 1.3);
    CHECK(mlist.size == 3);
    list_pop(&mlist, 1);
    CHECK(mlist.items[0] == 1.1);
    CHECK(mlist.items[1] == 1.3);
    CHECK(mlist.size == 2);
}
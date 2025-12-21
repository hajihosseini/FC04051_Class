#include "mstring.h"


void main()
{
    mstring s;
    str_assign(&s, "34567890");
    str_append(&s, "fghjl"); // 34567890fghjl
}
#include "mylist.h"

void main()
{
    list mynums;
    list_append(&mynums, 5.1);
    list_append(&mynums, 5.2);
    list_append(&mynums, 5.3);
    list_append(&mynums, 5.4);
    list_print(&mynums);
}





























// double* list_append(double* items, int* size, int* capacity, double item)
// {
//     if (*size == *capacity || *capacity == 0)
//     {
//         int new_capacity = *capacity == 0 ? 1 : *capacity * 2;
//         double* new_items = malloc(new_capacity * sizeof(double));
//         for(int i=0; i<*capacity; i++)
//             new_items[i] = items[i];
//         free(items);
//         items = new_items;
//         *capacity = new_capacity;
//     }
//     items[*size] = item;
//     (*size)++;
//     return items;
// }

// void print_list(double* items, int size)
// {
//     for(int i=0; i<size; i++)
//         printf("%lf ", items[i]);
//     printf("\n");
// }

// double list_pop(double* items, int* size, int idx)
// {
//     double item = *(items+idx); // items[idx]
//     for (int i=idx+1; i<*size; i++)
//         items[i-1] = items[i];
//     (*size)--;
//     return item;
// }


// double pop_list(double* items, int* size)
// {
//     (*size)--;
//     return items[*size];
// }

// void main()
// {
//     int list_size = 0;
//     int list_capacity = 0;
//     double* list_nums = NULL;
// }
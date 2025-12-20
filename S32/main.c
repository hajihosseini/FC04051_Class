#include<stdio.h>
#include<stdlib.h>


double* list_append(double* items, int* size, int* capacity, double item)
{
    if (*size == *capacity || *capacity == 0)
    {
        int new_capacity = *capacity == 0 ? 1 : *capacity * 2;
        double* new_items = malloc(new_capacity * sizeof(double));
        for(int i=0; i<*capacity; i++)
            new_items[i] = items[i];
        free(items);
        items = new_items;
        *capacity = new_capacity;
    }
    items[*size] = item;
    (*size)++;
    return items;
}

void print_list(double* items, int size)
{
    for(int i=0; i<size; i++)
        printf("%lf ", items[i]);
    printf("\n");
}

double pop_list(double* items, int* size, int idx)
{
    
}


double pop_list(double* items, int* size)
{
    (*size)--;
    return items[*size];
}

void main()
{
    int list_size = 0;
    int list_capacity = 0;
    double* list_nums = NULL;

    list_nums = list_append(list_nums, &list_size, &list_capacity, 5.1);
    print_list(list_nums, list_size);
    list_nums = list_append(list_nums, &list_size, &list_capacity, 5.2);
    print_list(list_nums, list_size);
    list_nums = list_append(list_nums, &list_size, &list_capacity, 5.3);
    print_list(list_nums, list_size);
    int cap = list_capacity;
    for(int i=0; i<1000*1000; i++)
    {
        list_nums = list_append(list_nums, &list_size, &list_capacity, 5.3*i);
        if (cap != list_capacity)
        {
            printf("old-cap: %d, new-cap: %d\n", cap, list_capacity);
            cap = list_capacity;
        }
    }
    printf("size: %d, cap: %d", list_size, list_capacity);
}

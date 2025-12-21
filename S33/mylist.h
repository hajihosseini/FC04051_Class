#include<stdio.h>
#include<stdlib.h>

typedef struct _list {
    int capacity;
    int size;
    double* items;
} list;

void list_append(list* dlist, double item)
{
    if (dlist->size == dlist->capacity || dlist->capacity == 0)
    {
        int new_capacity = dlist->capacity == 0 ? 1 : dlist->capacity * 2;
        double* new_items = (double*) malloc(new_capacity * sizeof(double));
        for(int i=0; i<dlist->capacity; i++)
            new_items[i] = dlist->items[i];
        free(dlist->items);
        dlist->items = new_items;
        dlist->capacity = new_capacity;
    }
    dlist->items[dlist->size] = item;
    dlist->size++;
}

void list_print(list* dlist)
{
    for(int i=0; i<dlist->size; i++)
        printf("%lf ", dlist->items[i]);
    printf("\n");
}


double list_pop(list* dlist, int idx)
{
    double item = *(dlist->items+idx); // items[idx]
    for (int i=idx+1; i<dlist->size; i++)
        dlist->items[i-1] = dlist->items[i];
    dlist->size--;
    return item;
}


double list_pop_last(list* dlist)
{
    dlist->size--;
    return dlist->items[dlist->size];
}

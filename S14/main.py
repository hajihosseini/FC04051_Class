def MIN(lst):
    min = lst[0]
    for i in range(len(lst)):
        if lst[i]<min:
            min = lst[i]
    return min

def Remove(lst, value):
    lst_new = []
    count = 0
    for i in range(len(lst)):
        if lst[i]==value:
            count += 1
        else:
            lst_new.append(lst[i])
    return lst_new, count 

    
def Sort(lst):
    list_sort = []
    
    while(len(lst)>0):
        min = MIN(lst)
        lst, c = Remove(lst,min)

        for i in range(c):
            list_sort.append(min)

    return list_sort


a = [2,1,5, 2, 3,7,8,2]

# a_new, c = Remove(a,20)
# print(a_new)
# print(c)

print(Sort(a))

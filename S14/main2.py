def Reverse(lst):
    n = len(lst)
    for i in range(n//2):
        temp = lst[i]
        lst[i] = lst[n-i-1]
        lst[n-i-1] = temp
    return lst

print(Reverse([1,2,3,4]))
print(Reverse([1,2,3,4,5]))

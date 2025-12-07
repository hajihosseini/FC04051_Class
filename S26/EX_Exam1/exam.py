def isPrime(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True

def q6_reverse_prime_positions(lst):
    reverseindex = []
    for i in range(len(lst)):
        if isPrime(i):
            reverseindex.append(i)
    for i in range(len(reverseindex)//2):
        temp = lst[reverseindex[i]]
        lst[reverseindex[i]] = lst[reverseindex[len(reverseindex)-i-1]]
        lst[reverseindex[len(reverseindex)-i-1]] = temp
    return lst


def q2_nth_prime_number(n):
    i = 1
    counter = 0
    while(counter<n):
        if isPrime(i):
            counter += 1
        i+= 1
    return i-1

def q8_count_chrs(lst):
    dic = {}
    for i in range(len(lst)):
        str = lst[i]

        for chr in str:
            if CheckIn(dic,chr):
                dic[chr] += 1
            else:
                dic[chr] = 1

    return dic


def CheckIn(dic, key):
    keys = list(dic.keys())
    for i in range(len(keys)):
        if keys[i] == key:
            return True
    return False


def q5_count_substring(str, substr):
    counter = 0
    for i in range(len(str)-len(substr)+1):
        flag = True
        for j in range(len(substr)):
            if substr[j] == str[i+j]:
                continue
            else:
                flag = False
        if flag:
            counter+= 1
    return counter
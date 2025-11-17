a = [12,3,4,5.5,9]
print(a)
a.append(18)
print(a)


print(a[0])
print(a[3])
# print(a[6])

print(len(a))

def AVG(scores):
    size = len(scores)
    sum = 0
    for i in range(size):
        sum += scores[i]

    return sum/size


def AVG2(scores, weights):
    sum_s = 0
    sum_w = 0
    for i in range(len(scores)):
        sum_s += scores[i]*weights[i]
        sum_w += weights[i]

    return sum_s/sum_w

x = [12,13,16,20]
w = [3,3,2,1]

print(AVG(x))
print(AVG2(x,w))


def Append2(a,indx, val):
    a_list = []

    for i in range(indx):
        a_list.append(a[i])

    a_list.append(val)

    for i in range(indx,len(a)):
        a_list.append(a[i])
    
    return a_list

print(Append2([1,2,3,4],2,5))


y = [1,2,1,3,4,1,2,1,4,1,5,1]

def Count(lst, val):
    n = 0
    for i in range(len(lst)):
        if lst[i]==val:
            n+=1
    return n

print(Count(y,1))
print(Count(y,10))


print()

t = [4,1,7,20,3]

for i in range(len(t)):
    print(t[i])

print()

for i in t:
    print(i)


def SUM(lst):
    sum = 0
    for i in lst:
        sum += i

    # for i in range(len(lst)):
    #     sum += lst[i]
    
    return sum

print(SUM([1,2,3,4,5,6]))

q = [1,4,5,6,3,8]

if 5 not in q:
    print("OK")
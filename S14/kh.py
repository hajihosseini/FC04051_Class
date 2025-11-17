def F(number):
    result = 1
    for i in range(1, number+1):
        result *= i
    return result
def C(n,r):
    return F(n)//(F(r)*F(n-r))
def KH(n):
    for i in range(n):
        print((n-i)*"\t", end="")
        for j in range(i+1):
            print(C(i,j), end="\t\t")
        print()
KH(5)
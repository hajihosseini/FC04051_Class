def F(n):
    if n==1:
        return 1
    
    return n*F(n-1)


def Fib(n):
    if n==1 or n==2:
        return 1    
    return Fib(n-1)+Fib(n-2)


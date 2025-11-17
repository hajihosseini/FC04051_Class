while(False):
    print("OK")

def Isprime(n):
    if n==0:
        return False
    if n==1:
        return False
    
    for i in range(2,n):
        if n%i==0:
            return False
    return True

def SumIsPrime(lst):
    sum = 0
    for i in range(len(lst)):
        if Isprime(i):
            sum += lst[i]
    return sum

print(SumIsPrime([1,2,3,4,5,6,7,8,9,10,11,12]))
# print(Isprime(1))
# print(Isprime(2))
# print(Isprime(4))

# if Isprime(5)==True:
#     print("5 is prime!")

# if Isprime(5):
#     print("5 is prime!")

# else:
#     print("is not prime!")
def isPrime(n):
    if n==1:
        return 0
    
    for i in range(2,n):
        if n%i == 0:
            return 0 
    return 1

print(isPrime(1))
print(isPrime(2))
print(isPrime(3))
print(isPrime(5))
print(isPrime(6))
print(isPrime(9))
print(isPrime(11))
print(isPrime(19))


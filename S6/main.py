def factorial(n):
    result = 1
    for i in range(1,n+1):
        result *= i
    return result


y = factorial(4)


def Add(a,b):
    return a+b
    # result = a+b
    # return result

r = Add(3,4)
print(r)
print(Add(5,4))


x = 12
y = 7

print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(x//y)
print(x%y)

print(2**3)

x = 5
print(type(x))

y = 2.5
print(type(y))

z = 'a'
print(type(z))

x = 6.7
print(type(x))



def Add2(a,b):
    result = 0
    for i in range(a,b+1):
        result += i
    
    return result

t = Add2(5,9)
print(t)


def Add3(a,b):
    result = 0
    for i in range(a,b+1,2):
        result += i
        #result = result + i
    
    return result

q = Add3(3,9)
w = Add3(3,10)

print(q)
print(w)


def Add4(a,b):
    result = 0
    if a%2==1:
        for i in range(a,b+1,2):
            result +=i
    else:
        for i in range(a+1,b+1,2):
            result += i
    return result
    

r = Add4(4,15)

def Add5(a,b):
    result = 0
    for i in range(a,b+1):
        if i%2==1:
            result += i

    return result
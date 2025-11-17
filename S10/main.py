def BMM(a,b):
    bmm = 1
    for i in range(1,a+1):
        if (a%i==0 and b%i==0):
            bmm = i
    return bmm


def BMM2(a,b):
    for i in range(a,0,-1):
        if (a%i==0 and b%i==0):
            return i
        

print(BMM(8,12))
print(BMM2(8,12))
print(BMM(3,5))
print(BMM2(3,5))


def KMM(a,b):
    bmm = BMM(a,b)
    return (a*b)//bmm
    #return (a*b)//BMM(a,b)

def KMM2(a,b):
    for i in range(b,(a*b)+1):
        if (i%a==0 and i%b==0):
            return i
        
print(KMM(8,12))
print(KMM2(8,12))
print(KMM(3,5))
print(KMM2(3,5)) 


def KMM3(a,b):
    i = 1
    kmm = b
    while(kmm%a!=0 or kmm%b!=0):
        kmm = b*i
        i +=1

    return kmm


def power(a,b=1):
    # a = 3
    # b = 4
    result = 1
    for _ in range(1,b+1):
        result = result * a
        #return result
    
    #print(result)
    return result
    #print(result)



x = power(2,3)
y = power(3,5)
z = power(4,2)
q = power(8)

print(x+z)
print(power(3,4))
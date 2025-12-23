
def add(a,b):
    return a + b

def mul(a,b):
    return a * b

def dif(a,b):
    return a - b

def list_add(a,b):
    result = []
    for i in range(len(a)):
        result.append(add(a[i], b[i]))
    return result

def list_mul(a,b):
    result = []
    for i in range(len(a)):
        result.append(mul(a[i], b[i]))
    return result

def list_dif(a,b):
    result = []
    for i in range(len(a)):
        result.append(dif(a[i], b[i]))
    return result

def list_apply(a, b, fn):
    result = []
    for i in range(len(a)):
        result.append(fn(a[i], b[i]))
    return result

nums1 = [1,2,3,4,4,8,3]
nums2 = [-1,-2,3,0,4,10,3]

print(list_mul(nums1, nums2))
print(list_apply(nums1, nums2, mul))
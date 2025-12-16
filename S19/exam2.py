def q0_pythagoras(m,n):
    x = m**2 + n**2
    return x**0.5


def q2_get_last_index2(nums, v):
    found = -1
    for i in range(len(nums)):
        if nums[i]==v:
            found = i
    return found

def q2_get_last_index(nums, v):
    for i in range(len(nums)-1, -1, -1):
        if nums[i]==v:
            return i
    return -1
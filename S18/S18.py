import math

def q1_add_if_odd(a,b):
    if ((a+b)%2==1):
        return a+b
    return -(a+b)

def q2_average(arr):
    result = 0
    for i in arr:
        result += i
    result = result/len(arr)
    return round(result,2)
    

def q3_is_closest_to_average(arr):
    avg = q2_average(arr)

    min = abs(arr[0]-avg)
    index = 0

    for i in range(len(arr)):
        if abs(arr[i]-avg)<min:
            min = abs(arr[i]-avg)
            index = i
    
    return arr[index]




def q4_split_word_to_characters(s):
    pass

def q5_average_all(arr):
    pass

def q6_Check_Arithmetic_or_Geometric(arr, n):
    pass

def q7_determinant_2_2(arr):
    pass
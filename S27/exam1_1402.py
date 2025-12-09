def abs(x):
    if x<0:
        return -x
    return x


def q0_manhatan_distance(x1,y1,x2,y2):
    return abs(x2-x1)+abs(y2-y1)


def q1_closest_neighbor(lst):
    min = abs(lst[1]-lst[0])
    for i in range(len(lst)-1):
        if abs(lst[i]-lst[i+1])<min:
            min = abs(lst[i]-lst[i+1])

    return min


def q2_add_nums(lst1, lst2):
    lst3 = []

    for i in range(len(lst1)):
        lst3.append(lst1[i]+lst2[i])
    return lst3

def q3_closest_two_friends(lst):
    index1 = 0
    index2 = 1
    min = abs(lst[0]-lst[1])
    for i in range(len(lst)):
        for j in range(i+1,len(lst)):
            if abs(lst[i]-lst[j])<min:
                min = abs(lst[i]-lst[j])
                index1 = i
                index2 = j

    return index1, index2, min

def q4_apply_rule_once(str, lst):
    newStr = ""
    rule0 = lst[0]
    rule1 = lst[1]

    for i in range(len(str)):
        if str[i] == rule0:
            newStr += rule1
        else:
            newStr+= str[i]

    return newStr


def q5_apply_rules_once(str, lst):
    newStr = str
    for i in range(len(lst)):
        newStr = q4_apply_rule_once(str, lst[i])
        str = newStr
    
    return newStr


def q6_apply_rules_n(str, lst, itr):
    for i in range(itr):
        str = q5_apply_rules_once(str, lst)

    return str
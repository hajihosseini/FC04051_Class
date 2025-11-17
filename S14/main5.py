def CheckIN(string, value):
    for i in range(len(string)):
        if string[i]==value:
            return True
    return False


def RemoveAIOEU(str1):
    newSTR = ""
    AIOEU = "aioueAIOUE"
    for i in range(len(str1)):
        if CheckIN(AIOEU, str1[i]):
            continue
        else:
            newSTR += str1[i]

    return newSTR

print(RemoveAIOEU("abdeusno"))


s1 = "abdjfsfeiojrwe"
s2 = "bdj"

if s2 in s1:
    print("ok")
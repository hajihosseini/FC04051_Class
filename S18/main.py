def CheckSubstring(s,s1):
    for i in range(len(s)-len(s1)+1):
        flag = True
        for j in range(len(s1)):
            if s[i+j]!=s1[j]:
                flag = False
                break
        if flag:
            return True
        
    return False
        

print(CheckSubstring("asdfgaf","sdf"))
print(CheckSubstring("aabsbdbs","bsad"))
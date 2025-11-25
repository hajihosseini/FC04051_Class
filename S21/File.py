import random

def Save_Int_File(filename, n, a, b):
    f = open(filename, 'w')

    for i in range(n):
        num = random.randint(a,b)
        f.write(str(num)+"\n")
    
    f.close()


#Save_Int_File("numbers.txt", 50, 1, 20)
#print(random.randint(10,20))

def Get_Index(arr, value):
    for i in range(len(arr)):
        if arr[i] == value:
            return i


def Count_Nums_File_List(filename):
    f = open(filename, 'r')
    lines = f.readlines()

    UniqueNumbers = []
    CountNums = []

    for li in lines:
        li = int(li.strip())
        if li in UniqueNumbers:
            index = Get_Index(UniqueNumbers, li)
            CountNums[index] += 1
        
        else:
            UniqueNumbers.append(li)
            CountNums.append(1)

    
    for i in range(len(UniqueNumbers)):
        print(f"{UniqueNumbers[i]}:{CountNums[i]}")


Count_Nums_File_List("numbers.txt")


def Count_Nums_File_Dict(filename):
    f = open(filename, 'r')
    lines = f.readlines()

    DictNums = {}

    for li in lines:
        li = int(li.strip())

        if li in DictNums:
            DictNums[li] += 1
        else:
            DictNums[li] = 1

    for k, v in DictNums.items():
        print(f"{k}:{v}")

print()
Count_Nums_File_Dict("numbers.txt")



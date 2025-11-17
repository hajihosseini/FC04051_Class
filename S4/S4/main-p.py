
def khat_bekesh(w, c):
    print(" +", end="")
    for i in range(w):
        print(c, end="")
    print("+ ")

def sookht(w,h,c):
    for i in range(h):
        khat_bekesh(w, c)
    khat_bekesh(w, "-")

#sookht(15,8,"&")




def kolahakbip():
    print(r"     ^      ")
    print(r"    /|\     ")
    print(r"   //|\\    ")
    print(r"  ///|\\\   ")
    print(r" +-------+  ")

def kolahak(h):
    print(r"     ^      ")
    for i in range(h):
        print(" "*(h+1-i), end="")
        if (i == 8):
            print("\\"*(i+1))
        else:
            print("/"*(i+1))

    print(r" +-------+  ")
kolahak(10)






















# def sookht(w,h):
#     for i in range(h):
#         print(" +", end="")
#         for i in range(w):
#             print("*", end="")
#         print("+")
#     print(" +", end="")
#     for i in range(w):
#         print("-", end="")
#     print("+")
#sookht(20,7)


# def sookht(w,h):
#     for i in range(h):
#         print(" +" + "*" * w + "+  ")
#     print(" +" + "-" * w + "+  ")

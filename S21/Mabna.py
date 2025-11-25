def Binary_To_Decimal(bits):
    power = len(bits)-1
    decimal = 0
    for b in bits:
        decimal += int(b) * (2**power)
        power -= 1
    
    return decimal

print(Binary_To_Decimal("1111"))
print(Binary_To_Decimal("1011"))
print(Binary_To_Decimal("11011"))
print(Binary_To_Decimal("11"))
print(Binary_To_Decimal("110"))


def Decimal_To_Binary(nums):
    if nums == 0:
        return "0"

    bits = ""
    while(nums>0):
        r = nums%2
        nums = nums//2
        bits = str(r) + bits
    
    return bits


print()
print(Decimal_To_Binary(15))
print(Decimal_To_Binary(11))
print(Decimal_To_Binary(27))
print(Decimal_To_Binary(3))
print(Decimal_To_Binary(6))

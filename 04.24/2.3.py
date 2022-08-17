a = int(input())
b = int(input())
if a % b == 0:
    print(a, " делится на ", b, " нацело")
    print("Частное: ", a // b)

if a % b != 0:
    print(a, " не делится на ", b, " нацело")
    print("Частное: ", a // b )
    print("Остаток: ", a % b)
    
    
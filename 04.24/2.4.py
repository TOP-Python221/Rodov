a = int(input())
b = int(input())
c = int(input())

if a < 0:
    a = int(0)
    if b < 0:
            b = int(0)
            if c < 0:
                    c = int(0)
                    print(a + b + c)
            print(a + b + c)
    print(a + b + c)
else:
    print(a + b + c)
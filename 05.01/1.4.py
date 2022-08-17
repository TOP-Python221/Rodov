# int(ord('a')) 97
# int(ord('b')) 98
# int(ord('c')) 99
# int(ord('d')) 100
# int(ord('e')) 101
# int(ord('f')) 102
# int(ord('g')) 103
# int(ord('h')) 104

x1 = input()
y1 = int(input())
x2 = input()
y2 = int(input())

sum1 = (int(ord(x1)) + y1)
sum2 = (int(ord(x2)) + y2)

if sum1 - sum2 > 3:
    print('Нет')
else:
    print('Да')



print(int(ord(x1)) + y1)
print(int(ord(x2)) + y2)

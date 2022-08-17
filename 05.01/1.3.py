
# x1 = input()
# y1 = int(input())
# x2 = input()
# y2 = int(input())

# if x1 == x2 or y1 == y2:
    # print('Да')
# else:
    # print('Нет')
# От 98 До 112
    
    
x1 = input()
y1 = int(input())
x2 = input()
y2 = int(input())

if x1 == x2 or y1 == y2:
    if 98 <= int(ord(x1)) + y1 <= 112 and 98 <= int(ord(x2)) + y2 <= 112:
        print('Да')
    else:
        print('Введите корректные данные')
else:
    print('Нет')

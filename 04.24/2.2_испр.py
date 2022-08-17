age = int(input())

if age < 0:
    print('Введите корректные данные')
elif age <= 13:
    print("Детство")
elif age <= 24:
    print("Молодость")
elif age <= 59:
    print("Зрелость")
else:
    print("Старость")

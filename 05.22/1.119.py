numbers = ''
sum_of_num = 0
average = 0
below_num = ''
upper_num = ''

# ИСПРАВИТЬ: то же самое, что и в предыдущей задаче
while True:
    vvod = input('Введите число: ')
    if vvod == '':
        break
    numbers += vvod + ','

# ИСПРАВИТЬ: numbers = [int(n) for n in numbers.split(',') if n]
numbers = numbers.split(',')

if '' in numbers:
    numbers.pop()

# ИСПРАВИТЬ: sum([int(n) for n in numbers]), если в numbers всё ещё строки, если уже числа, то просто sum(numbers)
for i in range(len(numbers)):
    sum_of_num += int(numbers[i])

average = sum_of_num / len(numbers)

print(f'Среднее число: {average}')

# ИСПРАВИТЬ: переписать с использованием представлений списков
for j in range(len(numbers)):
    # ИСПРАВИТЬ: числа и строки сравниваются по-разному
    if numbers[j] < str(average):
        below_num += str(numbers[j]) + ', '
    elif numbers[j] > str(average):
        upper_num += str(numbers[j]) + ', '
        
print(f'Числа ниже среднего: {below_num}')
print(f'Числа выше среднего: {upper_num}')

# print(numbers)
# print(sum_of_num)


# ДОБАВИТЬ: закомментированный вывод результатов нескольких запусков скрипта с различными входными данными
# tests:


# ИТОГ: не увидел представлений списков, переписать — 1/4

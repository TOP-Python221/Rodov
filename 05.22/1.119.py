numbers = ''
sum_of_num = 0
average = 0
below_num = ''
upper_num = ''
while True:
    vvod = input('Введите числo: ')
    if vvod == '':
        break
    numbers += vvod + ','
    
numbers = numbers.split(',')

if '' in numbers:
    numbers.pop()

for i in range(len(numbers)):
    sum_of_num += int(numbers[i])

average = sum_of_num / len(numbers)

print(f'Среднее число: {average}')

for j in range(len(numbers)):
    if numbers[j] < str(average):
        below_num += str(numbers[j]) + ', '
    elif numbers[j] > str(average):
        upper_num += str(numbers[j]) + ', '
        
print(f'Числa ниже среднего: {below_num}')
print(f'Числa выше среднего: {upper_num}')
#print(numbers)
#print(sum_of_num)



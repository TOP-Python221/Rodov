
numbers = ''
while True:
    vvod = input('Введите числo: ')
    if vvod == '':
        break
    numbers += vvod + ','
    
numbers = numbers.split(',')

if '' in numbers:
    numbers.pop()

if len(numbers) < 5:
    print('Введите больше 4-ёх чисел')
else:
    numbers.sort()
    print(numbers)
        

# ИСПРАВИТЬ: с учётом того, что здесь мы работаем уже со списками, то и заполнять вводимыми объектами стоило бы сразу список — заодно и проблемы с последним пустым элементом не было бы
numbers = ''
while True:
    vvod = input('Введите числo: ')
    if vvod == '':
        break
    numbers += vvod + ','

# ИСПРАВИТЬ: вот здесь пригодилось бы представление списка для преобразования строк в числа
numbers = numbers.split(',')

if '' in numbers:
    numbers.pop()

# КОММЕНТАРИЙ: это условие скорее из задачи 112, здесь в нём нет необходимости
if len(numbers) < 5:
    print('Введите больше 4-ёх чисел')
else:
    # ИСПРАВИТЬ: метод sort() — это хорошо, но противоречит условию задачи — вам нужно не менять исходный список чисел, а сформировать новые — здесь-то вам представления списков и пригодятся
    # КОММЕНТАРИЙ: к тому же сортировка строк отличается от сортировки чисел
    numbers.sort()
    print(numbers)


# ДОБАВИТЬ: закомментированный вывод результатов нескольких запусков скрипта с различными входными данными
# tests:


# ИТОГ: не увидел представлений списков, переписать — 1/4

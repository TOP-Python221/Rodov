# ДОБАВИТЬ: аннотации типов параметров и возвращаемого значения
def date(day, month, year):
    # ДОБАВИТЬ: документацию функции
    ordinalDate = 366 - (366 - day - 30*month)
    if month > 12 or day > 31:
        print('Введите корректные данные')
    else:   
        print(f'Введённая дата является {ordinalDate} днём {year} года')
   
date(12, 12, 2001)


# ДОБАВИТЬ: закомментированный вывод результатов нескольких запусков скрипта с различными входными данными
# tests:

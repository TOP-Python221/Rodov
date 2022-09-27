def date(day, month, year): 
    ordinalDate = 366 - ((366 - day) - (month * 30))
    if month > 12 or day > 31:
        print('Введите корректные данные')
    else:   
        print(f'Введённая дата является {ordinalDate} днём {year} года')
   
date(12, 12, 2001)

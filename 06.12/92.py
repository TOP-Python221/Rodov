def date(ordinalDate):
    date1 = ordinalDate // 30, ordinalDate % 30
    # date1 = '.'.join(date1)
    print(ordinalDate // 30, ordinalDate % 30)

date(366)
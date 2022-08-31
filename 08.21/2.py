import datetime as dt


class DateTime:
    def __init__(self, time_zone: str) -> str:
        self.time_zone = time_zone

    def inf(self) -> str:
        """Информирует пользователя какой часовой пояс он выбрал в зависимости от введённого значения."""
        if self.time_zone == '2':
            print('Kaliningrad Time')

        elif self.time_zone == '3':
            print('Moscow Time')

        elif self.time_zone == '4':
            print('Samara Time')

        elif self.time_zone == '5':
            print('Yekaterinburg Time')

        elif self.time_zone == '6':
            print('Omsk Time')

        elif self.time_zone == '7':
            print('Krasnoyarsk Time')

        elif self.time_zone == '8':
            print('Irkutsk Time')

        elif self.time_zone == '9':
            print('Yakutsk Time')

        elif self.time_zone == '10':
            print('Vladivostok Time')

        elif self.time_zone == '11':
            print('Magadan Time')

        elif self.time_zone == '12':
            print('Kamchatka Time')

        else:
            print('Сказано же: от 2 до 12!')

    def diff(self) -> str:
        """Указывает количество часов в другом указанном пользователе регионе.

        К сожалению, смог додумать только то, как можно вывести количество часов, а не полное время."""
        date_t = str(dt.datetime.today()).split(' ')[1]
        hour = date_t.split(':')[0]
        print('Время в чужом часовом поясе: ')
        print(int(time_zone2.__dict__['time_zone']) + int(hour))

# экземпляры класса DateTime
time_zone1 = DateTime(input('Введите Ваш часовой пояс России в UTC(от 2 до 12): '))
time_zone2 = DateTime(input('Введите чужой часовой пояс России В UTC(от 2 до 12): '))

print(time_zone1.inf())
print(time_zone1.diff())

print(time_zone2.inf())
print(time_zone1.diff())

# date_t = str(dt.datetime.today()).split(' ')[1]
# hour = date_t.split(':')[0]
# print(date_t)
# print(f'Часы: {hour}', f'Тип: {type(hour)}')
# print(type(date_t))
# print(time_zone1)

"""Модель классов университета."""

from enum import Enum


class Sex(Enum):
    MALE = 'm'
    FEMALE = 'f'

class Degree(Enum):
    BACHELOR = 'b'
    MASTER = 'm'
    DOCTOR = 'd'

# ДОБАВИТЬ: перечислитель EducationForm


class Person:
    def __init__(self, name: str,
                 birthdate: str,
                 sex: Sex):
        # ОТВЕТИТЬ: вот это правильно! а вы понимаете, как этот атрибут будет использоваться (имея в виду и свойство)?
        self.__name = name
        self.birthdate = birthdate
        self.sex = sex

    @property
    def name(self):
        return self.__name

    # ДОБАВИТЬ: метод __str__()


class Employee(Person):
    def __init__(self,
                 name: str,
                 birthdate: str,
                 sex: Sex,
                 position: str,
                 salary: int):
        super().__init__(name, birthdate, sex)
        # ДОБАВИТЬ: атрибут employment_date
        self.position = position
        self.salary = salary

    # ДОБАВИТЬ: свойство annual_income

    def index_salary(self, CPI: float = 99.38) -> float:
        """Рассчитывает повышение оклада (Индексация Заработной Платы)"""
        # Индекс Потребительских Цен по Нижегородской области на август 2022
        # УДАЛИТЬ: хранить такой общий коэффициент в экземпляре сотрудника мне представляется не лучшей идеей — не довольно ли того, что вы его передаёте параметром? этот индекс ведь меняется от месяца к месяцу, если я правильно понимаю
        self.CPI = 99.38
        salary = self.salary
        # КОММЕНТАРИЙ: индексация на убывание? хорошо, что вы не в администрации работаете xD
        salary_increase = salary * CPI / 100
        # ДОБАВИТЬ: мне представляется, что возвращаемое значение этого метода будет перезаписывать атрибут зарплаты для сотрудников, а он у нас принимает int объекты — может стоит преобразовать?
        return salary_increase

    # ДОБАВИТЬ: метод __str__()


class GeneralPersonnel(Employee):
    pass


class SecurityPersonnel(Employee):
    def __str__(self):
        # ИСПРАВИТЬ: у вас эта строка частично дублируется во многих классах — этого надо стараться избегать
        # ИСПОЛЬЗОВАТЬ: пропишите доступную часть строки в методе __str__() базового класса Person, а затем в соответствующих методах подклассов вызывайте метод родительского класса — он вернёт строку, как и должен, а вы к этой строке добавите ещё одну часть:
        # return super().__str__() + f'заработная плата: {self.salary}'
        return f'Имя сотрудника: {self.name}; ' \
               f'дата рождения: {self.birthdate}; ' \
               f'пол: {self.sex}; ' \
               f'должность: {self.position}; ' \
               f'заработная плата: {self.salary}.'


class Administrator(Employee):
    def __init__(self,
                 # ДОБАВИТЬ: аннотации
                 name,
                 birthdate,
                 sex,
                 position,
                 salary,
                 # ИСПОЛЬЗОВАТЬ: когда нужно аннотировать объявляемый класс, то можно взять имя класса в кавычки, чтобы избежать ошибок
                 supervisor: 'Administrator',
                 subordinates: list[Employee]):
        super().__init__(name, birthdate, sex, position, salary)
        self.supervisor = supervisor
        # ИСПОЛЬЗОВАТЬ: значение по умолчанию для атрибута subordinates
        self.subordinates = subordinates

    # ИСПРАВИТЬ: дублирование кода
    def __str__(self):
        return f'Имя администратора: {self.name}; ' \
               f'дата рождения: {self.birthdate}; ' \
               f'пол: {self.sex}; ' \
               f'должность: {self.position}; ' \
               f'заработная плата: {self.salary};' \
               f'подчинённые {self.subordinates}.'


class ProfessionalEmployee(Employee):
    # ДОБАВИТЬ: аннотации и значение по умолчанию для параметра degree
    def __init__(self,
                 name,
                 birthdate,
                 sex,
                 position,
                 salary,
                 degree,
                 experience: int = 0):
        super().__init__(name, birthdate, sex, position, salary)
        self.degree = degree
        self.experience = experience

    def years_of_experience(self) -> int:
        # ИСПРАВИТЬ: предполагалось, что этот метод будет рассчитывать общий стаж сотрудника: тот, с которым он принят на работу (записан в атрибуте experience), плюс стаж в университете (с даты приёма по текущую дату)
        year_of_work = int(input('Введите текущий стаж работы сотрудника в организации: '))
        total_experience = self.experience + year_of_work
        return total_experience

    # ДОБАВИТЬ: метод __str__()


class Teacher(Employee):
    def __init__(self,
                 name: str,
                 birthdate: str,
                 sex: Sex,
                 position: str,
                 salary: int,
                 courses,
                 degree: Degree = Degree.MASTER,
                 professorship: bool = False,
                 experience: int = 0):
        super().__init__(name, birthdate, sex, position, salary)
        self.degree = degree
        self.professorship = professorship
        self.experience = experience

        self._courses = list(courses)

    # ИСПРАВИТЬ: а я бы сделал здесь только один геттер через свойство — также как с name в Person вы сделали
    def get_courses(self) -> list:
        """Возвращает приватный атрибут класса Teacher (getter)."""
        return self._courses

    def set_courses(self, courses: list):
        """Получает приватный атрибут класса Teacher (setter)."""
        self._courses = courses

    # ИСПРАВИТЬ: лучше здесь по-одному курсу добавлять
    def add_course(self, course: list):
        """Добавляет наименования курсов, которые может вести преподаватель."""
        self._courses.append(course)

    # ИСПРАВИТЬ: лучше здесь по-одному курсу добавлять
    def rem_course(self, course: list):
        """Удаляет наименования ранее созданных либо уже имеющихся курсов."""
        # ОТВЕТИТЬ: в чём разница между "ранее созданными" и "уже имеющимися"?

        self._courses.remove(course)

    # ДОБАВИТЬ: метод __str__()


class Researcher(Employee):
    def __init__(self,
                 name: str,
                 birthdate: str,
                 sex: Sex,
                 position: str,
                 salary: int,
                 degree: Degree = Degree.MASTER):
        super().__init__(name, birthdate, sex, position, salary)
        self.degree = degree

    # ИСПРАВИТЬ: дублирование кода
    def __str__(self):
        return f'Имя сотрудника: {self.name}; ' \
               f'дата рождения: {self.birthdate}; ' \
               f'пол: {self.sex}; ' \
               f'должность: {self.position}; ' \
               f'заработная плата: {self.salary}; ' \
               f'научная степень: {self.degree}'


class Student(Person):
    def __init__(self,
                 # ДОБАВИТЬ: аннотации типов
                 name,
                 birthdate,
                 sex,
                 year: int = 1,
                 average_grade: float = -1):
        super().__init__(name, birthdate, sex)
        # ДОБАВИТЬ: атрибут form
        self.year = year
        self.average_grade = average_grade

    # КОММЕНТАРИЙ: вот, собственно, поэтому я и говорил о необходимости добавить в модель дисциплины, которые можно связать со студентами и каждому студенту по каждой дисциплине выставлять баллы — а не вручную вводить название предмета и уж точно не обращаться к объектам в глобальном пространстве имён — я их сейчас перенёс из этого модуля (как это и должно было быть) и весь код этих двух методов превратился в тыкву; попытку, впрочем, засчитываю =)
    #  вспомните принцип инверсии зависимостей: код верхнего уровня и код нижнего уровня не должны зависеть друг от друга
    def average_grade(self) -> int:
        # УДАЛИТЬ: код метода — оставьте пока заглушку, после доработки модели допишем
        """Подсчитывает средний балл за введённую пользователем дисциплину и выводит соответствующие сообщения."""
        subject = input('Введите наименование предмета: ')
        # Проверка на наличие студента (его фамилии) в списке группы.
        if self.name not in list(group221.keys()):
            raise ValueError('Студент не найден.')
        # Проверка на наличие предмета в списке группы.
        if subject not in list(group221.values())[0]:
            raise ValueError('У студента нет такого предмета.')
        print(f'Student {self.name} has'
              f' {round(sum(group221[self.name][subject]) / len(group221[self.name][subject]), 2)} '
              f'average grade in {subject}.')
        return round(sum(group221[self.name][subject]) / len(group221[self.name][subject]), 2)

    def year_increment(self, year: int = 0, average_grade: int = 0) -> str:
        # УДАЛИТЬ: код метода — оставьте пока заглушку, после доработки модели допишем
        """Выводит пользователю сообщение о студенте: переведён, остается на текущем курсе на второй год или закончил обучение."""
        self.year = year
        self.average_grade = average_grade
        exam = input('Сдал ли данный студент экзамен? [Да/Нет]: ')
        avgr = s1.average_grade1()
        if year >= 4 and avgr > 2.51 and exam == 'Да':
            return 'Студент закончил обучение.'
        if exam == 'Да' and avgr > 2.51:
            return 'Студент переведён на следующий курс.'
        else:
            return 'Студент остаётся на второй год на текущем курсе.'


# ДОБАВИТЬ: классы OrganizationLevel, University, Institute, Department, Group


# ИТОГ: на самом деле довольно хорошо, но требует доработки — 7/10

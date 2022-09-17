from enum import Enum
import math


# Groups:
group221 = {'Rodov': {'math': [2, 5, 5, 5, 5, 3, 3],
                      'nature': [2, 4, 5, 3],
                      'rus': [2, 2, 2, 2]},
            'Stafeev': {'math': [2, 3, 3, 2, 2, 4, 3],
                        'nature': [3, 4, 5, 4],
                        'eng': [2, 3, 2, 2]}}

# any groups...


class Sex(Enum):
    MALE = 'm'
    FEMALE = 'f'


class Degree(Enum):
    BACHELOR = 'b'
    MASTER = 'm'
    DOCTOR = 'd'


class Person:
    def __init__(self, name: str,
                 birthdate: str,
                 sex: Sex):
        self.__name = name
        self.birthdate = birthdate
        self.sex = sex

    @property
    def name(self):
        return self.__name


class Employee(Person):
    def __init__(self,
                 name: str,
                 birthdate: str,
                 sex: Sex,
                 position: str,
                 salary: int):
        super().__init__(name, birthdate, sex)
        self.position = position
        self.salary = salary

    def index_salary(self, CPI: float = 99.38) -> float:
        """Расчитывает повышение оклада (Индексация Заработной Платы)"""
        self.CPI = 99.38  # Индекс Потребительских Цен по Нижегородской области на август 2022
        salary = self.salary
        salary_increase = salary * CPI / 100
        return salary_increase


class ProfessionalEmployee(Employee):
    def __init__(self, name, birthdate, sex, position, salary, degree, experience: int = 0):
        super().__init__(name, birthdate, sex, position, salary)
        self.degree = degree
        self.experience = experience

    def years_of_experience(self) -> int:
        year_of_work = int(input('Введите текущий стаж работы сотрудника в организации: '))
        total_experience = self.experience + year_of_work
        return total_experience


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

    def __str__(self):
        return f'Имя сотрудника: {self.name}; ' \
               f'дата рождения: {self.birthdate}; ' \
               f'пол: {self.sex}; ' \
               f'должность: {self.position}; ' \
               f'заработная плата: {self.salary}; ' \
               f'научная степень: {self.degree}'


class SecurityPersonnel(Employee):
    def __str__(self):
        return f'Имя сотрудника: {self.name}; ' \
               f'дата рождения: {self.birthdate}; ' \
               f'пол: {self.sex}; ' \
               f'должность: {self.position}; ' \
               f'заработная плата: {self.salary}.'


class Administrator(Employee):
    def __init__(self, name, birthdate, sex, position, salary, supervisor, subordinates: list):
        super().__init__(name, birthdate, sex, position, salary)
        self.supervisor = supervisor
        self.subordinates = subordinates

    def __str__(self):
        return f'Имя администратора: {self.name}; ' \
               f'дата рождения: {self.birthdate}; ' \
               f'пол: {self.sex}; ' \
               f'должность: {self.position}; ' \
               f'заработная плата: {self.salary};' \
               f'подчинённые {self.subordinates}.'


class Student(Person):
    def __init__(self, name, birthdate, sex, year: int = 1, average_grade: float = -1):
        super().__init__(name, birthdate, sex)
        self.year = year
        self.average_grade = average_grade

    def average_grade1(self) -> int:
        """Подсчитывает средний балл за введённую пользователем дисциплину и выводит соответсвующие сообщения."""
        subject = input('Введите наименование предмета: ')
        # Проверка на наличие студента(его фамилии) в списке группы.
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
        """Выводит пользователю сообщение о студенте: Переведён, остается на второй курс или закночил обучение."""
        self.year = year
        self.average_grade = average_grade
        exam = input('Сдал ли данный студент экзамен? (Введите: "Да" или "Нет"): ')
        avgr = s1.average_grade1()
        if year >= 4 and avgr > 2.51 and exam == 'Да': return 'Студент закончил обучение.'
        if exam == 'Да' and avgr > 2.51: return 'Студент переведён на следующий курс.'
        else: return 'Студент остаётся на второй курс'


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
        self.__courses = list(courses)

    def set_courses(self, courses: list):
        """Получает приватный атрибут класса Teacher (setter)."""
        self.__courses = courses

    def get_courses(self) -> list:
        """Возвращает приватный атрибут класса Teacher (getter)."""
        return self.__courses

    def add_course(self, course: list):
        """Добавляет наименования, преподаваемых учителем, курсов."""
        self.__courses.append(course)

    def rem_course(self, course: list):
        """Удаляет наименования ранее созданных либо уже имеющихся курсов."""
        self.__courses.remove(course)


t1 = Teacher('Nikolay', '07.08.1972', Sex.MALE, 'laboratory head', 50000, '')


class GeneralPersonnel(Employee):
    pass


# t1._Teacher__courses.append('Physics')
# print(t1._Teacher__courses)


t1.add_course('Microelectronic')


s1 = Student('Rodov', '21.12.98', Sex.MALE) # stdin: 'math' -> Student Rodov has 3.29 average grade in math.
s2 = Student('Stafeev', '30.12.98', Sex.MALE) # stdin: 'any_arg' -> ValueError: У студента нет такого предмета.
s3 = Student('Morozov', '29.12.97', Sex.MALE) # stdin: 'any_arg' or existing value (for example: 'math') -> ValueError:
# Студент не найден.

TOTAL_STUDENT = [s1.year_increment(3), s2.year_increment(4)]

#print(s1.year_increment(3))
#print(s2.year_increment())


p1 = Person('Ivan', '01.06.1980', Sex.MALE)
print(f'{p1.__dict__ = }\n')

e1 = Employee('Ivan', '01.06.1980', Sex.MALE, 'director', None)
print(f'{e1.__dict__ = }\n')

r1 = Researcher('Andrey', '07.08.1972', Sex.MALE, 'laboratory head', 50000, Degree.DOCTOR)
print(r1)
print(f'{r1.__dict__ = }\n')

g1 = GeneralPersonnel('Olga', '08.09.1949', Sex.FEMALE, 'clothkeeper', 10000)
print(f'{g1.__dict__ = }\n')

em1 = Employee('Roman', '19.02.2001', Sex.MALE, 'student', 45000)

PE = ProfessionalEmployee('Roman', '19.02.2001', Sex.MALE, 'student', 45000, Degree.BACHELOR, 12)

# print(f'Общий стаж работы данного сотрудника составляет: {PE.years_of_experience()}')

print(f'Индексация: {em1.index_salary()}')

t2 = Teacher('Roman', '19.02.2001', Sex.MALE, 'student', 45000, '')

t2.add_course('Technical Mechanic')
t2.add_course('Nature')
t2.add_course('Math')
t2.rem_course('Math')

print(f'Преподаватель {t1.name} преподаёт {t1.get_courses()}')
print(f'Преподаватель {t2.name} преподаёт {t2.get_courses()}, хотя как: он же студент :)')
# print(t1._Teacher__courses) -> Учебный пример. Больше ни разу в жизни такого не повторять :)(с)

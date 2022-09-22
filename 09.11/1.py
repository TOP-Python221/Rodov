"""Модель классов университета."""

from enum import Enum


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
        """Рассчитывает повышение оклада (Индексация Заработной Платы)"""
        # Индекс Потребительских Цен по Нижегородской области на август 2022
        self.CPI = 99.38
        salary = self.salary
        salary_increase = salary * CPI / 100
        return salary_increase


class GeneralPersonnel(Employee):
    pass


class SecurityPersonnel(Employee):
    def __str__(self):
        return f'Имя сотрудника: {self.name}; ' \
               f'дата рождения: {self.birthdate}; ' \
               f'пол: {self.sex}; ' \
               f'должность: {self.position}; ' \
               f'заработная плата: {self.salary}.'


class Administrator(Employee):
    def __init__(self,
                 name,
                 birthdate,
                 sex,
                 position,
                 salary,
                 supervisor: 'Administrator',
                 subordinates: list[Employee]):
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


class ProfessionalEmployee(Employee):
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
        year_of_work = int(input('Введите текущий стаж работы сотрудника в организации: '))
        total_experience = self.experience + year_of_work
        return total_experience


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

    def get_courses(self) -> list:
        """Возвращает приватный атрибут класса Teacher (getter)."""
        return self._courses

    def set_courses(self, courses: list):
        """Получает приватный атрибут класса Teacher (setter)."""
        self._courses = courses

    def add_course(self, course: list):
        """Добавляет наименования курсов, которые может вести преподаватель."""
        self._courses.append(course)

    def rem_course(self, course: list):
        """Удаляет наименования ранее созданных либо уже имеющихся курсов."""
        self._courses.remove(course)


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


class Student(Person):
    def __init__(self,
                 name,
                 birthdate,
                 sex,
                 year: int = 1,
                 average_grade: float = -1):
        super().__init__(name, birthdate, sex)
        self.year = year
        self.average_grade = average_grade

    def average_grade(self) -> int:
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

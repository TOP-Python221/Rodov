from random import randrange as rr

# КОММЕНТАРИЙ: странный выбор базового класса: класс int позволяет создавать одиночные числа, а матрица — это по определению контейнер с числами
class Matrix(int):
    # УДАЛИТЬ: параметр some_arg не используется
    def __init__(self, some_arg):
        # УДАЛИТЬ: атрибут some_arg не используется
        self.some_arg = some_arg
        # ИСПРАВИТЬ: хорошо, предположим, хранить каждый элемент матрицы отдельным атрибутом тоже можно — но как насчёт матриц различных размерностей? я сейчас вижу класс, с помощью которого можно создать только матрицу 1х3 — как-то бедновато, не находите?
        self.el_of_mat1 = rr(-10, 10)
        # КОММЕНТАРИЙ: следующий момент: сейчас все элементы матрицы инициализируются случайными значениями — это хороший вариант, если нужно быстро создать матрицу со случайными числами, нет проблем
        # ДОБАВИТЬ: но как насчёт куда более востребованной возможности инициализировать матрицу своими значениями?
        self.el_of_mat2 = rr(-10, 10)
        self.el_of_mat3 = rr(-10, 10)
        # ДОБАВИТЬ: для динамического создания атрибутов можно работать с внутренним словарём __dict__ объекта экземпляра

    # КОММЕНТАРИЙ: именно этот метод в первую очередь должен использоваться для возврата форматированной удобно читаемой строки — а вовсе не какой-то неочевидный для пользователя check()
    def __str__(self):
        return f'{self.el_of_mat1}' + ' ' + f'{self.el_of_mat2}' + ' ' + f'{self.el_of_mat3}'

    # ИСПРАВИТЬ: либо этот метод должен быть защищённым и использоваться методом __str__(), либо содержимое этого метода должно быть в методе __str__()
    def check(self) -> str:
        """Проверяет длину и наличие символа '-' в строке и выравнивает строку по правому краю."""
        # ИСПРАВИТЬ: может сравнение чисел использовать? или хотя бы конкатенацию строк? или множества? а когда у вас будет пара десятков или пара сотен элементов матрицы — как вы в них наличие знака минус проверять станете?
        if '-' in str(self.el_of_mat1) or '-' in str(self.el_of_mat2) or '-' in str(self.el_of_mat3):
            return str(self.el_of_mat1).rjust(3) \
                   + str(self.el_of_mat2).rjust(3) \
                   + str(self.el_of_mat3).rjust(3)
        # ИСПРАВИТЬ: смотрите карточку Логические выражения
        if len(str(self.el_of_mat1)) or len(str(self.el_of_mat2)) or len(str(self.el_of_mat3)) >= 3:
            return str(self.el_of_mat1).rjust(3) \
                   + str(self.el_of_mat2).rjust(3) \
                   + str(self.el_of_mat3).rjust(3)

    # КОММЕНТАРИЙ: эти методы должны реализовывать поэлементное сложение и вычитание двух матриц
    def __add__(self, other):
        # КОММЕНТАРИЙ: а не складывать два ноля с помощью метода базового класса
        res = super().__add__(other)
        # КОММЕНТАРИЙ: и не создавать новую случайную матрицу
        return Matrix(res)

    def __sub__(self, other):
        res = super().__sub__(other)
        return Matrix(res)
    # СДЕЛАТЬ: изучайте: https://thecode.media/matrix-101/ (вторая ссылка в Яндексе по запросу "поэлементное сложение матриц"...)


# экземпляры класса Matrix()
m1 = Matrix(1)
m2 = Matrix(1)
m3 = m2 + m1
m4 = m2 - m1

# УДАЛИТЬ: мы не должны явным образом использовать для вывода экземпляра матрицы дополнительные методы — есть метод __str__()
# print('m1:', m1.check())
# print('m2:', m2.check())
# print('m3:', m3.check())
# print('m4:', m4.check(), end='\n\n')

# КОММЕНТАРИЙ: метод __str__() может в своём коде использовать дополнительные скрытые методы, да, но с точки зрения того, кто использует класс, выполняется только метод __str__() — вот так:
print(m1)
print(m2)
print(m3)
print(m4, end='\n\n')


# ============= Черновые работы ================

# class Matrix:
      # КОММЕНТАРИЙ: параметры конструктора не используются
#     def __init__(self, el_of_mat1: int, el_of_mat2: int, el_of_mat3: int) -> int:
#         self.el_of_mat1 = rr(-100, 100)
#         self.el_of_mat2 = rr(-100, 100)
#         self.el_of_mat3 = rr(-100, 100)
#
#
#     def decValue(self, el_of_mat1, el_of_mat2, el_of_mat3):
#         self.el_of_mat1 = el_of_mat1
#         self.el_of_mat2 = el_of_mat2
#         self.el_of_mat3 = el_of_mat3
#
#     def __str__(self):
           # КОММЕНТАРИЙ: f-строки так не используются
#          return f'{self.el_of_mat1, self.el_of_mat2, self.el_of_mat3}'
#
#
# m1 = Matrix(1, 1, 1)
# m2 = Matrix(1, 1, 1)
# m3 = Matrix(1, 1, 1)
#
# print(m1)
# print(m2)
# print(m3)


# ========================== Second choice ====================================

# class Matrix(int):
#     def __init__(self, some_arg):
          # КОММЕНТАРИЙ: способ хранения элементов не изменился
#         self.some_arg = some_arg
#         self.el_of_mat1 = rr(-10, 10)
#         self.el_of_mat2 = rr(-10, 10)
#         self.el_of_mat3 = rr(-10, 10)
#
#     def __str__(self):
#         return f'{self.el_of_mat1}'+ ' ' + f'{self.el_of_mat2}' + ' ' + f'{self.el_of_mat3}'
#
#     def __add__(self, other):
#         res = super().__add__(other)
#         return Matrix(res)
#
      # КОММЕНТАРИЙ: изменился только этот метод
#     def check(self):
#         prefix = '-'
#         if not str(self.el_of_mat1).startswith(prefix):
#             return ' ' + str(self.el_of_mat1)
#         elif not str(self.el_of_mat2).startswith(prefix):
#             return ' ' + str(self.el_of_mat2)
#         elif not str(self.el_of_mat3).startswith(prefix):
#             return ' ' + str(self.el_of_mat3)
#
#     def __sub__(self, other):
#         res = super().__sub__(other)
#         return Matrix(res)


# КОММЕНТАРИЙ: самое главное — разных способов хранения элементов матрицы не увидел. можно создать атрибуты rows и columns, можно хранить всю матрицу в одном атрибуте в виде вложенного списка, или словаря, можно создать отдельный класс вектор (или ряд, или столбец) и использовать экземпляры этого класса в классе матрицы...


# ИТОГ: дорабатывать и дорабатывать — 4/12

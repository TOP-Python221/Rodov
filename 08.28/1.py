from random import randrange as rr

class Matrix(int):
    def __init__(self, some_arg):
        self.some_arg = some_arg
        self.el_of_mat1 = rr(-10, 10)
        self.el_of_mat2 = rr(-10, 10)
        self.el_of_mat3 = rr(-10, 10)

    def __str__(self):
        return f'{self.el_of_mat1}' + ' ' + f'{self.el_of_mat2}' + ' ' + f'{self.el_of_mat3}'

    def check(self) -> str:
        """Проверяет длину и наличие символа '-' в строке и выравнивает строку по правому краю."""
        if '-' in str(self.el_of_mat1) or '-' in str(self.el_of_mat2) or '-' in str(self.el_of_mat3):
            return str(self.el_of_mat1).rjust(3) \
                   + str(self.el_of_mat2).rjust(3) \
                   + str(self.el_of_mat3).rjust(3)

        if len(str(self.el_of_mat1)) or len(str(self.el_of_mat2)) or len(str(self.el_of_mat3)) >= 3:
            return str(self.el_of_mat1).rjust(3) \
                   + str(self.el_of_mat2).rjust(3) \
                   + str(self.el_of_mat3).rjust(3)

    def __add__(self, other):
        res = super().__add__(other)
        return Matrix(res)

    def __sub__(self, other):
        res = super().__sub__(other)
        return Matrix(res)


# экземпляры класса Matrix()
m1 = Matrix(1)
m2 = Matrix(1)
m3 = m2 + m1
m4 = m2 - m1

print('m1:', m1.check())
print('m2:', m2.check())
print('m3:', m3.check())
print('m4:', m4.check(), end='\n\n')

print(m1)
print(m2)
print(m3)
print(m4, end='\n\n')


# ============= Черновые работы ================

# class Matrix:
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

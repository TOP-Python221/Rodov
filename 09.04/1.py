from random import randrange as rr

# ДОБАВИТЬ: а где исключения?

class MatrixOne(int):
    def __init__(self, some_arg: int):
        self.some_arg = some_arg
        self.el_of_mat1 = rr(-10, 10)
        self.el_of_mat2 = rr(-10, 10)
        self.el_of_mat3 = rr(-10, 10)

    def __str__(self):
        return f'{self.el_of_mat1}'+ ' ' + f'{self.el_of_mat2}' + ' ' + f'{self.el_of_mat3}'

    def __add__(self, other: int):
        res = super().__add__(other)
        return MatrixOne(res)

    def check(self) -> str:
        '''Проверяет длину и наличие символа <-> в строке и выравнивает строку по правому краю.'''
        if '-' in str(self.el_of_mat1) or '-' in str(self.el_of_mat2) or '-' in str(self.el_of_mat3):
            return str(self.el_of_mat1).rjust(3) + str(self.el_of_mat2).rjust(3) + str(self.el_of_mat3).rjust(3)
        if len(str(self.el_of_mat1)) or len(str(self.el_of_mat2)) or len(str(self.el_of_mat3)) >= 3:
            return str(self.el_of_mat1).rjust(3) + str(self.el_of_mat2).rjust(3) + str(self.el_of_mat3).rjust(3)

    def __sub__(self, other: int):
        res = super().__sub__(other)
        return MatrixOne(res)

#Экземпляры класса Matrix()
m1 = MatrixOne(1)
m2 = MatrixOne(1)
m3 = m2 + m1
m4 = m2 - m1

print(m1.check())
print(m2.check())
print(m3.check())
print(m4.check(), end = '\n\n')

class MatrixTwo(MatrixOne):
    pass

matrix1 = MatrixTwo(1)
matrix2 = MatrixTwo(1)
matrix3 = matrix1 + matrix2
matrix4 = matrix1 - matrix2

print(matrix1.check())
print(matrix2.check())
print(matrix3.check())
# print(matrix4.check())


# ИТОГ: не готово к проверке — 0/12
# КОММЕНТАРИЙ: когда допишете — удалите комментарий с меткой ИТОГ

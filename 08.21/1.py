
class Tetra:
    def __init__(self, x: int, y: int, edge: int = 10,):
        self.edge = edge
        self.x = x
        self.y = y

    def __sub__(self, other) -> float:
        if isinstance(other, Tetra):
            first_point = other.x - self.x
            second_point = other.y - self.y
            return round((first_point**2 + second_point**2)**0.5, 2)
        else:
            raise TypeError('other object isn`t Tetra')

    # ДОДЕЛАТЬ,:
    def surface(self, edge):
        pass

    def volume(self) -> float:
        """Рассчитывает объём тетраэдра."""
        return str(round((self.edge ** 3 / 12) ** 0.5, 2))

    # def ....

    def __lt__(self, other):
        if isinstance(other, Tetra):
            if self.volume() < other.volume():
                return True
            else:
                return False
        else:
            raise TypeError('other object isn`t Tetra. Look at the code a little bit better and try again :p')

# экземпляры класса Tetra
tetra1 = Tetra(3, 4, 12)
tetra2 = Tetra(3, 4, 15)

print(f'Объём первого тетраэдра: {tetra1.volume()}')
print(f'Объём второго тетраэдра: {tetra2.volume()}')


# ---------------- Черновые варианты: ----------------

# print(f'Объём первого тетраэдра { = }')
# print(f'Объём второго тетраэдр {= }')
#
# class Tetra:
#     ef __init__(self, edge: int = 10 ) -> float:
#         self.edge = edge
#
#     def volume(self, tetra1, tetra2):
#         self.tetra1 = tetra1
#         self.tetra2 = tetra2
#         self.Vtetra1 = str(round((self.tetra1 ** 3 / 12) * 1.41, 2))
#         self.Vtetra2 = str(round((self.tetra2 ** 3 / 12) * 1.41, 2))
#         return volume
#
#
# = str(round((tetra1 ** 3 / 12) * 1.41, 2))
# tetra1 = Tetra(12)
# tetra2 = Tetra(15)
#
# tetra2 = 12
# etra1 = 15
#
# print(tetra1.volume())
# volume1 = round((tetra1 ** 3 / 12) * 1.41, 2)
# volume2 = round((tetra2 ** 3 / 12) * 1.41, 2)

class Tetra:
    def __init__(self, x: int, y: int, edge: int = 10):
        self.edge = edge
        # КОММЕНТАРИЙ: тетраэдр — объёмная фигура, задавать его точкой на плоскости как-то.. мм.. и, кстати, если уж на то пошло, вершин у тетраэдра четыре — но здесь надо аккуратно: вам надо тогда, чтобы расстояние между вершинами было равно длине ребра — вопрос по сути сводится к тому, что через что вы задаёте — вершины из которых вычисляется ребро, или точку и ребро из которых вычисляются остальные вершины
        self.x = x
        self.y = y

    # КОММЕНТАРИЙ: для класса точки мы операцию вычитания переопределили как вычисление расстояния между точками — и это не самый очевидный ход, но допустимый
    # ОТВЕТИТЬ: а вот как вычитание объектов тетраэдров сводится к тому же действию?
    def __sub__(self, other) -> float:
        if isinstance(other, Tetra):
            first_point = other.x - self.x
            second_point = other.y - self.y
            return round((first_point**2 + second_point**2)**0.5, 2)
        else:
            raise TypeError('other object isn`t Tetra')

    # КОММЕНТАРИЙ: метки в верхнем регистре — моя прерогатива )) если сильно надо, то используйте тогда, пожалуйста, хотя бы базовые todo и fixme
    # ДОДЕЛАТЬ,:
    # УДАЛИТЬ: параметр edge здесь не нужен — он уже есть в self в качестве атрибута
    def surface(self, edge):
        # ДОБАВИТЬ: тело метода
        pass

    # ИСПРАВИТЬ: в аннотации float, а возвращаете str — надо выбрать одно
    def volume(self) -> float:
        """Рассчитывает объём тетраэдра."""
        return str(round((self.edge**3 / 12)**0.5, 2))

    # КОММЕНТАРИЙ: а вот добавление сравнения — это очень хорошо!
    def __lt__(self, other):
        if isinstance(other, Tetra):
            if self.volume() < other.volume():
                return True
            else:
                return False
        else:
            # КОММЕНТАРИЙ: не стоит предлагать смотреть на код, лучше напишите документацию к классу =Ъ
            raise TypeError('other object isn`t Tetra. Look at the code a little bit better and try again :p')


# экземпляры класса Tetra
tetra1 = Tetra(3, 4, 12)
tetra2 = Tetra(3, 4, 15)

print(f'Объём первого тетраэдра: {tetra1.volume()}')
print(f'Объём второго тетраэдра: {tetra2.volume()}')


# ИТОГ: хорошо! — 4/5

from abc import ABC, abstractmethod


# ДОБАВИТЬ: всем методам, кроме встроенных, аннотации типов возвращаемых значений


class Dishes(ABC):
    """Базовый класс <<Блюда>>"""
    def __init__(self, name: str, description: str, cost: float, *ingredients: str):
        self.cost = cost
        self.ingredients = ingredients
        self.description = description
        self.name = name

    @abstractmethod
    def create(self): pass

    @abstractmethod
    def describe(self): pass


class Snack(Dishes):
    """Конкретный класс <<Закуска>>"""
    def create(self):
        return f'We cooked {self.name}. It has {self.ingredients} ingredients and costs {self.cost}'

    def describe(self):
        return f'{self.name} {self.description}'


class MainDish(Dishes):
    """Конкретный класс <<Главное блюдо>>"""
    def create(self):
        return f'We cooked {self.name}. It has {self.ingredients} ingredients and costs {self.cost}'

    def describe(self):
        return f'{self.name} {self.description}'


class SecondDish(Dishes):
    """Конкретный класс <<Второе блюдо>>"""
    def create(self):
        return f'We cooked {self.name}. It has {self.ingredients} ingredients and costs {self.cost}'

    def describe(self):
        return f'{self.name} {self.description}'


class RussianSnack(Snack):
    """Расширенный класс <<Закуска>> из русской кухни"""
    def __init__(self):
        # 1ing and etc — количество каких-то ингредиентов для какого-то блюда
        super().__init__('Any Russian Snack', 'some describe of ', 130.00, '1ing', '3ing', '2ing')

    def describe(self):
        return f'{self.description}Russian Snack'


class RussianMain(MainDish):
    """Расширенный класс <<Главное блюдо>> из русской кухни"""
    def __init__(self):
        super().__init__('Any Russian Main Dish', 'some desc', 228.00, '1ing', '3ing', '2ing', '8ing', '1ing')

    def describe(self):
        return f'{self.description}Russian Main Dish'


class RussianSecond(SecondDish):
    """Расширенный класс <<Второе блюдо>> из русской кухни"""
    def __init__(self):
        super().__init__('Any Russian Second Dish', 'some desc', 390.00, '1ing', '2ing')

    def describe(self):
        return f'{self.description}Russian Second Dish'


class AsianSnack(Snack):
    def __init__(self):
        super().__init__('Any Asian Snack', 'some desc', 275.00, '1ing', '2ing')

    def describe(self):
        return f'{self.description}Asian Snack'


class AsianMain(MainDish):
    def __init__(self):
        super().__init__('Any Asian Main Dish', 'some desc', 1100.00, '1ing', '2ing')

    def describe(self):
        return f'{self.description}Asian Main Dish'


class AsianSecond(SecondDish):
    def __init__(self):
        super().__init__('Any Asian Second Dish', 'some desc', 890.00, '1ing', '2ing')

    def describe(self):
        return f'{self.description}Asian Second Dish'


class Factory(ABC):
    @abstractmethod
    def create_snack(self):
        pass

    @abstractmethod
    def get_main(self):
        pass

    @abstractmethod
    def get_second(self):
        pass


class RussianFactory(Factory):
    """Реализация абстрактной фабрики от <<Русской кухни>>"""
    def create_snack(self):
        return RussianSnack().create()

    def describe_snack(self):
        return RussianSnack().describe()

    def get_main(self):
        return RussianMain()

    def get_second(self):
        return RussianSecond()


class AsianFactory(Factory):
    """Реализация абстрактной фабрики от <<Азиатской кухни.>>"""
    def create_snack(self):
        return AsianSnack().create()

    def describe_snack(self):
        return AsianSnack().describe()

    def get_main(self):
        return AsianMain()

    def get_second(self):
        return AsianSecond()


# КОММЕНТАРИЙ: судя по количеству объектов, вызывающих другие объекты, которые вызывают третьи объекты — идеями абстракции вы прониклись =)

rf = RussianFactory()
af = AsianFactory()

print(rf.create_snack())
print(rf.describe_snack())
print()
print(af.create_snack())
print(af.describe_snack())

# ДОБАВИТЬ: напомню, что по условию задачи вам необходимо было получить от пользователя строку с названием кухни — и сгенерировать набор блюд соответствующей кухни — это можно сделать на тривиальных if...elif, что впрочем не лучший вариант, можно вручную составить словарь с нужными фабриками, можно проинспектировать код модуля, найдя подходящие объекты классов (фабрик) и поместив их в тот же словарь или перечислитель, можно вычислить eval() строку сразу в нужный объект класса... как видите способов много — как и всегда =)


# ИТОГ: доработать — 4/6


# СДЕЛАТЬ: первую задачу на шаблон Фабрика

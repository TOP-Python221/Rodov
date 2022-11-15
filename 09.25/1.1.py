class ClassBuilder:
    indent_size = 4
    # ОТВЕТИТЬ: это атрибут для флага или для контейнера? атрибут назван и по существу используется как флаг (логическая переменная), но при этом является списком — это как-то мало смысла для меня имеет
    # КОММЕНТАРИЙ: если имя переменной для контейнера описывает не сам контейнер, а его элементы, то оно почти всегда должно быть во множественном числе — иначе, это введение в заблуждение
    exist_class = []

    # ДОБАВИТЬ: аннотацию типа параметра class_name
    def __init__(self, class_name):
        self.class_name = class_name

    # ДОБАВИТЬ: аннотации типов параметров field_name и value и типа возвращаемого значения
    # КОММЕНТАРИЙ: как быть, если необходимо в один вызов метода передать в value число, а в другой — строку? (см. комментарий к выводу)
    def add_field(self, field_name=None, value=''):
        # ИСПРАВИТЬ здесь и далее: явного употребления имени класса лучше избегать: из-за этого будут возникать проблемы в сложных моделях, использующих наследование — а атрибуты класса можно вызывать и от self
        if field_name and not ClassBuilder.exist_class:
            # ИСПРАВИТЬ: задачей методов, работающих со строками, почти всегда является формирование строки, а не вывод в стандартный поток — дальнейшее использование этой строки является задачей кода верхнего уровня, использующего класс, а не самого класса — а вы здесь ограничили себя тем, что не сможете использовать строку с генерируемым кодом
            # ИСПРАВИТЬ: ключевое слово class пишется целиком в нижнем регистре
            print(f'Class {self.class_name}:')
            ClassBuilder.exist_class.append(self.class_name)
            # ДОБАВИТЬ: у метода конструктора __init__(), в котором происходит работа с объектом экземпляра, должен быть заголовок
            # ИСПРАВИТЬ: во время подстановки value в строку, мы должны учитывать тип объекта и при необходимости добавлять синтаксические символы, например кавычки для строки
            print(f"{' ' * ClassBuilder.indent_size}self.{field_name} = {value}")
        elif field_name and ClassBuilder.exist_class:
            # КОММЕНТАРИЙ: мне представляется намного более удобным в этом методе добавлять пары field_name и value в отдельный атрибут экземпляра — затем добавить метод __str__(), в котором, исходя из значений атрибутов, формировать и возвращать нужную строку
            print(f"{' ' * ClassBuilder.indent_size}self.{field_name} = {value}")
        else:
            print(f'Class {self.class_name}:')
            # ОТВЕТИТЬ: какую цель вы преследуете, возвращая из этого метода возвращаемое значение встроенной функции print()?
            return print(' ' * ClassBuilder.indent_size + 'pass')
        return self


cb = ClassBuilder('Person').add_field()


# -------------------------------------------------------------------------------------
# cb = ClassBuilder('Person').add_field()
# stdout:
#     Class Person:
#         pass
# -------------------------------------------------------------------------------------
# cb = ClassBuilder('Person').add_field('name', 'Andrey').add_field('age', 0)
# stdout:
#     Class Person:
          # КОММЕНТАРИЙ: если такой код передать интерпретатору, то без кавычек интерпретатор будет воспринимать Andrey как переменную
#         self.name = Andrey
#         self.age = 0
# -------------------------------------------------------------------------------------


# ИТОГ: код необходимо серьёзно переработать — 2/6


# СДЕЛАТЬ: остальные задачи на шаблон Строитель

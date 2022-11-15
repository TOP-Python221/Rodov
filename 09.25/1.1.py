class ClassBuilder:
    indent_size = 4
    # ОТВЕТИТЬ: это атрибут для флага или для контейнера? атрибут назван и по существу используется как флаг (логическая переменная), но при этом является списком — это как-то мало смысла для меня имеет
    # КОММЕНТАРИЙ: если имя переменной для контейнера описывает не сам контейнер, а его элементы, то оно почти всегда должно быть во множественном числе — иначе, это введение в заблуждение
    exist_class = []

    def __init__(self, class_name):
        self.class_name = class_name

    def add_field(self, field_name=None, value=''):
        if field_name and not ClassBuilder.exist_class:
            print(f'Class {self.class_name}:')
            ClassBuilder.exist_class.append(self.class_name)
            print(f"{' ' * ClassBuilder.indent_size}self.{field_name} = {value}")
        elif field_name and ClassBuilder.exist_class:
            print(f"{' ' * ClassBuilder.indent_size}self.{field_name} = {value}")
        else:
            print(f'Class {self.class_name}:')
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
#         self.name = Andrey
#         self.age = 0
# -------------------------------------------------------------------------------------

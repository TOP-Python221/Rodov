import importlib.util
import sys

from pathlib import Path

module_path = Path(sys.path[0]) / '1.py'
module_name = 'university_class_model'

spec = importlib.util.spec_from_file_location(module_name, module_path)
ucm = importlib.util.module_from_spec(spec)
sys.modules[module_name] = ucm
spec.loader.exec_module(ucm)

# print(ucm.__name__)
# print(ucm.__doc__)


# Немного не понял, как с этим работать. Постараюсь разобраться чуть позже. :D


# Groups:
group221 = {'Rodov': {'math': [2, 5, 5, 5, 5, 3, 3],
                      'nature': [2, 4, 5, 3],
                      'rus': [2, 2, 2, 2]},
            'Stafeev': {'math': [2, 3, 3, 2, 2, 4, 3],
                        'nature': [3, 4, 5, 4],
                        'eng': [2, 3, 2, 2]}}


t1 = ucm.Teacher('Nikolay', '07.08.1972', ucm.Sex.MALE, 'laboratory head', 50000, '')
t1.add_course('Microelectronic')

s1 = ucm.Student('Rodov', '21.12.98', ucm.Sex.MALE)
s2 = ucm.Student('Stafeev', '30.12.98', ucm.Sex.MALE)
s3 = ucm.Student('Morozov', '29.12.97', ucm.Sex.MALE)

p1 = ucm.Person('Ivan', '01.06.1980', ucm.Sex.MALE)
e1 = ucm.Employee('Ivan', '01.06.1980', ucm.Sex.MALE, 'director', None)
r1 = ucm.Researcher('Andrey', '07.08.1972', ucm.Sex.MALE, 'laboratory head', 50000, ucm.Degree.DOCTOR)

g1 = ucm.GeneralPersonnel('Olga', '08.09.1949', ucm.Sex.FEMALE, 'clothkeeper', 10000)

em1 = ucm.Employee('Roman', '19.02.2001', ucm.Sex.MALE, 'student', 45000)

PE = ucm.ProfessionalEmployee('Roman', '19.02.2001', ucm.Sex.MALE, 'student', 45000, ucm.Degree.BACHELOR, 12)

t2 = ucm.Teacher('Roman', '19.02.2001', ucm.Sex.MALE, 'student', 45000, '')

t2.add_course('Technical Mechanic')
t2.add_course('Nature')
t2.add_course('Math')
t2.rem_course('Math')

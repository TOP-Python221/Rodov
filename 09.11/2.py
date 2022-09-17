import importlib.util
import sys

from pathlib import Path

module_path = Path(sys.path[0]) / '1.py'
module_name = 'class_model'

spec = importlib.util.spec_from_file_location(module_name, module_path)
model = importlib.util.module_from_spec(spec)
sys.modules[module_name] = model
spec.loader.exec_module(model)

print(model.__name__)
print(model.__doc__)


TestClass = module_name.r1__dict__

test = TestClass()
print(f'\n{test = }\n')
test.hello()

# Немного не понял, как с этим работать. Постараюсь разобраться чуть позже. :D

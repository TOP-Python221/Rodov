from pathlib import Path
from random import shuffle

source = Path(r"d:\G-Doc\YandexDisk\Job\Компьютерная академия Шаг\Python web\221\homework\07.03\data.csv")
output = Path(r"d:\G-Doc\YandexDisk\Job\Компьютерная академия Шаг\Python web\221\homework\07.03\buffer.txt")

with open(source) as fh_in:
    data = fh_in.read()

data = data.split()[1:]

data_striped = []
for line in data:
    columns = line.split(';')
    for j in (0, 3, 4, 6, 7):
        data_striped += [columns[j]]

shuffle(data_striped)
data_shuffled = ';'.join(data_striped)

with open(output, 'w') as fh_out:
    fh_out.write(data_shuffled)

from __future__ import annotations

from dataclasses import dataclass

import os

if os.name == 'nt':
    PATH_SEP = '\\'
else:
    PATH_SEP = '/'


@dataclass
class File:
    """Файл в файловой системе."""
    name: str
    dir: str

    def __init__(self):
        self.dir_path = None

    @property
    def extension(self) -> str:
        return self.name.rsplit('.', 1)[-1][1:]

    def ls(self) -> str:
        return self.dir_path + PATH_SEP + self.name


class Folder(File):
    """Каталог в файловой системе. Может содержать вложенные каталоги и файлы."""
    def __init__(self, dir_path: str, name):
        self.name = name
        self.dir_path = dir_path
        self.elements: list[File] = []

    def add_files(self, element):
        self.elements += element
        return self.elements

    def check(self):
        pass


def ls(*objects: File | Folder) -> str:
    for obj in objects:
        print(obj.ls())


file = File()
fold = Folder('true', 'class')

ls(fold)
ls(file)


#Так и не разобрался :`(
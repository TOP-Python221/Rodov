
from collections.abc import Sequence
from json import load as jload
from mysql.connector import connect, Error as MySQLError
from pathlib import Path
from sys import path

# Переменная, содержащая список доступных sql-запросов.
CHECK_LIST = ['INSERT', 'insert',
              'UPDATE', 'update',
              'DELETE', 'delete']


class PersistenceManager:
    """
    Предоставляет методы для взаимодействия с БД.
    """
    default_dbconfig_path: Path | str = Path(path[0]) / 'db.json'
    default_stdout: bool = True

    @classmethod
    def _dbconfig_read(cls, dbconfig_path: Path | str = None):
        if dbconfig_path is None:
            dbconfig_path = cls.default_dbconfig_path
        with open(dbconfig_path, encoding='utf-8') as filein:
            return jload(filein)

    def __init__(self,
                 dbname: str = None,
                 dbconfig_path: Path | str = None,
                 autocommit: bool = True):
        try:
            self.connection = connect(
                **self._dbconfig_read(dbconfig_path),
                database=dbname
            )
            self.connection.autocommit = autocommit
        except MySQLError as err:
            if self.default_stdout:
                print(f'Connection failed: {err}')
        else:
            if self.default_stdout:
                print(f'Connection established')

    def select(self, query: str) -> Sequence[tuple]:
        """Возвращает данные, полученные при выполнении запроса выборки."""
        with self.connection.cursor() as cursor:
            cursor.execute(query)
            return cursor.fetchall()

    def insert(self, insert_query: str):
        """Добавляет данные в таблицу. Данный запрос должен начинаться с ключевого слова `INSERT/insert`"""
        with self.connection.cursor() as cursor:
            if insert_query.split(' ')[0] not in CHECK_LIST:
                raise ValueError('Данный запрос должен начинаться с ключевого слова `INSERT/insert`. Проверьте '
                                 'правильность '
                                 'ввода данных.')
            else:
                cursor.execute(insert_query)
                print('INSERT запрос успешно выполнен.')

    def update(self, update_query: str):
        """Обновляет данные в таблице. Данный запрос должен начинаться с ключевого слова `UPDATE/update`"""
        with self.connection.cursor() as cursor:
            if update_query.split(' ')[0] not in CHECK_LIST:
                raise ValueError('Данный запрос должен начинаться с ключевого слова `UPDATE/update`. Проверьте '
                                 'правильность '
                                 'ввода данных.')
            else:
                cursor.execute(update_query)
                print('UPDATE запрос успешно выполненен.')

    def delete(self, delete_query):
        with self.connection.cursor() as cursor:
            if delete_query.split(' ')[0] not in CHECK_LIST:
                raise ValueError('Данный запрос должен начинаться с ключевого слова `DELETE/delete`. Проверьте '
                                 'правильность '
                                 'ввода данных.')
            else:
                cursor.execute(delete_query)
                print('DELETE запрос успешно выполненен.')

    def set_foreign_key(self, foreign_keys: bool = True):
        '''Добавляет возможность смены внешнего ключа.'''
        with self.connection.cursor() as cursor:
            cursor.execute(f"SET FOREIGN_KEY_CHECKS = {foreign_keys};")
            if foreign_keys:
                print('Внешний ключ установлен.')
            else:
                print('Внешний ключ отсутствует.')

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.close()

    def __del__(self):
        self.connection.close()


if __name__ == '__main__':
    pm = PersistenceManager('world')
    pm.set_foreign_key(False)
    # pm.insert("INSERT INTO `city` (`Name`, `District`, `Population`) "
    #           "VALUES ('DisneyLand', 'MainDistrict', '123');")
    # pm.update("update `city` set `population` = 150 where `name` = 'DisneyLand';")
    pm.delete("DELETE FROM `city` WHERE `ID` > 4113;")

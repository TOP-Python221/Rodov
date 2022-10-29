from random import randrange as rr, choice as ch
from string import ascii_lowercase as alc
from abc import ABC, abstractmethod


class TestCase:
    history = []

    def __init__(self):
        self.messages = [
            ''.join(ch(alc) for _ in range(rr(3, 6)))
            for _ in range(1000)
        ]
        self.numbers = [
            (rr(10, 100) for _ in range(rr(4, 7)))
            for _ in range(1000)
        ]
        # ... другие поля?

    def print_msg(self):
        msg = self.messages.pop()
        return msg

    def sum_nums(self):
        nums = self.numbers.pop()
        return sum(nums)

    # ... другие методы?


class TestCaseCommand:
    """Класс <<Команда>>"""
    def __init__(self, test: TestCase):
        self.tester = test

    def saves(self) -> list:
        TestCase.history.append(self.tester.print_msg())
        return TestCase.history

    def remove(self) -> list:
        TestCase.history.pop(-1)
        return TestCase.history


test1 = TestCase()
some_test = TestCaseCommand(test1)
print(some_test.saves())
print(some_test.saves())
print(some_test.saves())
print(some_test.remove())



#----------------------First_Try------------------------------
# class Command(ABC):
#     @abstractmethod
#     def save(self):
#         pass
#
#     @abstractmethod
#     def remove(self):
#         pass
#
#
#    # @abstractmethod
#     #def redo(self):
#         #pass
#
#
# class PrintCommand(Command):
#     def __init__(self, test: TestCase):
#         self.command = []
#         self.tester = test
#
#     def save(self):
#         self.command += self.tester
#         return self.command
#
#     def remove(self):
#         """Отменяет последнюю команду в списке"""
#         self.command.remove(self.tester)
#
#
# class SumCommand(Command):
#     pass
#
#
# class Print:
#     def make_print(self):
#         print(f'Я что-то напечатал')
#
#
# class Invoker:
#     def __init__(self, command):
#         self.command = command
#
#     def set_command(self, command):
#         self.command = command
#
#     def invoke_remove(self):
#         self.command.remove()
#
#     def invoke_save(self):
#         self.command().save()
#
#
# test = TestCase()
# command_pr = PrintCommand(test.print_msg())
# invoker = Invoker(command_pr)
# invoker.invoke_save()
# invoker.set_command(PrintCommand)
# invoker.invoke_save()

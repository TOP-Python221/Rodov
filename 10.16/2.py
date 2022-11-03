from  enum import Enum
from abc import ABC, abstractmethod
from typing import List


class Parameter(Enum):
    INFORMATIONAL = 1
    SUCCESS = 2
    REDIRECTION = 3
    CLIENT_ERROR = 4
    SERVER_ERROR = 5


class Request:
    def __init__(self, description: List[str], req_type: Parameter):
        self.__description = description
        self.__req_type = req_type

    @property
    def req_type(self):
        return self.__req_type

    @property
    def description(self):
        return self.__description


class CodeHandler(ABC):

    def __init__(self, successor: None):
        self.__successor = successor

    def handle(self, request: Request) -> None:
        res = self._check_request(request.req_type)
        if not res and self.__successor:
            self.__successor.handle(request)

    @property
    def successor(self):
        return self.__successor

    @successor.setter
    def successor(self, successor: None):
        self.__successor = successor

    @abstractmethod
    def _check_request(self, request_type: Parameter):
        pass


class Code100(CodeHandler):
    def __init__(self, successor: CodeHandler = None):
        super().__init__(successor)

    def _check_request(self, request_type: Parameter) -> bool:
        check = request_type in (Parameter.INFORMATIONAL,
                                 Parameter.SUCCESS,
                                 Parameter.REDIRECTION,
                                 Parameter.CLIENT_ERROR,
                                 Parameter.SERVER_ERROR)
        if check:
            print('Ошибка 100-199 имеет <<информационный>> характер')
        return check


class Code200(CodeHandler):
    def __init__(self, successor: CodeHandler = None):
        super().__init__(successor)

    def _check_request(self, request_type: Parameter) -> bool:
        check = request_type in (Parameter.SUCCESS,
                                 Parameter.REDIRECTION,
                                 Parameter.CLIENT_ERROR,
                                 Parameter.SERVER_ERROR)
        if check:
            print('Ошибка 200-299 имеет <<успешный>> характер')
        return check


class Code300(CodeHandler):
    def __init__(self, successor: CodeHandler = None):
        super().__init__(successor)

    def _check_request(self, request_type: Parameter) -> bool:
        check = request_type in (Parameter.REDIRECTION,
                                 Parameter.CLIENT_ERROR,
                                 Parameter.SERVER_ERROR)
        if check:
            print('Ошибка 300-399 имеет <<перенаправленный>> характер')
        return check


class Code400(CodeHandler):
    def __init__(self, successor: CodeHandler = None):
        super().__init__(successor)

    def _check_request(self, request_type: Parameter) -> bool:
        check = request_type in (Parameter.CLIENT_ERROR,
                                 Parameter.SERVER_ERROR)
        if check:
            print('Ошибка 400-499 имеет <<клиенто-ошибочный>> характер')
        return check


class Code500(CodeHandler):
    pass


name1 = Code100()
name2 = Code200(name1)
name3 = Code300(name2)
name4 = Code400(name3)
name4.successor = name3
def request_handler(request: Request):
    name4.handle(request)

req_list = ['100', '101', '104']
request = Request(req_list, Parameter.INFORMATIONAL)
request_handler(request)

req_list = ['200', '202', '206']
request = Request(req_list, Parameter.SUCCESS)
request_handler(request)

req_list = ['300', '303', '309']
request = Request(req_list, Parameter.REDIRECTION)
request_handler(request)

req_list = ['400', '403', '409']
request = Request(req_list, Parameter.CLIENT_ERROR)
request_handler(request)


#








#==========================First_Try===============================
# class Handlers(list):
#     def __call__(self, *args, **kwargs):
#         for handler in self:
#             handler(*args, **kwargs)
#
#
# class Query:
#     def __init__(self, parameter: Parameter):
#         self.parameter = parameter
#
#
# class WebServer:
#     def __init__(self):
#         self.handlers = Handlers()
#
#     def perform_query(self, sender: 'Code', query: Query):
#         self.handlers(sender, query)
#
#
# class Code_100:
#     def __init__(self, server: WebServer):
#         self.server = server
#
#     @property
#     def stdin_code(self, value):
#         self.value = input('Введите код ошибки: ')
#         if self.value ==
#         return
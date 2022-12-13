# -*- coding: utf-8 -*-
class NameStr:

    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        setattr(instance, self.name, value)


class Person:

    first_name = NameStr()
    second_name = NameStr()
    patronymic = NameStr()

    def __init__(self, first_name: str, second_name: str, patronymic: str = ""):
        self.first_name = first_name
        self.second_name = second_name
        self.patronymic = patronymic

# -*- coding: utf-8 -*-
class Person:

    def __init__(self, first_name: str, second_name: str,
                 patronymic: str = ""):
        self._first_name = first_name
        self._second_name = second_name
        self._patronymic = patronymic

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        self._first_name = first_name

    @property
    def second_name(self):
        return self._second_name

    @second_name.setter
    def second_name(self, second_name):
        self._second_name = second_name

    @property
    def patronymic(self):
        return self._patronymic

    @patronymic.setter
    def patronymic(self, patronymic):
        self._patronymic = patronymic

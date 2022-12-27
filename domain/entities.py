# -*- coding: utf-8 -*-
from dataclasses import dataclass


class Person:

    def __init__(self, first_name: str,
                 second_name: str, patronymic: str):
        self._first_name = first_name
        self._second_name = second_name
        self._patronymic = patronymic

    @property
    def first_name(self) -> str:
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        self._first_name = first_name

    @property
    def second_name(self) -> str:
        return self._second_name

    @second_name.setter
    def second_name(self, second_name):
        self._second_name = second_name

    @property
    def patronymic(self) -> str:
        return self._patronymic

    @patronymic.setter
    def patronymic(self, patronymic):
        self._patronymic = patronymic


@dataclass
class Position:
    division: str = None
    subdivision: str = None
    post: str = None


@dataclass
class Contacts:
    phone: str = None
    mobile: str = None
    fax: str = None
    internal: str = None
    email: str = None
    address: str = None

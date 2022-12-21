# -*- coding: utf-8 -*-
from domain.person import Person


class PhoneBookEntry:

    def __init__(self, person: Person, number: str):
        self._person = person
        self._number = number

    @property
    def person(self):
        return self._person

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, number: str):
        self._number = number

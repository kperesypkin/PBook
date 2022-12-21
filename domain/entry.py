# -*- coding: utf-8 -*-
from domain.person import Person


class PhoneBookEntry:

    def __init__(self, person: Person, number: int):
        self._person = person
        self._number = number

    @property
    def person(self):
        return self._person

    @person.setter
    def person(self):
        pass

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, number: int):
        self._number = number

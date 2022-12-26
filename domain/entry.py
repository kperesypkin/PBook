# -*- coding: utf-8 -*-
from domain.employee import Employee


class PBookEntry:

    def __init__(self, employee: Employee, number: str):
        self._employee = employee
        self._number = number

    @property
    def employee(self):
        return self._employee

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, number: str):
        self._number = number

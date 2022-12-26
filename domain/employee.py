# -*- coding: utf-8 -*-
from dataclasses import dataclass


@dataclass
class Employee:

    first_name: str
    second_name: str
    patronymic: str
    department: str
    subdepartment: str
    post: str
    rank: str

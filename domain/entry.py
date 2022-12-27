# -*- coding: utf-8 -*-
from domain.entities import Contacts
from domain.entities import Person
from domain.entities import Position


class PBookEntry:

    def __init__(self, person: Person, position: Position,
                 contacts: Contacts, rank: str = None):
        self.person = person
        self.position = position
        self.contacts = contacts
        self.rank = rank

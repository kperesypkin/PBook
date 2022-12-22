import sqlite3

from domain.entry import PBookEntry
from domain.person import Person
from infrastructure.database import PBookDB


class Phonebook:
    """Phonebook class"""
    def __init__(self):
        self.db = PBookDB()

    def add_entry(self, entry: PBookEntry):
        self.db.add_entry(entry)

    def change_entry(self, entry: PBookEntry):
        pass

    def del_entry(self, entry: PBookEntry):
        pass

    def find_by_name(self, name):
        pass

    def find_by_number(self, number):
        pass




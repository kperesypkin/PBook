import sqlite3

from domain.entry import PBookEntry
from domain.person import Person

from infrastructure.config import add_entry
from infrastructure.config import add_person
from infrastructure.config import queries


class PBookDB:

    def __init__(self):
        self._on_start()

    def _on_start(self):
        self.conn = sqlite3.connect('pbook.db')
        self.cur = self.conn.cursor()
        for query in queries:
            self.cur.execute(query)
            self.conn.commit()

    def _add_person(self, person: Person):
        self.conn = sqlite3.connect('pbook.db')
        self.cur = self.conn.cursor()
        query = add_person
        insert_entry = (person.first_name, person.second_name,
                        person.patronymic)
        self.cur.execute(query, insert_entry)
        self.conn.commit()
        # self.conn.close()

    def add_entry(self, entry: PBookEntry):
        self.conn = sqlite3.connect('pbook.db')
        self.cur = self.conn.cursor()
        self._add_person(entry.person)
        query = add_entry
        insert_entry = (entry.number, entry.person.first_name,
                        entry.person.second_name, entry.person.patronymic)
        self.cur.execute(query, insert_entry)
        self.conn.commit()
        self.conn.close()

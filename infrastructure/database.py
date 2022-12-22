import sqlite3

from domain.entry import PBookEntry
from domain.person import Person

from infrastructure.config import ADD_ENTRY
from infrastructure.config import ADD_PERSON
from infrastructure.config import ENTRIES_TBL
from infrastructure.config import PERSONS_TBL, FIND_BY_NUMBER


class PBookDB:
    """Phonebook database class."""
    db_name = "pbook.db"

    def __init__(self):
        self._on_start()

    def _on_start(self):
        queries = ENTRIES_TBL, PERSONS_TBL
        for query in queries:
            self._run_query(query)

    def add_entry(self, entry: PBookEntry):
        """Add an entry to database."""
        query = ADD_ENTRY
        parameters = (entry.number, entry.person.first_name,
                      entry.person.second_name, entry.person.patronymic)
        self._add_person(entry.person)
        self._run_query(query, parameters)

    def find_by_number(self, number):
        query = FIND_BY_NUMBER
        parameters = (number, )
        self._run_query(query, parameters)

    def find_by_name(self, name):
        pass

    def _add_person(self, person: Person):
        query = ADD_PERSON
        parameters = (person.first_name, person.second_name,
                      person.patronymic)
        self._run_query(query, parameters)

    def _run_query(self, query, parameters=()):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            result = cursor.execute(query, parameters)
            conn.commit()
        return result

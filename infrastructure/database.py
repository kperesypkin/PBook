import sqlite3

from domain.entry import PBookEntry
from domain.employee import Employee

from infrastructure.config import ADD_ENTRY
from infrastructure.config import ADD_PERSON
from infrastructure.config import ENTRIES_TBL
from infrastructure.config import FIND_ALL
from infrastructure.config import FIND_BY_NUMBER
from infrastructure.config import PERSONS_TBL


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
        parameters = (entry.number, entry.employee.first_name,
                      entry.employee.second_name, entry.employee.patronymic)
        self._add_employee(entry.employee)
        self._run_query(query, parameters)

    def find_by_number(self, number):
        query = FIND_BY_NUMBER
        parameters = (number, )
        result = self._run_query(query, parameters).fetchall()
        return result

    def find_by_name(self, name):
        pass

    def find_all(self):
        query = FIND_ALL
        rows = self._run_query(query).fetchall()
        return rows

    def _add_employee(self, employee: Employee):
        query = ADD_PERSON
        parameters = (employee.first_name, employee.second_name,
                      employee.patronymic)
        self._run_query(query, parameters)

    def _run_query(self, query, parameters=()):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            result = cursor.execute(query, parameters)
            return result

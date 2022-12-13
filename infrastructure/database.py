import sqlite3


class Database:
    def __init__(self):
        self._con = sqlite3.connect("contacts.db")
        self._cur = self._con.cursor()
        
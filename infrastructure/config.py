ENTRIES_TBL = """
          CREATE TABLE IF NOT EXISTS
          entries
(
          id             INTEGER,
          person_id      INTEGER,
          phone_number   TEXT           NOT NULL,
          CONSTRAINT     entry_id       PRIMARY KEY (id),
          CONSTRAINT     person_fk      FOREIGN KEY (person_id) REFERENCES persons (id)
          CONSTRAINT     pid_number_u   UNIQUE (person_id, phone_number)
);
"""

PERSONS_TBL = """
          CREATE TABLE IF NOT EXISTS
          persons
(
          id             INTEGER,
          first_name     TEXT         NOT NULL,
          second_name    TEXT         NOT NULL,
          patronymic     TEXT,
          CONSTRAINT     person_pk    PRIMARY KEY (id),
          CONSTRAINT     full_name_u  UNIQUE (first_name, second_name, patronymic)
);
"""

ADD_PERSON = """
          INSERT OR IGNORE INTO
          persons (first_name, second_name, patronymic)
          VALUES (?, ?, ?)
"""

ADD_ENTRY = """
          INSERT OR IGNORE INTO
          entries (phone_number, person_id)
          SELECT ?, id
          FROM persons
          WHERE first_name = ? AND second_name = ? AND patronymic = ?
"""

FIND_ALL = """
          SELECT p.second_name, p.first_name, p.patronymic, e.phone_number
          FROM persons p
          LEFT JOIN entries e
          ON p.id = e.person_id
          ORDER BY p.second_name DESC
"""

FIND_BY_NUMBER = """
          SELECT p.second_name, p.first_name, p.patronymic, e.phone_number
          FROM persons p
          LEFT JOIN entries e
          ON p.id = e.person_id
          WHERE e.phone_number = ?
          ORDER BY p.second_name DESC
"""

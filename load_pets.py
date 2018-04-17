#!/usr/bin/python2.7

# Standard library imports.
from contextlib import closing
from sqlite3 import connect


# The path of the database.
db_path = r"/mnt/c/Users/Amanda/Desktop/spring-2018/is211/pets.db"


# The tables to be modified.
tables = ["person", "pet", "person_pet"]


# The queries used to insert records.
insert = {
    "person": """
INSERT INTO person (
    id,
    first_name,
    last_name,
    age
) VALUES (
    ?,
    ?,
    ?,
    ?
); """,
    "pet": """
INSERT INTO pet (
    id,
    name,
    breed,
    age,
    dead
) VALUES (
    ?,
    ?,
    ?,
    ?,
    ?
); """,
    "person_pet": """
INSERT INTO person_pet (
    person_id,
    pet_id
) VALUES (
    ?,
    ?
); """,
}


# The hard-coded input to be inserted into the database.
data = {
    "person": [
        (1, 'James',   'Smith',  41),
        (2, 'Diana',   'Greene', 23),
        (3, 'Sara',    'White',  27),
        (4, 'William', 'Gibson', 23),
    ],
    "pet": [
        (1, 'Rusty', 'Dalmation',       4, 1),
        (2, 'Bella', 'Alaskan Malamute', 3, 0),
        (3, 'Max',   'Cocker Spaniel',   1, 0),
        (4, 'Rocky', 'Beagle',          7, 0),
        (5, 'Rufus', 'Cocker Spaniel',   1, 0),
    ],
    "person_pet": [
        (1, 1),
        (1, 2),
        (2, 3),
        (2, 4),
        (3, 5),
        (4, 6),
    ]
}


# Execute the necessary insert statements.
with closing(connect(db_path)) as conn:
    cursor = conn.cursor()
    for table in tables:
        for record in data[table]:
            cursor.execute(insert[table], record)
    conn.commit()


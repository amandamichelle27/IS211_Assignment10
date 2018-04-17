#!/usr/bin/python2.7

# Standard library imports.
from contextlib import closing
from sqlite3 import connect


# The path of the database.
db_path = r"/mnt/c/Users/Amanda/Desktop/spring-2018/is211/pets.db"


# The query used to query people.
select_person = """
SELECT first_name, last_name, age
FROM   person
WHERE  id = ?
"""


# The query used to query pets.
select_pet = """
SELECT name, breed, dead, age
FROM   pet
JOIN   person_pet
ON     pet_id = id
WHERE  person_id = ?
"""


# The function to be executed repeatedly.
def perform_query():
    # Fetch the user input.
    try:
        id = int(raw_input("Please enter the person ID you wish to search for: "))
    except ValueError:
        print "Invalid input. Please try again."
        return perform_query()
    # Exit as necessary.
    if id == -1:
        return
    # Execute the necessary insert statements.
    with closing(connect(db_path, isolation_level=None)) as conn:
        cursor = conn.cursor()
        # Retrieve any matching people.
        result = cursor.execute(select_person, [id]).fetchone()
        if not result:
            print "No people exist for the given ID."
            return perform_query()
        print "%s %s, %d years old" % result
        # Retrieve any match pets.
        for name, breed, dead, age in cursor.execute(select_pet, [id]):
            print "%s %s %s %s, a %s that %s %d years old." % (
                result[0], result[1], "owned" if dead else "owns", name,
                breed, "was" if dead else "is", age)
        perform_query()
    


if __name__ == "__main__":
    perform_query()

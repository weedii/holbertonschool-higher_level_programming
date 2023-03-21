#!/usr/bin/python3

"""Script that lists all cities from the database hbtn_0e_4_usa"""

import MySQLdb
import sys

if __name__ == "__main__":

    database = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306
    )

    query = "SELECT cities.id, cities.name, states.name FROM cities INNER JOIN states ON cities.state_id = states.id ORDER BY cities.id ASC"

    cur = database.cursor()
    cur.execute(query)
    rows = cur.fetchall()

    for row in rows:
        print("{}".format(row))

    cur.close()
    database.close()

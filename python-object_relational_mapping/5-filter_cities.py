#!/usr/bin/python3

"""
script that takes in the name of a state as an argument and lists 
all cities of that state, using the database hbtn_0e_4_usa
"""

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

    query = "SELECT cities.name\
        FROM cities INNER JOIN states\
        ON states.id = cities.state_id\
        WHERE name=%s\
        ORDER BY cities.id ASC"

    cur = database.cursor()
    cur.execute(query, (sys.argv[4],))
    rows = cur.fetchall()

    for row in rows:
        if (sys.argv[4] == row[1]):
            print("{}".format(row))

    cur.close()
    database.close()

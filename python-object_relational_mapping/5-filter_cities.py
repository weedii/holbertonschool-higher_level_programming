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

    query = """SELECT cities.name
                FROM cities INNER JOIN states
                ON states.id = cities.state_id
                WHERE states.name=%s
                ORDER BY cities.id ASC"""

    cur = database.cursor()
    cur.execute(query, (sys.argv[4],))
    rows = cur.fetchall()

    lis = []
    for row in rows:
        lis.append(row[0])
        lis.append(', ')
    for i in range(len(lis) - 1):
        print(lis[i], end="")
    print()

    cur.close()
    database.close()

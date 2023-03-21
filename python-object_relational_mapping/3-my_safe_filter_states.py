#!/usr/bin/python3

"""
script that takes in an argument and displays all values in
the states table of hbtn_0e_0_usa where name matches the argument
But this time, its a one that is safe from MySQL injections!
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

    query = "SELECT * FROM states WHERE name=%s ORDER BY id ASC"

    cur = database.cursor()
    cur.execute(query, (sys.argv[4],))
    rows = cur.fetchall()

    for row in rows:
        if (sys.argv[4] == row[1]):
            print("{}".format(row))

    cur.close()
    database.close()

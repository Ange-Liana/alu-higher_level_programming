#!/usr/bin/python3
"""Lists states with names containing lowercase 'n'."""

import sys
import MySQLdb

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cur = db.cursor()

    # STRICT SQL FILTER (case-sensitive)
    cur.execute(
        "SELECT id, name FROM states "
        "WHERE name LIKE BINARY '%n%' "
        "ORDER BY id"
    )

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()

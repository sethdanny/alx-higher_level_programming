#!/usr/bin/env python3
"""
connect to the database and fetch data
"""
import MySQLdb
import sys

mydb = MySQLdb.connect(
            host="localhost",
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            port=3306
        )

cur = mydb.cursor()
cur.execute("SELECT * FROM states WHERE name LIKE BINARY'{}\
            ' ORDER BY states.id ASC".format(sys.argv[4]))
rows = cur.fetchall()
for row in rows:
    print(row)
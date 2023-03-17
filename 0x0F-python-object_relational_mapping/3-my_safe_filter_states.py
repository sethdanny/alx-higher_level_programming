#!/usr/bin/python3
"""
takes in an argument and display all values
from the states table where name is free
from sql injection
"""

if __name__ == '__main__':
    import MySQLdb
    import sys

    mydb = MySQLdb.connect(host='localhost', port=3306,
                           user=sys.argv[1], passwd=sys.argv[2],
                           db=sys.argv[3])
    cur = mydb.cursor()
    cur.execute("SELECT * FROM states WHERE name=%s\
                ORDER BY states.id ASC", (sys.argv[4]))
    rows = cur.fetchall()
    for row in rows:
        print(row)
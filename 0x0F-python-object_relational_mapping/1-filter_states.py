#!/usr/bin/python3
"""
connect to the database and fetch data
"""

if __name__ == '__main__':
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
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%'\
             ORDER BY states.id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)

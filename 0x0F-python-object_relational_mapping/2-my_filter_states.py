#!/usr/bin/env python3
"""
connect to the database and fetch data 
"""
import MySQLdb
import sys


if __name__ == "__main__":
    try:
        mydb = MySQLdb.connect(
            host="localhost",
            user=sys.argv[1], 
            passwd=sys.argv[2],
            db=sys.argv[3],
            port=3306
        )
    except:
        print("error in connection")
    try:
        cur = mydb.cursor()
        cur.execute("SELECT * FROM states WHERE name LIKE BINARY'{}' ORDER BY states.id ASC".format(sys.argv[4]))
        rows = cur.fetchall()
        for row in rows:
            print(row)
    except:
        print("Error in fectching data")
    cur.close()
    mydb.close()

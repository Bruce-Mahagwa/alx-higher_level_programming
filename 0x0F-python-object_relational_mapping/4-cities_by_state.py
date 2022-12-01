#!/usr/bin/python3
# Prints cities with states according to their id
import sys
import MySQLdb
if __name__ == "__main__":
    dbs = MySQLdb.connect(user = sys.argv[1], passwd = sys.argv[2], db = sys.argv[3], host = "localhost", port = 3306)
    cur = dbs.cursor()
    cur.execute("SELECT * FROM cities ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    dbs.close()

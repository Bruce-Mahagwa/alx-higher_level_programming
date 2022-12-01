#!/usr/bin/python3
#creates queries to list all the states in ascending order
import sys
import MySQLdb
#dbs = MySQLdb.connect(host = "localhost", user = "root", passwd = "root", port = 3306, db = "hbtn_0e_0_usa")
if __name__ == "__main__":
    dbs = MySQLdb.connect(user = sys.argv[1], passwd = sys.argv[2], db = sys.argv[3], host = "localhost", port = 3306)
    cur = dbs.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    dbs.close()

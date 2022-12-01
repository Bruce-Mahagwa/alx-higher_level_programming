#!/usr/bin/python3
import MySQLdb
dbs = MySQLdb.connect(host = "localhost", user = "root", passwd = "root", port = 3306, db = "hbtn_0e_0_usa")
cur = dbs.cursor()
cur.execute("SELECT * FROM states ORDER BY id ASC")
rows = cur.fetchall()
for row in rows:
    if (row[1][0] == "N"):
        print(row)
cur.close()
dbs.close()

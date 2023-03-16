#!/usr/bin/python3
"""This module retrieves data from database"""
from sys import argv
import MySQLdb

HOST = "localhost"
PORT = 3306
USER = argv[1]
PASSWD = argv[2]
D_BASE = argv[3]

db = MySQLdb.connect(
    host=HOST, port=PORT, user=USER, passwd=PASSWD, db=D_BASE, charset="utf8"
)
cur = db.cursor()

cur.execute("SELECT id, name FROM states WHERE name LIKE 'N%'")

all_rows = cur.fetchall()
for row in all_rows:
    print(row)

cur.close()
db.close()

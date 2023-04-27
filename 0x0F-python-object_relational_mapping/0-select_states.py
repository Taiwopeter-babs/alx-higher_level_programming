#!/usr/bin/python3
"""This module retrieves data from database"""
from sys import argv
import MySQLdb


def query_data():
    """Queries a database with module"""
    HOST = "localhost"
    PORT = 3306
    USER = argv[1]
    PWD = argv[2]
    D_BASE = argv[3]

    db = MySQLdb.connect(
        host=HOST, port=PORT, user=USER, passwd=PWD, db=D_BASE, charset="utf8"
    )
    cur = db.cursor()

    cur.execute("SELECT * FROM states ORDER BY id")

    all_rows = cur.fetchall()
    for row in all_rows:
        print(row)

    cur.close()
    db.close()


if __name__ == "__main__":
    query_data()

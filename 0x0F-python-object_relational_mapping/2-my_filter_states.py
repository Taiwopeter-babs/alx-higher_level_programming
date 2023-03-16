#!/usr/bin/python3
"""This module retrieves data from database"""
from sys import argv
import MySQLdb


def query_with_filter():
    """Get filter results returned to object"""
    HOST = "localhost"
    PORT = 3306
    USER = argv[1]
    PWD = argv[2]
    D_BASE = argv[3]
    arg = argv[4]

    db = MySQLdb.connect(
        host=HOST, port=PORT, user=USER, passwd=PWD, db=D_BASE, charset="utf8"
    )
    cur = db.cursor()

    cur.execute("SELECT id, name FROM states WHERE name='{}' ORDER BY id".format(arg))

    all_rows = cur.fetchall()
    for row in all_rows:
        print(row)

    cur.close()
    db.close()


if __name__ == "__main__":
    query_with_filter()

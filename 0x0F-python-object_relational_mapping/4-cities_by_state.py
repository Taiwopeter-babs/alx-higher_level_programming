#!/usr/bin/python3
"""This module retrieves data from database"""
from sys import argv
import MySQLdb


def query_multiple_tables():
    """Return results to object"""
    HOST = "localhost"
    PORT = 3306
    USER = argv[1]
    PWD = argv[2]
    D_BASE = argv[3]

    db = MySQLdb.connect(
        host=HOST, port=PORT, user=USER, passwd=PWD, db=D_BASE, charset="utf8"
    )
    cur = db.cursor()

    # SQL command
    sql_cmd = (
        "SELECT c.id, c.name, st.name "
        "FROM cities c "
        "LEFT JOIN states st "
        "ON c.state_id = st.id ORDER BY c.id"
    )
    cur.execute(sql_cmd)

    all_rows = cur.fetchall()
    for row in all_rows:
        print(row)

    cur.close()
    db.close()


if __name__ == "__main__":
    query_multiple_tables()

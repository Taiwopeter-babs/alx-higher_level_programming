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
    state_arg = argv[4]

    db = MySQLdb.connect(
        host=HOST, port=PORT, user=USER, passwd=PWD, db=D_BASE, charset="utf8"
    )
    cur = db.cursor()

    # SQL command
    sql_cmd = (
        "SELECT c.name "
        "FROM cities c "
        "LEFT JOIN states st "
        "ON c.state_id = st.id "
        "WHERE st.name = %s "
        "ORDER BY c.id"
    )
    cur.execute(sql_cmd, (state_arg,))

    all_rows = cur.fetchall()
    for idx, row in enumerate(all_rows):
        if idx == len(all_rows) - 1:
            print(row[0])
        else:
            print(row[0], end=", ")

    cur.close()
    db.close()


if __name__ == "__main__":
    query_multiple_tables()

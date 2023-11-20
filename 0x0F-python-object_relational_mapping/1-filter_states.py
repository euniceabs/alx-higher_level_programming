#!/usr/bin/python3
""" a python script that lists all states with a name
starting with N (upper N) from the database hbtn_0e_0_usa
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    db_connect = MySQLdb.connect(
        host="localhost",
        user=argv[1],
        port=3306,
        passwd=argv[2],
        db=argv[3])

    db_cursor = db_connect.cursor()

    db_cursor.execute("""SELECT * FROM states WHERE name
                      LIKE BINARY 'N%' ORDER BY states.id""")

    states = db_cursor.fetchall()

    for state in states:
        print(state)

    db_cursor.close()
    db_connect.close()

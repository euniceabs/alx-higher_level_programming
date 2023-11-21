#!/usr/bin/python3
"""  a python script that retrieves and displays values from the "states"
table of the hbtn_0e_0_usa database. The script takes an argument
representing a state name and returns all matching records from the table.
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    try:
        db_connect = MySQLdb.connect(
            host="localhost",
            user=argv[1],
            port=3306,
            passwd=argv[2],
            db=argv[3])

        db_cursor = db_connect.cursor()

        db_cursor.execute(
            "SELECT cities.id, cities.name, states.name "
            "FROM cities "
            "JOIN states ON cities.state_id = states.id "
            "ORDER BY cities.id ASC"
        )

        states = db_cursor.fetchall()

        for state in states:
            print(state)

        db_cursor.close()
        db_connect.close()

    except MySQLdb.Error as e:
        print("MySQL Error:", e)

#!/usr/bin/python3
"""  a python script that takes in an argument and displays all
values in the states table of hbtn_0e_0_usa where name
matches the argument.
"""

import MySQLdb
import sys  # Add this import

if __name__ == '__main__':
    try:
        if len(sys.argv) != 5:
            print("Usage: {} username password database state_name"
                  .format(sys.argv[0]))

        else:
            db_connect = MySQLdb.connect(
                host="localhost",
                user=sys.argv[1],
                port=3306,
                passwd=sys.argv[2],
                db=sys.argv[3])

            db_cursor = db_connect.cursor()

            db_cursor.execute(
                "SELECT * FROM states WHERE name LIKE "
                "BINARY %s",
                (sys.argv[4],))

            states = db_cursor.fetchall()

            for state in states:
                print(state)

            db_cursor.close()
            db_connect.close()

    except MySQLdb.Error as e:
        print("MySQL Error:", e)

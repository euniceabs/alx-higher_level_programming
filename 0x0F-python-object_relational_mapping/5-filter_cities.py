#!/usr/bin/python3
"""
A python script that retrieves a list of all cities within a specified
state from the `hbtn_0e_4_usa` database.
"""

import MySQLdb
import sys

if __name__ == '__main__':
    try:
        db_connect = MySQLdb.connect(
            host="localhost",
            user=sys.argv[1],
            port=3306,
            passwd=sys.argv[2],
            db=sys.argv[3])

        db_cursor = db_connect.cursor()

        db_cursor.execute("""SELECT cities.name FROM cities
            INNER JOIN states ON states.id = cities.state_id
            WHERE states.name = %s""", (sys.argv[4],))

        cities = db_cursor.fetchall()

        if cities is not None:
            city_names = [city[0] for city in cities]
            print(", ".join(city_names))

        db_cursor.close()
        db_connect.close()

    except MySQLdb.Error as e:
        print("MySQL Error:", e)

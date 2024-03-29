#!/usr/bin/python3
"""
Displays all cities of a given state from the
states table of the database hbtn_0e_4_usa.
Safe from SQL injections.
Usage: ./5-filter_cities.py <mysql username> <mysql password>  <database name>
                           <state name searched>
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3], charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name \
                 FROM cities, states WHERE  cities.state_id = states.id\
                 ORDER BY cities.id;")
    query_rows = cur.fetchall()
    print(", ".join(row[1] for row in query_rows if row[2] == argv[4]))
    cur.close()
    conn.close()

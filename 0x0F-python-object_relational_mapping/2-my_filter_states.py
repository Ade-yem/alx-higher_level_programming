#!/usr/bin/python3
"""
 Displays all values in the states table of the database hbtn_0e_0_usa
 whose name matches that supplied as argument.
 Usage: ./2-my_filter_states.py <mysql username> <mysql password>
                             <database name> <state name searched>
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    conn = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM states WHERE name = '{argv[4]}'")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()

#!/usr/bin/python3
"""
Script that lists all states with a name starting with N (upper N).
"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    cursor = db.cursor()
    cursor.execute(
        "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY states.id ASC"
    )
    rows = cursor.fetchall()
    for row in rows:
        if row[1].startswith('N'):
            print(row)
    cursor.close()
    db.close()

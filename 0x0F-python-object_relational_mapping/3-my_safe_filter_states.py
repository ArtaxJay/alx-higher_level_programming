#!/usr/bin/python3
"""Outputs all the states from hbtn_0e_0_usa DB."""
import MySQLdb
import sys

if __name__ == "__main__":
    DBname = MySQLdb.connect(host="localhost", user=sys.argv[1],
                             passwd=sys.argv[2], db=sys.argv[3], port=3306)
    my_cursor = DBname.cursor()
    equal_search = sys.argv[4]
    my_cursor.execute("SELECT * FROM states WHERE name LIKE %s",
                      (equal_search, ))
    tbl_records = my_cursor.fetchall()
    for record in tbl_records:
        print(record)
    my_cursor.close()
    DBname.close()

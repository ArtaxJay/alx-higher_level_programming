#!/usr/bin/python3
"""Outputs all the states from hbtn_0e_0_usa DB."""
import MySQLdb
import sys

if __name__ == "__main__":
    DBname = MySQLdb.connect(host="localhost", user=sys.argv[1],
                             passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = DBname.cursor()
    cur.execute("SELECT * FROM states")
    tbl_records = cur.fetchall()
    for record in tbl_records:
        print(record)
    cur.close()
    DBname.close()

#!/usr/bin/python3
"""Outputs all the states from hbtn_0e_0_usa DB."""
import MySQLdb
import sys

if __name__ == "__main__":
    DBname = MySQLdb.connect(host="localhost", user=sys.argv[1],
                             passwd=sys.argv[2], db=sys.argv[3], port=3306)
    my_cursor = DBname.cursor()
    my_cursor.execute("""SELECT cities.name FROM
    cities INNER JOIN states ON states.id=cities.state_id
                      WHERE states.name=%s""", (sys.argv[4],))
    tbl_records = my_cursor.fetchall()
    tmp_var = list(record[0] for record in tbl_records)
    print(*tmp_var, sep=", ")
    my_cursor.close()
    DBname.close()

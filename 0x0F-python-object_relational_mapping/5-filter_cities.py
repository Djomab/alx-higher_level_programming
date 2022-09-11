#!/usr/bin/python3
"""lists all states from the database 'hbtn_0e_0_usa'"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])
    cursor = db.cursor()
    cursor.execute("""SELECT cities.name FROM states INNER JOIN cities ON
    states.id = cities.state_id
    WHERE states.name = %(name)s ORDER BY cities.id ASC""", {'name': argv[4]})
    rows = cursor.fetchall()
    resultLenght = len(rows)
    if resultLenght == 0:
        print('')
    for i in range(resultLenght):
        if i < resultLenght - 1:
            print("{}".format(rows[i][0]), end=", ")
        else:
            print("{}".format(rows[i][0]))
    cursor.close()
    db.close()

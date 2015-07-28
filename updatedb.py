# -*- coding: utf-8 -*-
import csv, sys
import _mysql, string
import MySQLdb
from collections import OrderedDict

db = MySQLdb.connect("127.0.0.1","root","root123","mysqldbname", init_command="set names utf8")
cursor = db.cursor()
rows = ()
rowsall = rows

f = open('data.csv', 'r')
for row in csv.reader(f):
    print row[0], row[1], row[2]
    cursor.execute("""
    UPDATE table SET ID_no=%s,apply_type=%s,phone=%s,cellphone=%s,addr=%s,email=%s
    WHERE id = %s 
    """, [row[1], row[2], row[3], row[4], row[5], row[6], row[0]])

    db.commit()

f.close()

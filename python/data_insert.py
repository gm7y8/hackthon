#!/usr/bin/python

import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","root","Master@449","Customer_Data" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

for line in open(PATH_TO_FILE):
    cursor.execute(line)
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Commit your changes in the database
   db.commit()
except:
   # Rollback in case there is any error
   db.rollback()

# disconnect from server
db.close()
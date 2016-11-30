#!/usr/bin/python
import mysql.connector

#open database connection
db=mysql.connector.connect(user="m26415147",password="26415147",host="localhost",database="m26415147")

# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method.
cursor.execute("SELECT VERSION()")

# Fetch a single row using fetchone() method.
data = cursor.fetchone()

print "Database version : %s" % data












# disconnect from server
db.close()


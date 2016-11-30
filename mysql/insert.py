#!/usr/bin/python
import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","m26415147","26415147","m26415147")

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Inserts value
sql = """INSERT INTO jurusan VALUES
  (284,'Sastra Pemrograman'
  )"""
cursor.execute(sql)
cursor.execute("INSERT INTO jurusan VALUES(264,'Informatika')")
# disconnect from server
db.close()


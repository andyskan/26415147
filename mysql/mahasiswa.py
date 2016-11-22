#!/usr/bin/python

import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","m26415147","26415147","m26415147")

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Drop table if it already exist using execute() method.
cursor.execute("DROP TABLE IF EXISTS MAHASISWA")

# Create table as per requirement
sql = """CREATE TABLE mahasiswa(
    nrp       NUMBER(7) CONSTRAINT nrp_pk PRIMARY KEY,
    nama      VARCHAR2(30),
    tgl_lahir DATE,
    id_jur    NUMBER(7),
    CONSTRAINT mahasiswa_fk_id_jur FOREIGN KEY(id_jur) REFERENCES JURUSAN(id_jur));"""
cursor.execute(sql)

# disconnect from server
db.close()


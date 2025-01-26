import sqlite3

conn = sqlite3.connect("Chapter_14_ETL_in_Python/167_Intro_to_SQLite3/datafile_02.db")
cursor = conn.cursor()
cursor.execute("""
create table people (id integer promary key, name text, count integer)""")

cursor.execute("""insert into people (name, count) values ('Bob', 15)""")

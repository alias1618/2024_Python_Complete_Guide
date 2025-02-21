import sqlite3

conn = sqlite3.connect("Chapter_14_ETL_in_Python/169_SQL_Injection/datafile.db")
cursor = conn.cursor()
# name = input("Please type the name you want to search")
# cursor = conn.cursor()
# result = cursor.execute("""select * from people where name = '{}'""".format(name))
result = cursor.execute("""
create table people (id integer primary key, name text, count integer)""")
result = cursor.execute("insert into people (name, count) values ('Adam', 36)")
result = cursor.execute("insert into people (name, count) values ('Wilson', 85)")
result = cursor.execute("insert into people (name, count) values ('Grace', 55)")
conn.commit()
conn.close()
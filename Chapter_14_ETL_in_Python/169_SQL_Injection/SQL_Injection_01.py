import sqlite3

conn = sqlite3.connect("Chapter_14_ETL_in_Python/169_SQL_Injection/datafile.db")

name = input("Please type the name you want to search:")
cursor = conn.cursor()
result = cursor.execute("""select * from people where name = '{}'""".format(name))

print(result.fetchall())
conn.close()
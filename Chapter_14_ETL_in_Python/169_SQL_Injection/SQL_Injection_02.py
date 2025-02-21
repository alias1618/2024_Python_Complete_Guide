import sqlite3

conn = sqlite3.connect("Chapter_14_ETL_in_Python/169_SQL_Injection/datafile.db")
cursor = conn.cursor()

name = input("Please type the name you want to search:")
result = cursor.execute("""select * from people where name = :username""", {"username": name})

print(result.fetchall())
conn.close()
import sqlite3

conn = sqlite3.connect("Chapter_14_ETL_in_Python/168_CRUD_of_SQLite_3/datafile_03.db")
cursor = conn.cursor()

cursor.execute("""update people set count = :usercount where name = :username""",{"username": 'Bob', "usercount":39})
result = cursor.execute("select * from people")
print(result.fetchall())

conn.commit()
conn.close()
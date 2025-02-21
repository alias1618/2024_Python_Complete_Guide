import sqlite3

conn = sqlite3.connect("Chapter_14_ETL_in_Python/168_CRUD_of_SQLite_3/datafile_03.db")
cursor = conn.cursor()

result = cursor.execute("select * from people")
print(result.fetchmany(1))

conn.commit()
conn.close()
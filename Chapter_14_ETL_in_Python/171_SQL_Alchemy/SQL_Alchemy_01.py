from sqlalchemy import create_engine, select, MetaData, Table, Column, Integer, String
from sqlalchemy.orm import sessionmaker

dbPath = 'Chapter_14_ETL_in_Python/171_SQL_Alchemy/datafile.db'
engine = create_engine('sqlite:///%s' % dbPath)
metadata = MetaData(engine)
people = Table('people', metadata, Column('id', Integer, primary_key=True), Column(
    'name', String), Column('count', Integer))
Session = sessionmaker(bind=engine)
session = Session()
metadata.create_all(engine)


insert_statment = people.insert().values(name='Spencer', count=66)
print(str(insert_statment))
session.execute(insert_statment)
session.commit()

result = session.execute(select([people]))
for row in result:
    print(row)

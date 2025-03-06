from sqlalchemy import create_engine, select, MetaData, Table, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


dbPath = 'Chapter_14_ETL_in_Python/173_Class_Objects_as_Data_Row/datafile01.db'
engine = create_engine('sqlite:///%s' % dbPath)
metadata = MetaData(engine)
people = Table('people', metadata, Column('id', Integer, primary_key=True), Column(
    'name', String), Column('count', Integer))

Base = declarative_base()
class People(Base):
    __tablename__ = 'people'
    id = Column(Integer, primary_key=True)
    name = Column('name', String)
    count = Column('count', Integer)

Session = sessionmaker(bind=engine)
session = Session()
metadata.create_all(engine)

wilson = session.query(People).filter_by(name='Wilson').first()
session.delete(wilson)
session.commit()


for r in session.query(people).all():
    print(r.id, r.name, r.count)

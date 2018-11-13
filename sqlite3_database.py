from sqlalchemy import create_engine
from sqlalchemy import MetaData, Table
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///telepulesek.db')

Session = sessionmaker(bind=engine)
session = Session()

metadata = MetaData()
varosok = Table('varosok', metadata, autoload=True, autoload_with=engine)

# for instance in session.query(varosok).order_by(varosok.c.nev):
#    print(instance)

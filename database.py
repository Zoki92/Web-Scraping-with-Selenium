from sqlalchemy import (create_engine, Table,
                        Column, Integer, String,
                        MetaData, ForeignKey, Float)
from sqlalchemy.sql import select


engine = create_engine("sqlite:///testdb.sqlite")
metadata = MetaData()


prices = Table('prices', metadata,
               Column('id', Integer, primary_key=True),
               Column('name', String),
               Column('supermarket', String),
               Column('price', Float),
               )


metadata.create_all(engine)

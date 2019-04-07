from sqlalchemy import create_engine

engine = create_engine("sqlite:///testdb.sqlite")

connection = engine.connect()

results = engine.execute('SELECT * FROM prices')


for row in results:
    print(row)

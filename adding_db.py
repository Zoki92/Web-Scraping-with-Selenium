
from asdascraping import data
from database import prices, engine


ins = prices.insert().values(name="bananas", supermarket="Asda", price=data[0])
connection = engine.connect()
connection.execute(ins)

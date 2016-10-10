from model import *

db.connect()

db.drop_tables([Person], safe=True, cascade=True)
db.create_tables([Person], safe=True)

Person.create(name="A", age=2)
Person.create(name="B", age=3)
Person.create(name="C", age=4)
Person.create(name="D", age=5)
Person.create(name="E", age=6)

from peewee import *

# Configure your database connection here
# database name = should be your username on your laptop
# database user = should be your username on your laptop
db = PostgresqlDatabase('testtt', user='komlancz')


class BaseModel(Model):
    """A base model that will use our Postgresql database"""
    class Meta:
        database = db


class Person(BaseModel):

    name = CharField()
    age = IntegerField()

    @classmethod
    def get_serialized_persons(cls):
        people_list = []
        # people_list = [{'name': 'Bela', 'age': 20}, {'name': 'Mary', 'age': 21}]
        for element in Person.select():
            person_dict = {}
            person_dict['id'] = element.id
            person_dict['name'] = element.name
            person_dict['age'] = element.age
            people_list.append(person_dict)

        return people_list

    @classmethod
    def get_person_by_id(cls, id):
        return_dict = {}
        element = Person.select(cls.name, cls.age).where(cls.id == id).get()
        return_dict['name'] = element.name
        return_dict['age'] = element.age
        return return_dict

    @classmethod
    def get_person_by_name(cls, name):
        return_dict = {}
        element = Person.select(cls.name, cls.age).where(cls.name == name).get()
        return_dict['name'] = element.name
        return_dict['age'] = element.age
        return return_dict
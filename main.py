from sqlalchemy import create_engine, Column, String, Integer, CHAR
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()


class Person(Base):
    __tablename__ = ('Persons')

    id = Column("id", Integer, primary_key=True)

    firstname = Column("firstname", String)
    lastname = Column("lastname", String)
    gender = Column("gender", CHAR)
    age = Column("age", Integer)

    def __init__(self, id, firstname, lastname, gender, age):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.gender = gender
        self.age = age

    def __repr__(self):
        return f"({self.id}, {self.firstname}, {self.lastname}, {self.age} {self.gender})"


engine = create_engine('sqlite:///mydb.db', echo=True)
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

person = Person(1, "MockName", "Mockito", "m", 19)
person1 = Person(2, "MockName1", "Mockito1", "m", 19)
person2 = Person(3, "MockName2", "Mockito2", "m", 19)
person3 = Person(4, "MockName3", "Mockito3", "m", 19)

personList = [person, person1, person2, person3]

session.add_all(personList)

session.commit()

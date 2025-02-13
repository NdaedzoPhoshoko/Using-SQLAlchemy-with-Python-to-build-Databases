from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, CHAR
from sqlalchemy.orm import declarative_base, sessionmaker

Base_class = declarative_base()
class Person(Base_class):
    __tablename__ = 'person'

    id = Column('id', Integer, primary_key=True)
    firstname = Column('firstname', String)
    lastname = Column('lastname', String)
    age = Column('age', Integer)
    gender = Column('gender', CHAR)

    def __init__(self, id, firstname, lastname, age, gender):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.gender = gender

    def __repr__(self):
        return f"{self.id} - {self.firstname} {self.lastname} - {self.gender} - {self.age}"

# We now bring the concepts of foreign keys,this means a child class can belongs to a parent class
# We create a class named Thing to show that a person can own a thing
class Thing(Base_class):
    __tablename__ = 'thing'
    # columns
    t_id = Column('thing_id', Integer, primary_key=True)
    description = Column('description', String(50))
    o_id = Column('ownder_id', Integer, ForeignKey("person.id")) # this column is a foreign key that reference to a id in person table

    def __init__(self, t_id, description, owner):
        self.t_id = t_id
        self.description = description
        self.o_id = owner

    def __repr__(self):
        return f"{self.t_id} - {self.description} is owned by {self.o_id}"

engine = create_engine("sqlite:///mydb.db", echo=True)
Base_class.metadata.create_all(bind=engine)

# Drop the 'thing' table
# Thing.__table__.drop(engine)

Session = sessionmaker(bind=engine)
sess_obj = Session()

#Note: already we've added data on the person table, so we will add data to the thing table
'''
t1 = Thing(12001239, "Phone", 1015)
t2 = Thing(101123, "Headphones", 1005)
t3 = Thing(123477, "Headphones", 123)
t4 = Thing(9959392, "Jet x3", 123) # Clement owns both Headphones and Jet x3
# adding a thing with person in implicitly, just by getting actual data in the person table
t5 = Thing(912945, "Coupe 2012", sess_obj.query(Person).filter(Person.firstname == 'Clement').first().id)

sess_obj.add(t1)
sess_obj.add(t2)
sess_obj.add(t3)
sess_obj.add(t4)
'''
sess_obj.commit()

# going through the two tables
# Display Persons who actually owns a Thing
print("\nShowing people who owns certain things.")
results = sess_obj.query(Person).filter(Person.id == Thing.o_id).all()
for person in results:
    print("|", person.firstname, "-", person.age, "-", person.gender)

print("\nShowing people who own things and the things they own")
results = sess_obj.query(Person).filter(Person.id == Thing.o_id).all()
for person in results:
    print("|", person.firstname, "-", person.age, "owns", sess_obj.query(Thing).filter(Thing.o_id == person.id).first().description)

# print("\nShowing people who do not own any thing.")



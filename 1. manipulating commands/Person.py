from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, CHAR
from sqlalchemy.orm import declarative_base, sessionmaker

Base_class = declarative_base() # Construct a base class for declarative class definitions.

class Person(Base_class):
    '''
    Person class will inherit all methods from the Base_class'''

    __tablename__ = 'person' # table name

    # Below are person table data/columns
    id = Column('id', Integer, primary_key=True)
    firstname = Column('firstname', String)
    lastname = Column('lastname', String)
    age = Column('age', Integer)
    gender = Column('gender', CHAR)

    # The init method will use the object 'self' to accept parameters
    def __init__(self, id, firstname, lastname, age, gender):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.gender = gender
    
    # method that will describe the object of this class Person
    def __repr__(self):
        return f"{self.id} - {self.firstname} {self.lastname} - {self.gender} - {self.age}"

# create a new engine, it creates a new file to work with
engine = create_engine("sqlite:///mydb.db", echo=True)

# from the class Person, create all tables and store them inside the database
# then attach it to the engine
Base_class.metadata.create_all(bind=engine)

# Creates a Session class that will instantiate an object which will be used
# to manipulate data (adding, deleting queries etc)
Session = sessionmaker(bind=engine)
sess_obj = Session()

# Populate the data in the object
'''
# Instantiate new entries
p1 = Person(123, "Clement", "Phoshoko", 24, 'm')
p2 = Person(345, "Chantelle", "Phoshoko", 17, 'f')
p3 = Person(542, "Mulweli", "Phoshoko", 8, 'm')
# Add entries to the session
sess_obj.add(p1)
sess_obj.add(p2)
sess_obj.add(p3)

# Commit all entries to the database
sess_obj.commit()
'''

# query to see select all data from our database
'''
result = sess_obj.query(Person).all() # the result is a list of objects
print(result)
'''

# query to see the rows of persons whose firstname is Clement
'''
results = sess_obj.query(Person).filter(Person.firstname=='Clement').all() # filter() returns a query

for row in results:
    print("row:", row)
'''

# query to see only the id and gender of persons whose age > 18
'''
results = sess_obj.query(Person).filter(Person.age > 18).aal()
for row in results:
    print("Person:", row.id, "-", row.gender)
'''
# if we have multiple conditions we can separate the conditions by comma
# results = sess_obj.query(Person).filter(Person.age > 18, Person.gender == 'm')

# query to fetch the names of persons whose firstname starts with letter C
results = sess_obj.query(Person).filter(Person.firstname.like("C%")).all()
for row in results:
    print(row.firstname, end='\n')
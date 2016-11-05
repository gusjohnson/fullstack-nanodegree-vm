import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Enum, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Shelter(Base):
	__tablename__ = 'shelter'
	name = Column(String(80), nullable = False)
	address = Column(String(255), nullable = False)
	city = Column(String(255), nullable = False)
	state = Column(String(2), nullable = False)
	zipCode = Column(Integer(5), nullable = False)
	website = Column(String(255), nullable = False)
	id = Column(Integer, primary_key = True)

class Puppy(Base):
	__tablename__ = 'puppy'
	name = Column(String(80),nullable = False)
	id = Column(Integer, primary_key = True)
	dateOfBirth = Column(Date, nullable = False)
	gender = Column(Enum("female", "male", name="gender_enum", create_type=False), nullable = False)
	weight = Column(Integer, nullable = False)
	picture = Column(String(255), nullable = False)
	shelter_id = Column(Integer, ForeignKey('shelter.id'))
	shelter = relationship(Shelter)
	
	
#########insert at end of file ########

engine = create_engine('sqlite:///puppyshelter.db')
Base.metadata.create_all(engine)
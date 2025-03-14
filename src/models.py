import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    firstName = Column(String(250), nullable=False)
    lastName = Column(String(250), nullable=False)
    username = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    likeCharacter = relationship("CharacterFavorites")
    likePlanet = relationship("PlanetsFavorites")
    
class Planets(Base):
    __tablename__ = 'planets'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    rotationPeriod = Column(Integer) 
    orbitalPeriod = Column(Integer) 
    diameter = Column(Integer) 
    gravity = Column(String(250))
    population = Column(Integer)
    likePlanet = relationship("PlanetsFavorites") 
    

class Characters(Base):
    __tablename__ = 'characters'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    height = Column(Integer) 
    mass = Column(Integer)
    hairColor = Column(String(250)) 
    skinColor = Column(String(250))
    birthYear = Column(String(250))
    likeCharacter = relationship("CharacterFavorites")
    

class PlanetsFavorites(Base):
    __tablename__ = 'planetsfavorites'
    id = Column(Integer, primary_key=True)
    userId = Column(Integer, ForeignKey("user.id"))
    planetId = Column(Integer, ForeignKey("planets.id"))
   
    
class CharacterFavorites(Base):
    __tablename__ = 'Characterfavorites'
    id = Column(Integer, primary_key=True)
    userId = Column(Integer, ForeignKey("user.id"))
    characterId = Column(Integer, ForeignKey("characters.id"))
  


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')

# class Person(Base):
#     __tablename__ = 'person'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)

# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)
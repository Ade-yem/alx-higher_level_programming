#!/usr/bin/python3
"""
`model_city.py` contains the class definition of a City
 and an instance Base = declarative_base()"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, UniqueConstraint, ForeignKey
from model_state import State

Base = declarative_base()


class City(Base):
    """class that defines a city
    __tablename__ (str): The name of the MySQL table to store Cities.
    id (sqlalchemy.Integer): The city's id.
    name (sqlalchemy.String): The city's name.
    state_id (sqlalchemy.Integer): The state's id.
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey(State.id))

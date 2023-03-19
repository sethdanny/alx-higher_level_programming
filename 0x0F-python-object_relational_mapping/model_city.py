#!/usr/bin/python3
""" module for model city """

from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base()

Base = declarative_base()

class City(Base):
    """ table city """
    __tablename__ = "cities"

    id = Column(Integer,  autoincrement=True, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, nullable=False, ForeignKey('state.id'))

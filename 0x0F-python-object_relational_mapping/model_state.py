#!/usr/bin/python3
"""
Create a class, State, that inherits from sqlalchemy Base class
 in order to use declarative_base() instance.
"""
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base

my_metadata = MetaData()
Base = declarative_base(metadata=my_metadata)


class State(Base):
    """
    Will create a table-state with id and name as fields.
    """
    __tablename__ = 'states'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)

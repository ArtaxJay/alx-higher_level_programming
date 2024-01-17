#!/usr/bin/python3
"""
This script will output all State objects that contains
the letter `a` from hbtn_0e_6_usa DB.
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    new_session = sessionmaker(bind=engine)
    session_obj = new_session()
    for record in session_obj.query(State).filter(State.name.like('%a%')):
        print(record.id, record.name, sep=": ")

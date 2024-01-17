#!/usr/bin/python3
"""
This script prints all City objects from hbtn_0e_14_usa DB.
"""
import sys
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    new_session = sessionmaker(bind=engine)
    session_obj = new_session()
    for record in (session_obj.query(State.name, City.id, City.name)
                     .filter(State.id == City.state_id)):
        print(record[0] + ": (" + str(record[1]) + ") " + record[2])

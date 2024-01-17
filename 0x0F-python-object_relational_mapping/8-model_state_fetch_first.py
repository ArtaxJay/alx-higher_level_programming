#!/usr/bin/python3
"""
Outputs d first State object frm hbtn_0e_6_usa DB.
"""
import sys
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    new_session = sessionmaker(bind=engine)
    session_obj = new_session()
    records = session_obj.query(State).first()
    if records is None:
        print("Nothing")
    else:
        print(records.id, records.name, sep=": ")

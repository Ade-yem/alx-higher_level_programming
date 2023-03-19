#!/usr/bin/python3
"""script that lists all State objects from the database hbtn_0e_6_usa"""
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    n = 0
    for state in session.query(State):
        if state.name == sys.argv[4]:
            print("{}".format(state.id))
            n = 1
            break
    if n == 0:
        print("Nothing")
    session.close()

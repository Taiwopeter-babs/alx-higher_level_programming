#!/usr/bin/python3
"""This module contains a function that fetches data from a table"""
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv


def query_first_of_states():
    """Queries the first of State objects"""
    # Arguments from terminal
    user = argv[1]
    pwd = argv[2]
    database = argv[3]

    """
        The engine and database schema are created
        then engine is bound to current session with session maker
    """
    URL = "mysql+mysqldb://{}:{}@localhost:3306/{}"
    engine = create_engine(URL.format(user, pwd, database))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    # creates a new session
    session = Session()

    # Query of first result
    query_states = session.query(State).first()

    if query_states is not None:
        print("{}: {}".format(query_states.id, query_states.name))
    else:
        print("Nothing")

    # Cleanup
    session.commit()
    session.close()


if __name__ == "__main__":
    query_first_of_states()

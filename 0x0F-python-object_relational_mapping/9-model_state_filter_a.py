#!/usr/bin/python3
"""This module contains a function that fetches data from a table"""
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv


def filter_query():
    """Queries the State objects by character"""
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

    # Query of filtered result
    query_states = session.query(State).filter(State.name.like("%a%"))

    # Add order to query result
    for state in query_states.order_by(State.id.asc()).all():
        print("{}: {}".format(state.id, state.name))

    # Cleanup
    session.commit()
    session.close()


if __name__ == "__main__":
    filter_query()

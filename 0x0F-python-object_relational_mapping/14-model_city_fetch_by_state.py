#!/usr/bin/python3
"""This module contains a function that fetches data from a table"""
from model_state import State, Base
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv


def query_all_city_objects():
    """Queries all City objects"""
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

    # QUERY FOR TWO TABLES
    query = session.query(State, City).join(City).order_by(City.id.asc()).all()

    for state, city in query:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    # Cleanup
    session.commit()
    session.close()


if __name__ == "__main__":
    query_all_city_objects()

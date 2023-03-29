#!/usr/bin/python3
""" This script contains a function that creates new objects
    from two different tables
"""
from relationship_city import City
from relationship_state import State, Base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sys import argv


def create_objects_from_relationship():
    try:
        USER = argv[1]
        PWD = argv[2]
        DB = argv[3]
    except IndexError:
        return

    # set the url; dialect -> mysql, driver -> mysqldb
    URL = "mysql+mysqldb://{}:{}@localhost:3306/{}"
    engine = create_engine(URL.format(USER, PWD, DB))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    # create a session
    session = Session()

    # create instances
    state = State(name="California")
    city = City(name="San Francisco")
    state.cities.append(city)

    session.add(state)
    session.commit()


if __name__ == "__main__":
    create_objects_from_relationship()

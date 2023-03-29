#!/usr/bin/python3
""" This script contains a function that creates new objects
    from two different tables
"""
from relationship_city import City
from relationship_state import State, Base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sys import argv


def query_city_objects_with_relationship():
    """
        Creates new objects
    """
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

    query = session.query(City).order_by(City.id).all()

    for city in query:
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))

    session.commit()
    session.close()


if __name__ == "__main__":
    query_city_objects_with_relationship()

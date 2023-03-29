#!/usr/bin/python3
"""This module defines a mapped class that classes
    inherit from and a State class
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base


class City(Base):
    """Definition of City Class"""

    __tablename__ = "cities"

    id = Column(Integer, autoincrement=True, primary_key=True,
                nullable=False, unique=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)

#!/usr/bin/python3
"""This module defines a mapped class that classes
    inherit from and a State class
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String


# Mapper class
Base = declarative_base()


class State(Base):
    """Definition of State Class"""

    __tablename__ = "states"

    id = Column(Integer, autoincrement=True, primary_key=True,
                nullable=False, unique=True)
    name = Column(String(128), nullable=False)

#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey


class City(BaseModel, Base):
    """ creates a city
    Inherities from BaseModel and Base
    
    Attributes:
        __tablename__(str): Creates a MYSQL table named cities
        state_id (sqlalchemy.String): The state ID of the city
        name (sqlalchemy.String): The name of the city
    """
    __tablename__ = "cities"
    state_id = Column(String(60), nullable=False, ForeignKey(state.id))
    name = Column(String(128), nullable=False)

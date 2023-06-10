#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """This class defines a user by various attributes
        Attributes:
            __tablename__ (str): MySQl table to store the user
            email (sqlalchemy.string): The user email
            password (sqlalchemy.string): The user password
            first_name (sqlalchemy.string): The user first name
            last_name (sqlalchemy.string): The user last name
    """
    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
    places = relationship("Place", backref="user", cascade="all, delete")

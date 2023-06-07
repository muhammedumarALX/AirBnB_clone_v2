#!/usr/bin/python3
"""Creating new engine DBsttorage"""
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine
import os
from models.base_model import Base



class DBStorage:
    """creates a DB storage"""
    __engine = None
    __session = None

    def __init__(self):
        """Initializes a new instance"""
        user = os.environ.get('HBNB_MYSQL_USER')
        password = os.environ.get('HBNB_MYSQL_PWD')
        host = os.environ.get('HBNB_MYSQL_HOST')
        database = os.environ.get('HBNB_MYSQL_DB')
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".format(user, password, host, database), pool_pre_ping=True)

        if os.environ.get('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """method that queries a datadbase and returns a dictionary"""
        results = {}
        if cls == None:
            from models.state import State
            from models.city import City
            from models.user import User
            objects = self.__session.query(State).all()
            objects.extend(self.__session.query(City).all())
            objects.extend(self.__session.query(User).all())
        else:
            objects = self.__session.query(cls).all()

        for obj in objects:
            key = f"{type(obj).__name__}.{obj.id}"
            results[key] = obj
        return results

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Reload a new database session"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session_factory)


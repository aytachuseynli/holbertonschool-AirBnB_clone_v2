#!/usr/bin/python3
"""
Module for DBStorage class
"""
import os
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base, BaseModel
from models.amenity import Amenity
from models.city import City
from models.state import State
from models.user import User
from models.place import Place
from models.review import Review


class DBStorage:
    """DB Storage class"""

    __engine = None
    __session = None
    all_classes = [State, City, User, Place, Review, Amenity]

    def __init__(self):
        """DBStorage Constructor"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(getenv('HBNB_MYSQL_USER'),
                                              getenv('HBNB_MYSQL_PWD'),
                                              getenv('HBNB_MYSQL_HOST'),
                                              getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)

        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """returns a dictionary of __session state objects"""
        objs = {}
        if cls is None:
            for cls in DBStorage.all_classes:
                for obj in self.__session.query(cls).all():
                    key = "{}.{}".format(obj.__class__.__name__, obj.id)
                    objs[key] = obj
        else:
            for obj in self.__session.query(eval(cls)).all():
                key = "{}.{}".format(obj.__class__.__name__, obj.id)
                objs[key] = obj
        return objs

    def new(self, obj):
        """Adds the object to the current __session"""
        self.__session.add(obj)

    def save(self):
        """Commits all changes of the current __session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete obj from the current __session"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables in the database"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """calls remove() method on the private session attribute (self.__session)"""
        self.__session.close()

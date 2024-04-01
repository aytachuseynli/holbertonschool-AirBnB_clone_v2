#!/usr/bin/python3
"""This module defines the DBStorage class for managing SQLAlchemy storage"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base
from models.city import City
from models.state import State
from models.base_model import Base
import os
import sys


Base = declarative_base()


class DBStorage:
    """This class manages storage of hbnb models using SQLAlchemy"""
    __engine = None
    __session = None
    all_classes = ["State", "City", "User", "Place", ]
    def __init__(self):
        """Instantiates a new DBStorage object"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(os.getenv('HBNB_MYSQL_USER'),
                                              os.getenv('HBNB_MYSQL_PWD'),
                                              os.getenv('HBNB_MYSQL_HOST'),
                                              os.getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)
        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Returns a dictionary of objects of a given class"""
        objs = {}
        if cls:
            objects = self.__session.query(cls).all()
            for obj in objects:
                key = "{}.{}".format(obj.__class__.__name__, obj.id)
                objs[key] = obj
        else:
            for class_name in self.all_classes:
                class_name = eval(class_name)
                objects = self.__session.query(class_name).all()
                for obj in objects:
                    key = "{}.{}".format(obj.__class__.__name__, obj.id)
                    objs[key] = obj
        return objs

    def new(self, obj):
        """Adds a new object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commits all changes to the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes obj from the current database session"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Creates all tables in the database and creates the current database session"""
        Base.metadata.create_all(self.__engine)
        session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session)
        self.__session = Session()
        
    def close(self):
        """Close session"""
        self.reload()
        self.__session.close()

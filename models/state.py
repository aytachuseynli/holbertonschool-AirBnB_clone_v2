#!/usr/bin/python3
"""This module defines the State class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    """This class represents a state"""
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")

    if getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            """Returns the list of City instances with state_id equal to the current State.id"""
            from models import storage
            cities = []
            all_cities = storage.all('City')
            for city in all_cities.values():
                if city.state_id == self.id:
                    cities.append(city)
            return cities

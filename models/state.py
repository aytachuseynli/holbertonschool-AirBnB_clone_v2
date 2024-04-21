#!/usr/bin/python3
"""
Module for State class
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv
import models


class State(BaseModel, Base):
    """State class"""
    __tablename__ = 'states'
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state",
                              cascade="all, delete-orphan")

    else:
        @property
        def cities(self):
            """returns the list of City objects from storage
            linked to the current State"""
            cities_list = []
            all_cities = models.storage.all("City")
            for city in all_cities.values():
                if city.state_id == self.id:
                    cities_list.append(city)
            return cities_list
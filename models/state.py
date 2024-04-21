#!/usr/bin/python3
"""
State module
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
from os import getenv


class State(BaseModel, Base):
    """State class"""
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="all, delete", backref="state")


    if getenv("HBNB_TYPE_STORAGE") == "db":

        @property
        def cities(self):
            """Returns the list of City instances with state_id
            equals to the current State.id"""
            from models import storage
            cities_list = []
            for city in list(storage.all(City).values()):
                if city.state_id == self.id:
                    cities_list.append(city)
            return cities_list

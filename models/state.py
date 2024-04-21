#!/usr/bin/python3
"""
State module
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
from os import getenv
from models.engine.file_storage import FileStorage


class State(BaseModel, Base):
    """State class"""
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="all, delete", backref="state")

    def __init__(self, *args, **kwargs):
        """initializes"""
        super().__init__(*args, **kwargs)



    if getenv("HBNB_TYPE_STORAGE") == "db":

        @property
        def cities(self):
            """Returns the list of City instances with state_id
            equals to the current State.id"""
            storage = FileStorage()
            return [city for city in storage.all(City).values()
                    if city.state_id == self.id]

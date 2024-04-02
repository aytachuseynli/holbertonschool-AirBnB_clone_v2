#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModeli, Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class Amenity(BaseModel):
    __tablename__ = 'amenities'
    name = Column(String(128), nulable=False)
    place_amenities = relationship('Place', secondary='place_amenity',
                                   overlaps="amenities", viewonly=False)

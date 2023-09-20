#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.city import City
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")
    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """getter for cities"""
            cities_list = [i for i in list(models.storage.all(City).values())
                           if i.state_id == self.id]
            return cities_list

#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
from models.city import City
from os import environ
import models


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    if  environ.get('HBNB_TYPE_STORAGE') == "db":
        name = Column(String(128), nullable=False)
        cities = relationship("City", cascade="all, delete", backref="state")
    else:
        name = ""

    if  environ.get('HBNB_TYPE_STORAGE') != "db":
        @property
        def cities(self):
            listCities = []
            allCites = models.storage.all()
            for key, objCity in allCites.items():
                if objCity.id == self.id:
                    listCities.append(objCity)
            return listCities

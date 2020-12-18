#!/usr/bin/python3
"""This module defines a class User"""

from models.base_model import BaseModel
from models.base_model import Base
from models.place import Place
from models.review import Review
from sqlalchemy import Column
from sqlalchemy import String
from os import getenv
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """This class defines a user by various attributes"""

    __tablename__ = 'users'
    if getenv("HBNB_TYPE_STORAGE") == "db":
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128))
        last_name = Column(String(128))
        places = relationship(
            'Place',
            cascade='all, delete',
            backref='user'
        )
        reviews = relationship(
            'Review',
            backref='user',
            cascade='all, delete-orphan'
        )
    else:
        email = ''
        password = ''
        first_name = ''
        last_name = ''

    def __init__(self, *args, **kwargs):
        """ initializes obj user """
        super().__init__(*args, **kwargs)

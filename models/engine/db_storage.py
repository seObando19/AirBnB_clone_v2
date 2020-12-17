#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
from os import environ
from sqlalchemy import create_engine
from models.base_model import BaseModel, Base
from sqlalchemy.orm import sessionmarker, scoped_session
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


def new_dict(_dict, obj):
    for ob in obj:
        key = "{}.{}".format(type(ob).__name__, ob.id)
        value = ob
        _dict[key] = value

class DBStorage:
    """"""
    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}"
                                      .format(environ.get("HBNB_MYSQL_USER"),
                                              environ.get("HBNB_MYSQL_PWD"),
                                              environ.get("HBNB_MYSQL_HOST"),
                                              environ.gte("HBNB_MYSQL_DB")),
                                              pool_pre_ping=True)
        if environ.get("HBNB_ENV") == "test":
            Base.metadata.drop(self.__engine)

    def all(self, cls=None):
        """Select all objects of a cls"""
        my_session = __session
        my_dict = {}
        my_list = ['User', 'State', 'City', 'Amenity', 'Place', 'Review']

        if cls is None:
            for cls in list:
                sess = my_session.query(eval(cls)).all()
                new_dict(my_dict, sess)
        else:
            sess = my_session.query(eval(cls)).all()
            new_dict(my_dict, sess)
        return my_dict

    def new(self, obj):
        """Add obj to the database session
        """
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the db session
        """
        self.__session.commit()

    def delete(self, obj=None):
        """Delete obj if not none
        """
        if obj not is None:
            del obj

    def reload(self):
        """Update obj
        """
        Base.metadata.create_all(self.__engine)
        session_contruct = sessionmarker(bind=self.__engine,
                                         expire_on_commit=False)
        self.__session = scoped_session(session_contruct)

#!/usr/bin/python3
"""This module defines a class to manage db storage for hbnb clone"""
from models.base_model import Base
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.user import User
from models.place import Place
from models.review import Review
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from os import getenv

classes = {
    'State': State,
    'City': City,
    'Place': Place,
    'Amenity': Amenity,
    'Review': Review,
    'User': User
}

class DBStorage:
    """This class manages storage of hbnb models in db"""
    __engine = None
    __session = None

    def __init__(self):
        """ create engine """

        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(
                getenv('HBNB_MYSQL_USER'),
                getenv('HBNB_MYSQL_PWD'),
                getenv('HBNB_MYSQL_HOST'),
                getenv('HBNB_MYSQL_DB')
            ),
            pool_pre_ping=True
        )

        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ query on the current database session - optional, filter by cls"""
        queryList = []
        queryDict = {}
        if cls in classes:
            obj = self.__session.query(classes[cls]).all()
            for obj_ in obj:
                key = "{}.{}".format(obj_.__class__.__name__, obj_.id)
                value = obj_
                queryDict[key] = value
        elif cls is None:
            for cls_ in classes:
                obj = self.__session.query(classes[cls]).all()
                for obj_ in obj:
                    key = "{}.{}".format(obj_.__class__.__name__, obj_.id)
                    value = obj_
                    queryDict[key] = value
        return queryDict
        """ d = {}

        if cls:
            obj = self.__session.query(cls).all()
        else:
            mycls = ['State', 'City', 'Amenity', 'User', 'Place', 'Review']
            obj = []
            for namecls in mycls:
                for o in self.__session.query(eval(namecls)):
                    obj.append(o)
        for item in obj:
            k = type(item).__name__ + '.' + str(item.id)
            d[k] = item
        return d """

        """ dict_ = {}

        if cls:
            query = self.__session.query(cls).all()
            for obj in query:
                delattr(obj, '_sa_instance_state')
                dict_[obj.__class__.__name__ + '.' + obj.id] = obj
        else:
            for key, value in classes.items():
                query = self.__session.query(key).all()
                for obj in query:
                    delattr(obj, '_sa_instance_state')
                    dict_[obj.__class__.__name__ + '.' + obj.id] = obj
        return dict_ """

    def new(self, obj):
        """ add the object to the current database session """
        self.__session.add(obj)

    def save(self):
        """ commit all changes of the current database session """
        self.__session.commit()

    def delete(self, obj=None):
        """ delete from the current database session obj if not None """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """  """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
            bind=self.__engine,
            expire_on_commit=False
        )
        self.__session = scoped_session(session_factory)

    def close(self):
        """ """
        self.__session.remove()

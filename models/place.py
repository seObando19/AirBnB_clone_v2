#!/usr/bin/python3
""" Imports """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, Table, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv
import models
from models.review import Review

place_amenity = Table(
    'place_amenity',
    Base.metadata,
    Column(
        'place_id',
        String(60),
        ForeignKey(
            'places.id',
            onupdate='CASCADE',
            ondelete='CASCADE'),
        primary_key=True
    ),
    Column(
        'amenity_id',
        String(60),
        ForeignKey(
            'amenities.id',
            onupdate='CASCADE',
            ondelete='CASCADE'),
        primary_key=True
    )
)


class Place(BaseModel, Base):
    """ A place to stay """

    __tablename__ = "places"

    if getenv("HBNB_TYPE_STORAGE") == "db":
        user_id = Column(
            String(60),
            ForeignKey("users.id"),
            nullable=False)

        city_id = Column(
            String(60),
            ForeignKey("cities.id"),
            nullable=False)

        name = Column(
            String(128),
            nullable=False)

        description = Column(String(1024))

        number_rooms = Column(
            Integer,
            default=0,
            nullable=False)

        number_bathrooms = Column(
            Integer,
            default=0,
            nullable=False)

        max_guest = Column(
            Integer,
            default=0,
            nullable=False)

        price_by_night = Column(
            Integer,
            default=0,
            nullable=False)

        latitude = Column(Float)

        longitude = Column(Float)

        reviews = relationship(
            'Review',
            backref='place',
            cascade='all, delete-orphan'
        )

        amenities = relationship(
            'Amenity',
            secondary=place_amenity,
            back_populates='place_amenities',
            viewonly=False
        )

        amenity_ids = []

    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

    if models.storage_type == 'fs':
        @property
        def reviews(self):
            """Method getter setter for return Cities
            instance of current state_id"""
            reviews = []
            objs = models.storage.all(models.review.Review)
            for val in objs:
                if objs[key].place_id is self.id:
                    cities.append(objs[key])
            return reviews

        @property
        def amenities(self):
            """Method that returnsthe list of Amenity instances
            based on the attribute amenity_ids that contains all Amenity.id
            linked to the Place"""
            amenity_objs = []
            for amenity_id in self.amenity_ids:
                key = 'Amenity.' + amenity_id
                if key in FileStorage.__objects:
                    amenity_objs.append(FileStorage.__objects[key])
            return amenity_objs

        @amenities.setter
        def amenities(self, obj):
            """
            adds an Amenity.id to the attribute amenity_ids if obj is
            an instance of Amenity
            """
            if isinstance(obj, Amenity):
                self.amenity_ids.append(obj.id)

    def __init__(self, *args, **kwargs):
        """ initializes obj place """
        super().__init__(*args, **kwargs)

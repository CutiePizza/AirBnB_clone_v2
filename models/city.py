#!/usr/bin/python3
"""This is the city class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from models import storage


class City(BaseModel, Base):
    """This is the class for City
    Attributes:
        state_id: The state id
        name: input name
    """
    __tablename__ = "cities"
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    name = Column(String(128), nullable=False)

    @property
    def cities(self):
        """
        Getter attribute for cities
        """
        cities = storage.all(City)
        dic = {}
        for key, value in cities.items():
            if value.state_id == self.id:
                dic[key] = value
        return dic

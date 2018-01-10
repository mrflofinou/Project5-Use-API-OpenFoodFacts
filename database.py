#! /usr/bin/env python3
# coding: utf-8

"""
This file defines the tables of the database with the ORM SQLAlchemy
The tabeles are:
    - categories
    - products
"""


from sqlalchemy import Column, Integer, String, Index, Text, ForeignKey
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.orm import relationship

from base import Base


class Category(Base):
    """
    This class defines the table of the categories of food
    """
    __tablename__ = 'categories'

    id = Column(INTEGER(unsigned=True), primary_key=True)
    name = Column(String(150), nullable=False)
    mysql_engine ='InnoDB',

    def __init__(self, name):
        self.name = name


class Product(Base):
    """
    This class defines the table of products
    """
    __tablename__ = "products"

    id = Column(INTEGER(unsigned=True), primary_key=True)
    # Creation of a Many To One association with the ID of the categories
    id_category = Column(INTEGER(unsigned=True), ForeignKey('categories.id'))
    category = relationship("Category", backref="products")
    name = Column(String(150), nullable=False)
    ingredients = Column(String(500))
    magasin = Column(String(100))
    url = Column(String(200))
    mysql_engine = 'InnoDB'

    def __init__(self, name, category, url):#, ingredients, magasin,):
        self.name = name
        self.category = category
        # self.ingredients = ingredients
        # self.magasin = store
        self.url = url

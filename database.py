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
    name = Column(String(150), nullable=False)
    # Creation of a Many To One association with the ID of the categories
    id_category = Column(INTEGER(unsigned=True), ForeignKey('categories.id'))
    category = relationship("Category", backref="products")
    mysql_engine = 'InnoDB'

    def __init__(self, name, category):
        self.name = name
        self.category = category

#! /usr/bin/env python3
# coding: utf-8

"""
This file defines the tables of the database with the ORM SQLAlchemy
The tabeles are:
    - categories
    - products
    - substitutes
"""


from sqlalchemy import Column, Integer, String, Index, Text, ForeignKey
from sqlalchemy.dialects.mysql import INTEGER, BIGINT
from sqlalchemy.orm import relationship

from base import Base


class Category(Base):
    """
    This class defines the table of the categories of food
    """
    __tablename__ = 'categories'

    id = Column(INTEGER(unsigned=True), primary_key=True)
    name = Column(String(150), nullable=False, unique=True)
    mysql_engine ='InnoDB'


class Product(Base):
    """
    This class defines the table of products
    """
    __tablename__ = "products"

    id = Column(BIGINT(unsigned=True), primary_key=True)
    # Creation of the foreign key
    id_category = Column(INTEGER(unsigned=True), ForeignKey('categories.id'), nullable=False)
    # Creation of a Many To One association with the ID of the categories
    category = relationship("Category", backref="products")
    name = Column(String(150), nullable=False)
    store = Column(String(100))
    nutriscore = Column(String(10))
    url = Column(String(200))
    mysql_engine = 'InnoDB'


class Substitute(Base):
    """
    This class defines the table of the substitutes
    """
    __tablename__ = "substitutes"

    id = Column(INTEGER(unsigned=True), primary_key=True)
    name = Column(String(150), nullable=False)
    store = Column(String(100))
    url = Column(String(200))

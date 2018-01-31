#! /usr/bin/env python3
# coding: utf-8

"""
This file defines the tables of the database with the ORM SQLAlchemy
The tabeles are:
    - categories
    - products
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
    product = relationship("Product", backref="categories")
    name = Column(String(150), nullable=False, unique=True)
    mysql_engine ='InnoDB',

    def __init__(self, name):
        self.name = name


class Product(Base):
    """
    This class defines the table of products
    """
    __tablename__ = "products"

    id = Column(INTEGER(unsigned=True), primary_key=True)
    id_product = Column(BIGINT(unsigned=True), unique=True)
    # Creation of the foreign key
    id_category = Column(INTEGER(unsigned=True), ForeignKey('categories.id'), nullable=False)
    # Creation of a Many To One association with the ID of the categories
    category = relationship("Category", backref="products")
    name = Column(String(150), nullable=False)
    store = Column(String(100))
    nutriscore = Column(String(10))
    url = Column(String(200))
    mysql_engine = 'InnoDB'

    def __init__(self, name, id_product, id_category, store,  nutriscore, url):
        self.name = name
        self.id_product = id_product
        self.id_category = id_category
        self.store = store
        self.nutriscore = nutriscore
        self.url = url


class Substitute(Base):
    """
    This class defines the table of the substitutes
    """
    __tablename__ = "substitutes"

    id = Column(INTEGER(unsigned=True), primary_key=True)
    id_substitute = Column(BIGINT(unsigned=True), nullable=False)
    id_product_substituted = Column(BIGINT(unsigned=True), nullable=False)
    name = Column(String(150), nullable=False)
    store = Column(String(100))
    url = Column(String(200))

    def __init__(self, name, substitute, product, store, url):
        self.name = name
        self.id_substitute = substitute
        self.id_product_substituted = product
        self.store = store
        self.url = url

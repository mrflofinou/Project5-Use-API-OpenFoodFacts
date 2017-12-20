#! /usr/bin/env python3
# coding: utf-8

"""
This file define the tables of the database with the ORM SQLAlchemy
The tabeles are:
    - categories
"""


from sqlalchemy import create_engine, Column, Integer, String, Index, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import settings as s


engine = create_engine('mysql+pymysql://{}:{}@localhost/test_projet05'.format(s.username, s.password))
Session = sessionmaker(bind=engine)
Base = declarative_base()

class Category(Base):
    """
    This class is for create table of the categories of food
    """
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    name = Column(String(150), nullable=False)

    def __init__(self, name):
        self.name = name

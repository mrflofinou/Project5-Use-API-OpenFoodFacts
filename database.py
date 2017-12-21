#! /usr/bin/env python3
# coding: utf-8

"""
This file define the tables of the database with the ORM SQLAlchemy
The tabeles are:
    - categories
"""


from sqlalchemy import create_engine, Column, Integer, String, Index, Text
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import settings as s

# creation of engine with our database (here mysql) and the DBAPI (here pymysql). DON'T FORGET THE CHARSET UTF8 !
engine = create_engine('mysql+pymysql://{}:{}@localhost/test_projet05?charset=utf8&use_unicode=0'.format(s.username, s.password))
Session = sessionmaker(bind=engine)
Base = declarative_base()

class Category(Base):
    """
    This class is for create table of the categories of food
    """
    __tablename__ = 'categories'

    id = Column(INTEGER(unsigned=True), primary_key=True)
    name = Column(String(150), nullable=False)
    mysql_engine='InnoDB',

    def __init__(self, name):
        self.name = name

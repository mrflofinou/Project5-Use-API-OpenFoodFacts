#! /usr/bin/env python3
# coding: utf-8

"""
This file create the tables of the database with the ORM SQLAlchemy
The tabeles are:
    - categotries
"""


from sqlalchemy import create_engine, Column, Integer, String, Index, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import settings as s


engine = create_engine('mysql+pymysql://{}:{}@localhost/test_projet05'.format(s.username, s.password))
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class Category(Base):
    """
    This class is for create the database table of the categories of food
    """
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    name = Column(String(150), nullable=False)
    description = Column(Text)

    def __init__(self, name, description):
        self.name = name
        self.description = description

# Schema mapping to create the tables
Base.metadata.create_all(engine)

category_fruits = Category("Fruits", "Que des bons fruits")
category_biscuits = Category("biscuits", "Tous ce qui croustille")

# Add the modification in database
session.add(category_fruits)
session.add(category_biscuits)
session.commit()
session.close()

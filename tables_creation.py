#! /usr/bin/env python3
# coding: utf-8

"""
This file creates the tables of the database with the ORM SQLAlchemy
"""

import json
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database import Base, Category, Product
import settings as s

# Creation of engine with our database (here mysql) and the DBAPI (here pymysql)
# DON'T FORGET THE CHARSET UTF8 !
engine = create_engine('mysql+pymysql://{}:{}@localhost/test_projet05?charset=utf8&use_unicode=0'.format(s.username, s.password))
Session = sessionmaker(bind=engine)
# Creation of a session to commnicate with the database
session = Session()
# Schema mapping to create the tables
Base.metadata.create_all(engine)

# Creation of categories
i=0
categories = json.load(open("categories.json"))
for elmt in categories["tags"]:
    category = Category(elmt["name"])
    # Add the modification in database
    session.add(category)
    i += 1
    if i == 1:
        break

category1 = json.load(open("category1.json"))
for elmt in category1["products"]:
    product = Product(elmt["product_name"], category)
    # Add the modification in database
    session.add(category)

#Save the modifications
session.commit()
# Close the session
session.close()

# i=0
# compter = json.load(open("categories.json"))
# for elmt in compter["tags"]:
#     if elmt["products"] < 100 and elmt["products"] > 90:
#         print(elmt["name"])
#         i += 1
# print(i)

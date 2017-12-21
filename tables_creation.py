#! /usr/bin/env python3
# coding: utf-8

"""
This file create the tables of the database with the ORM SQLAlchemy
"""

import json

from database import engine, Base, Session, Category


# Creation of a session to commnicate with the database
session = Session()
# Schema mapping to create the tables
Base.metadata.create_all(engine)

# Creation of categories
i = 0
for cat in json.load(open('categories.json')):
    category = Category(cat['category'])
    # Add the modification in database
    session.add(category)
    i += 1
    if i == 2:
        break

session.commit()
session.close()

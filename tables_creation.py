#! /usr/bin/env python3
# coding: utf-8

"""
This file create the tables of the database with the ORM SQLAlchemy
"""

from database import engine, Base, Session, Category


# Creation of a session to commnicate with the database
session = Session()
# Schema mapping to create the tables
Base.metadata.create_all(engine)

# Creation of categories
category_fruits = Category("Fruits", "Que des bons fruits")
category_biscuits = Category("biscuits", "Tous ce qui est sucré et qui croustille")

# Add the modification in database
session.add(category_fruits)
session.add(category_biscuits)
session.commit()
session.close()

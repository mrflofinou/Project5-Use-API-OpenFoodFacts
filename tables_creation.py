#! /usr/bin/env python3
# coding: utf-8

"""
This file creates the tables of the database with the ORM SQLAlchemy
"""

import requests
from sqlalchemy.sql.expression import insert

from database import Category, Product
from base import Base, Session, engine
from settings import categories_limit as limit


# Creation of a session to commnicate with the database
session = Session()
# Schema mapping to create the tables
Base.metadata.create_all(engine)

def get_from_api(url):
    """
    Function to get data from the API
    """
    # Make GET request to the API
    resp = requests.get(url+".json")
    data = resp.json()
    return data

def insert_in_database(elmt, Product, category):
    """
    Function to insert values in the database
    """
    for j in range(1, 6):
        products = get_from_api(elmt["url"]+"/{}".format(j))
        for elemt in products["products"]:
            # Insert data in database
            product = insert(Product).prefix_with("IGNORE")
            product_values = {
            'name': elemt.get("product_name", "'Pas de nom renseigné'"),
            'id': elemt["_id"],
            'id_category': category.id,
            'store': elemt.get("stores",""),
            'nutriscore': elemt.get("nutrition_grade_fr", "e"),
            'url': elemt["url"]
            }
            session.execute(product, product_values)
            #Save the modifications in data base
            session.commit()

# I select all of the categories in the database
categories_list = session.query(Category).all()
# get the categories with the API
categories = get_from_api("https://fr.openfoodfacts.org/categories")
# I verify if there are 30 categories
if len(categories_list) < limit:
    for elmt in categories["tags"]:
        if elmt["products"] < 2000:
            categories = insert(Category).prefix_with("IGNORE")
            cat_values = {'name': elmt["name"]}
            session.execute(categories, cat_values)
            # Save the modifications in data base
            session.commit()
            # this request will allow to select the id of the category for the products
            category = session.query(Category).filter(Category.name == elmt["name"]).one()
            # I select all of the categories in the database to know its length
            categories_length = session.query(Category).all()
            # Get products from page 1 to page 5
            insert_in_database(elmt, Product, category)
            # I want insert 30 categories
            if len(categories_length) == limit:
                break
# If there are 30 categories in the database, we update with new products
else:
    # I save the names of the categories in a list
    categories_names = [category.name for category in categories_list]
    for elmt in categories["tags"]:
        if elmt["name"] in categories_names:
            category = session.query(Category).filter(Category.name == elmt["name"]).one()
            insert_in_database(elmt, Product, category)

# Close the session
session.close()

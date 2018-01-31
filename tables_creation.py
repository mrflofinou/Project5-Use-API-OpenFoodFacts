#! /usr/bin/env python3
# coding: utf-8

"""
This file creates the tables of the database with the ORM SQLAlchemy
"""

import json
import requests
from sqlalchemy.sql.expression import insert

from database import Category, Product
from base import Base, Session, engine


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

categories = get_from_api("https://fr.openfoodfacts.org/categories")
i = 0;
for elmt in categories["tags"]:
    # No nutrition grades for beers and wines
    if elmt["products"] < 2000:
        categories = insert(Category).prefix_with("IGNORE")
        cat_values = {'name': elmt["name"]}
        session.execute(categories, cat_values)
        i += 1
        # Get products from page 1 to page 5
        for j in range(1, 6):
            products = get_from_api(elmt["url"]+"/{}".format(j))
            for elemt in products["products"]:
                # Insert data in database
                product = insert(Product).prefix_with("IGNORE")
                product_values = {
                'name': elemt["product_name"],
                'id_product': elemt["_id"],
                'id_category': i,
                'store': elemt.get("stores"),
                'nutriscore': elemt.get("nutrition_grade_fr", "e"),
                'url': elemt["url"]
                }
                session.execute(product, product_values)
                # session.add(product)
        if i == 30:
            break

#Save the modifications in data base
session.commit()
# Close the session
session.close()

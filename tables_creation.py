#! /usr/bin/env python3
# coding: utf-8

"""
This file creates the tables of the database with the ORM SQLAlchemy
"""

import json
import requests

from database import Category, Product
from base import Base, Session, engine


# Creation of a session to commnicate with the database
session = Session()
# Schema mapping to create the tables
Base.metadata.create_all(engine)

# Make GET request to the API
resp = requests.get('https://fr.openfoodfacts.org/categories.json')
data = resp.json()
# Save the JSON data in a file
with open("JSON_files/categories.json", "w") as categories:
    json.dump(data, categories, ensure_ascii=False, indent=4, sort_keys=True)

# Creation of categories
categories = json.load(open("JSON_files/categories.json"))
for elmt in categories["tags"]:
    if elmt["products"] < 20000 and elmt["products"] > 2000:
        category = Category(elmt["name"])
        # Add the modification in database
        session.add(category)
        # Creation of products for each category
        response = requests.get(elmt["url"]+".json")
        # Problem with the category 'jus et nectar de fruits'
        # This try - except block is a temparory patch
        try:
            data_prod = response.json()
        except:
            continue
        product_file = elmt["url"].replace('https://fr.openfoodfacts.org/categorie/','')
        # Save the JSON data in a file
        with open("JSON_files/{}.json".format(product_file), "w") as products:
            json.dump(data_prod, products, ensure_ascii=False, indent=4, sort_keys=True)
        products = json.load(open("JSON_files/{}.json".format(product_file)))
        for elemt in products["products"]:
            product = Product(name=elemt["product_name"], category=category, url=elemt["url"])#, ingredients=elmt["ingredients_text_fr"], store=elmt["stores"])
            # Add the modification in database
            session.add(product)

#Save the modifications
session.commit()
# Close the session
session.close()

# i=0
# compter = json.load(open("JSON_files/categories.json"))
# for elmt in compter["tags"]:
#     if elmt["products"] < 20000 and elmt["products"] > 2000:
#         print(elmt["name"])
#         i += 1
# print(i)

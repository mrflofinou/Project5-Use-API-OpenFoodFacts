#! /usr/bin/env python3
# coding: utf-8

"""
This file creates the tables of the database with the ORM SQLAlchemy
"""

import json
import requests
import re
from sqlalchemy.exc import IntegrityError

from database import Category, Product
from base import Base, Session, engine


# Creation of a session to commnicate with the database
session = Session()
# Schema mapping to create the tables
Base.metadata.create_all(engine)

def get_from_api(url):
    # Make GET request to the API
    resp = requests.get((url+".json"))
    data = resp.json()
    # Use regular expression to take the end of the url to name the file
    file_name = re.search("^.+/(.+)", url)
    # Save the JSON data in a file
    with open("JSON_files/{}.json".format(file_name.group(1)), "w") as values: #group of regular expression
        json.dump(data, values, ensure_ascii=False, indent=4, sort_keys=True)
    # Creation of the dictionnary from the JSON file
    values = json.load(open("JSON_files/{}.json".format(file_name.group(1)))) #group of regular expression
    return values

categories = get_from_api("https://fr.openfoodfacts.org/categories")
i = 0;
for elmt in categories["tags"]:
    if elmt["products"] <= 2000:
        session.begin_nested() # establish a savepoint of the session
        try:
            category = Category(elmt["name"])
            # Add the modification in data base
            session.add(category)
            session.flush()
        except IntegrityError:
            session.rollback()
        i += 1
        products = get_from_api(elmt["url"])
        for elemt in products["products"]:
            session.begin_nested() # establish a savepoint of the session
            try:
                product = Product(name=elemt["product_name"], category=category, url=elemt["url"])#, magasin=elemt["stores"])
                # Add the modification in database
                session.add(product)
                session.flush()
            except IntegrityError:
                session.rollback()
        if i == 30:
            break

#Save the modifications in data base
session.commit()
# Close the session
session.close()

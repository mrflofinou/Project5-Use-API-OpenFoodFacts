#! /usr/bin/env python3
# coding: utf-8

"""
This file allows to make the differents requests to the API of Open Food Facts
"""

import json
import requests

# Make GET request to the API
resp = requests.get('https://fr.openfoodfacts.org/categories.json')
data = resp.json()
print(resp.status_code)

# Save the JSON data in a file
with open("categories.json", "w") as categories:
    json.dump(data, categories, ensure_ascii=False, indent=4, sort_keys=True)

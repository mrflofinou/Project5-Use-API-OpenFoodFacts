#! /usr/bin/env python3
# coding: utf-8

"""
Project 5 of Python web developer course of OpenClassrooms
This program allows to choose a food product in a database to find a
subsitute.
With this program you can save a pruduct and his substitue.
"""

from base import Session
from database import Category, Product


def main():
    session = Session()
    # To manage the home loop
    home = True
    # To manage the product loop
    product = False
    while home:
        # Choose a category
        print("\nVeuillez taper le chiffre correspodant à votre choix:\n")
        print("1 - Quel aliment souhaitez-vous remplacer ?")
        print("2 - Retrouver mes aliments substitués.")
        # This try-except block check the input is an integer
        try:
            home_choice = int(input("\nEntrez votre choix ici : "))
        except ValueError:
            print("\nVotre saisie est incorrect\n")
            continue
        # To make a SELECT query in the table categories
        # categories is a list wich contains objects of the table category
        categories = session.query(Category).all()
        # Display the categories
        if home_choice == 1:
            print("\nVeuillez selectionner une catégorie:")
            print("\n----Catégories----\n")
            for category in categories:
                print("{:02d} | {}".format(category.id, category.name))
            # To out of the home loop
            home = False
            # To in in the product loop
            product = True
        # Display the saved products
        elif home_choice == 2:
            print("\n---- SECTION EN COURS DE DEVELOPPEMENT ----\n")
        else:
            print("Votre choix ne correspond pas à ceux proposés\n")

    # Loop to manage the products
    while product:
        try:
            product_choice = int(input("\nEntrez votre choix ici : "))
        except ValueError:
            print("\nVotre saisie est incorrect\n")
            continue
        # To make a JOIN query
        products = session.query(Product) \
            .join(Category) \
            .filter(Category.id == product_choice) \
            .all()
        # To display the name of the category
        # I use categories list
        # This list contains the objects of the table categories
        # I can call one of them and choose a column with '.name' for example
        print("\n---- {} ----\n".format(categories[product_choice - 1].name))
        for prod in products:
            print("{:03d} | {}".format(prod.id, prod.name))
        product = False


if __name__ == "__main__":
    main()

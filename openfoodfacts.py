#! /usr/bin/env python3
# coding: utf-8

"""
Project 5 of Python web developer course of OpenClassrooms
This program allows to choose a food product in a database to find a
subsitute.
With this program you can save a pruduct and his substitue.
"""

import os

from base import Session
from database import Category, Product


session = Session()

def main():
    # Main loop
    application = True
    # To manage the home loop
    home = True
    # To manage the category loop
    category = False
    # To manage the display of the details of a product loop
    product = False
    save = False
    while application:
        while home:
            os.system('cls' if os.name=='nt' else 'clear') # To clear the terminal
            print("\n")
            print("\t########################")
            print("\t#                      #")
            print("\t#### MENU PRINCIPAL ####")
            print("\t#                      #")
            print("\t########################")
            # Choose a category
            print("\nVeuillez taper le chiffre correspodant à votre choix:\n")
            print("1 - Quel aliment souhaitez-vous remplacer ?")
            print("2 - Retrouver mes aliments substitués.")
            print("3 - Quitter")
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
                # id_cat will allows to check the input for to choose a category
                id_cat = []
                for category in categories:
                    id_cat.append(category.id)
                    print("{:02d} | {}".format(category.id, category.name))
                # To out of the home loop
                home = False
                # To in in the product loop
                category = True
            # Display the saved products
            elif home_choice == 2:
                print("\n---- SECTION EN COURS DE DEVELOPPEMENT ----\n")
            elif home_choice == 3:
                home = False
                application = False
            else:
                print("Votre choix ne correspond pas à ceux proposés\n")

        # Loop to manage the products
        while category:
            try:
                category_choice = int(input("\nEntrez votre choix ici : "))
            except ValueError:
                print("\nVotre saisie est incorrect\n")
                continue
            if category_choice in id_cat:
                # To make a JOIN query
                products = session.query(Product) \
                    .join(Category) \
                    .filter(Category.id == category_choice) \
                    .all()
                # To display the name of the category
                # I use categories list
                # This list contains the objects of the table categories
                # I can call one of them and choose a column with '.name' for example
                print("\n---- {} ----\n".format(categories[category_choice - 1].name))
                # id_cat will allows to check the input for to choose a product
                id_prod = []
                for prod in products:
                    id_prod.append(prod.id)
                    print("{:03d} | {:100s} | Nutriscrore: {}".format(prod.id, prod.name, prod.nutriscore))
                category = False
                product = True
            else:
                print("\nVotre choix ne correspond pas à ceux proposés\n")

        # Loop to display the product
        while product:
            try:
                product_choice = int(input("\nEntrez votre choix ici : "))
            except ValueError:
                print("\nVotre saisie est incorrect\n")
                continue
            if product_choice in id_prod:
                product_chosen = session.query(Product) \
                    .filter(Product.id == product_choice) \
                    .all()
                for elmt in product_chosen:
                    print("\nVoici un subsitut pour le produit: {}".format(elmt.name))
                    print("{} | {} | {}".format(elmt.name, elmt.store, elmt.url))
                print("\nQue souhaitez-vous faire ?")
                print("1 - Sauvegarder votre choix (retour automatique au menu principal) ")
                print("2 - Retourner au menu principal (sans sauvegarder)")
                print("3 - Quitter sans sauvegarder")
                product = False
                save = True
            else:
                print("\nVotre choix ne correspond pas à ceux proposés\n")

        while save:
            try:
                choix = int(input("\nEntrez votre choix ici : "))
            except ValueError:
                print("\nVotre saisie est incorrect\n")
                continue
            if choix == 1:
                print("\n---- SECTION EN COURS DE DEVELOPPEMENT ----\n")
                save = False
                home = True
            elif choix == 2:
                save = False
                home = True
            elif choix == 3:
                save = False
                application = False
            else:
                print("\nVotre choix ne correspond pas à ceux proposés\n")

if __name__ == "__main__":
    main()
    session.close()

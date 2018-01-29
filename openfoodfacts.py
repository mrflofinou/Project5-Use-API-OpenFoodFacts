#! /usr/bin/env python3
# coding: utf-8

"""
Project 5 of Python web developer course of OpenClassrooms
This program allows to choose a food product in a database to find a
subsitute.
With this program you can save a pruduct and his substitute.
"""

import os
from operator import attrgetter

from base import Session
from database import Category, Product, Substitute


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
    # To manage the save of the substitute
    save = False
    while application:
        while home:
            os.system('cls' if os.name == 'nt' else 'clear') # To clear the terminal
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
            categories = session.query(Category).all() # categories is a list wich contains objects of the table category
            # Display the categories
            if home_choice == 1:
                print("\nVeuillez selectionner une catégorie:")
                print("\n----Catégories----\n")
                # id_cat will allows to check the input to choose a category
                id_cat = []
                for category in categories:
                    id_cat.append(category.id)
                    # To display the categories
                    print("{:02d} | {}".format(category.id, category.name))
                # To out of the home loop
                home = False
                # To in in the product loop
                category = True
            # Display the saved products
            elif home_choice == 2:
                substitutes = session.query(Substitute).all()
                for substit in substitutes:
                    # To display the saved substitutes
                    print("{:02d} | {:50s} | {:10s} | {}".format(substit.id, substit.name, substit.store, substit.url))
                home_menu = input("\nAppuyez sur Entrée pour retourner au menu principal: ")
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
            if category_choice in id_cat: # To verify the user input is in the list of categories
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
                # id_prod will allows to check the input for to choose a product
                id_prod = []
                for prod in products:
                    id_prod.append(prod.id)
                    # To display the products of the chosen category
                    print("{:03d} | {:100s} | Nutriscrore: {}".format(prod.id, prod.name, prod.nutriscore))
                # To out of category loop
                category = False
                # To in in the product loop
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
            # To choose a product
            if product_choice in id_prod: # To verify the user input is in the list of products
                product_chosen = session.query(Product) \
                    .filter(Product.id == product_choice) \
                    .all()
                # To find a substitute
                for elmt in product_chosen:
                    prod_chosen = elmt
                    # if elmt.nutriscore == "a":
                    #     print("L'aliment que vous avez choisi a un nutriscore 'A'. Il n'y a donc pas de substitut correspondant à cet aliment")
                    # else :
                    #     # I sort the products according to their 'nutriscore' and i choose the first five
                    substitutes_list = sorted(products, key=attrgetter("nutriscore"))
                    print("\nVoici une liste de cinq substituts ayant un meilleur nutriscore que: {}".format(elmt.name))
                    for i in range(0, 5):
                        # The substitutes don't must be the chosen product and must have a lower 'nutriscore'
                        if substitutes_list[i].id_product != prod_chosen.id_product or substitutes_list[i].nutriscore <= prod_chosen.nutriscore:
                            # Display the substitutes
                            print("\n{}:\nProduit: {} \nMagasin: {} \nNutriscore: {} \nUrl: {}".format(i+1, substitutes_list[i].name, substitutes_list[i].store, substitutes_list[i].nutriscore, substitutes_list[i].url))
                product = False
                save = True
            else:
                print("\nVotre choix ne correspond pas à ceux proposés\n")

        # Loop to save the choice
        while save:
            print("\n\nQue souhaitez-vous faire ?")
            print("1 - Sauvegarder votre choix")
            print("2 - Retourner au menu principal (sans sauvegarder)")
            print("3 - Quitter sans sauvegarder")
            try:
                save_choice = int(input("\nEntrez votre choix ici: "))
            except ValueError:
                print("\nVotre saisie est incorrect\n")
                continue
            # To save the substitutes
            if save_choice == 1:
                print("\nVous souhaitez:")
                print("1 - Sauvegarder les 5 substituts")
                print("2 - Sauvegarder un seul substitut")
                check = True
                while check:
                    try:
                        save_mode = int(input("\nEntrez votre choix ici: "))
                    except ValueError:
                        print("\nVotre saisie est incorrect\n")
                        continue
                    # To save the 5 substitutes
                    if save_mode == 1:
                        for i in range(0, 5):
                            sub = Substitute(name=substitutes_list[i].name, substitute=substitutes_list[i].id_product, product=prod_chosen.id_product, store=substitutes_list[i].store, url=substitutes_list[i].url)
                            session.add(sub)
                        session.commit()
                        check = False
                    # To save a chosen substitute
                    elif save_mode == 2:
                        check_save = True
                        while check_save:
                            try:
                                save_substitute = int(input("\nVeuillez choisir le substitut que vous souhaitez enregistrer: "))
                            except ValueError:
                                print("\nVotre saisie est incorrect\n")
                                continue
                            sub = Substitute(name=substitutes_list[save_substitute - 1].name, substitute=substitutes_list[save_substitute - 1].id_product, product=prod_chosen.id_product, store=substitutes_list[save_substitute - 1].store, url=substitutes_list[save_substitute - 1].url)
                            session.add(sub)
                            session.commit()
                            check_save = False
                            check = False
                    else:
                        print("\nVotre choix ne correspond pas à ceux proposés\n")
                save = False
                home = True
            elif save_choice == 2:
                save = False
                home = True
            elif save_choice == 3:
                save = False
                application = False
            else:
                print("\nVotre choix ne correspond pas à ceux proposés\n")

if __name__ == "__main__":
    main()
    session.close()

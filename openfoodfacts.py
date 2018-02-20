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
            categories = session.query(Category).order_by(Category.id).all() # categories is a list wich contains objects of the table category
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
                id_sub = []
                for substit in substitutes:
                    # To display the saved substitutes
                    print("{:02d} | {:50s} | {:10s} | {}".format(substit.id, substit.name, substit.store, substit.url))
                    id_sub.append(substit.id)
                print("\nQue souhaitez-vous faire ?")
                print("1 - Retourner au menu principal")
                print("2 - Supprimer un substitut")
                substitute_save = True
                while substitute_save:
                    try:
                        home_substitutes = int(input("\nEntrez votre choix: "))
                    except ValueError:
                        print("\nVotre saisie est incorrect\n")
                        continue
                    if home_substitutes == 1:
                        substitute_save = False
                    # To delete a substitute form the database
                    elif home_substitutes == 2:
                        if len(id_sub) == 0:
                            print("Il n'y a aucun substitut d'enregistré")
                            delete_substitute = False
                        else:
                            delete_substitute = True
                        while delete_substitute:
                            try:
                                delete_id = int(input("Veuiller entrer le numéro d'identifiant du substitut à supprimer: "))
                            except ValueError:
                                print("\nVotre saisie est incorrect\n")
                                continue
                            if delete_id in id_sub:
                                delete_sub = session.query(Substitute).filter(Substitute.id == delete_id).one()
                                session.delete(delete_sub)
                                session.commit()
                                delete_substitute = False
                                substitute_save = False
                            else:
                                print("\nL'identifiant choisi n'existe pas.")
                    else:
                        print("Votre choix ne correspond pas à ceux proposés\n")
            elif home_choice == 3:
                home = False
                application = False
                os.system('cls' if os.name == 'nt' else 'clear') # To clear the terminal
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
                    .order_by(Product.id) \
                    .all()
                if len(products) == 0:
                    print("Cette catégorie est vide")
                    continue
                # To display the name of the category
                # I use categories list
                # This list contains the objects of the table categories
                # I can call one of them and choose a column with '.name' for example
                print("\n---- {} ----\n".format(categories[category_choice - 1].name))
                # id_prod will allows to check the input for to choose a product
                id_prod = []
                i = 1
                for prod in products:
                    id_prod.append(i)
                    # To display the products of the chosen category
                    print("{:03d} | {:100s} | Nutriscrore: {}".format(i, prod.name, prod.nutriscore))
                    i += 1
                # To out of category loop
                category = False
                # To in in the product loop
                product = True
            else:
                print("\nVotre choix ne correspond pas à ceux proposés\n")

        # Loop to display the substitute of the product chosen
        while product:
            try:
                product_choice = int(input("\nEntrez votre choix ici : "))
            except ValueError:
                print("\nVotre saisie est incorrect\n")
                continue
            # To choose a product
            if product_choice in id_prod: # To verify the user input is in the list of products
                product_chosen = products[product_choice - 1]
                # I sort the products according to their 'nutriscore' and i choose the first five
                substitutes_list = sorted(products, key=attrgetter("nutriscore"))
                print("\nVoici une liste de substituts ayant un meilleur nutriscore que: {}".format(product_chosen.name))
                substitutes_choice = []
                # if there are more of 5 products
                if len(substitutes_list) > 5:
                    h = 0
                    g = 0
                    while h != 5:
                        # The substitutes don't must be the chosen product
                        if substitutes_list[g].id != product_chosen.id:
                            # Display the substitutes
                            print("\n{}:\nProduit: {} \nMagasin: {} \nNutriscore: {} \nUrl: {}".format(h+1,
                                                                                                substitutes_list[g].name,
                                                                                                substitutes_list[g].store,
                                                                                                substitutes_list[g].nutriscore,
                                                                                                substitutes_list[g].url)
                                                                                                )
                            # I save the 5 substitutes in a list with the goal the user will can choose to save one of them.
                            substitutes_choice.append(substitutes_list[g])
                            h += 1
                            g += 1
                        else:
                            g += 1
                else:
                    for i,prod in enumerate(substitutes_list):
                        # Display the substitutes
                        print("\n{}:\nProduit: {} \nMagasin: {} \nNutriscore: {} \nUrl: {}".format(i+1,
                                                                                            substitutes_list[i].name,
                                                                                            substitutes_list[i].store,
                                                                                            substitutes_list[i].nutriscore,
                                                                                            substitutes_list[i].url)
                                                                                            )
                        # I save the substitutes in a list with the goal the user will can choose to save one of them
                        substitutes_choice.append(substitutes_list[i])
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
                check = True
                while check:
                    # To save a chosen substitute
                    try:
                        save_substitute = int(input("\nVeuillez choisir le substitut que vous souhaitez enregistrer: "))
                    except ValueError:
                        print("\nVotre saisie est incorrect\n")
                        continue
                    if substitutes_choice[save_substitute - 1].store == "NULL":
                        sub = Substitute(
                        name = substitutes_choice[save_substitute - 1].name,
                        store = "",
                        url = substitutes_choice[save_substitute - 1].url
                        )
                    else:
                        sub = Substitute(
                        name = substitutes_choice[save_substitute - 1].name,
                        store = substitutes_choice[save_substitute - 1].store,
                        url = substitutes_choice[save_substitute - 1].url
                        )
                    session.add(sub)
                    session.commit()
                    check = False
                save = False
                home = True
            elif save_choice == 2:
                save = False
                home = True
            elif save_choice == 3:
                save = False
                application = False
                os.system('cls' if os.name == 'nt' else 'clear') # To clear the terminal
            else:
                print("\nVotre choix ne correspond pas à ceux proposés\n")

if __name__ == "__main__":
    session = Session()
    main()
    session.close()

#! /usr/bin/env python3
# coding: utf-8

"""
Project 5 of Python web developer course of OpenClassrooms
This program allows to choose a food product in a database to find a
subsitute.
With this program you can save a pruduct and his substitue.
"""

from base import Session
from database import Category


def main():
    session = Session()
    # To make a SELECT query
    categories = session.query(Category).all()
    loop = True
    while loop:
        # Choose a category
        print("\nVeuillez choisir le chiffre correspodant à votre choix:\n")
        print("1 - Catégories")
        print("2 - Aliments enregistrés")
        # This try-except block check the input is an integer
        try:
            home_choice = int(input("\nQue voulez-vous faire ? "))
            # Display the categories
            if home_choice == 1:
                print("Vous voulez afficher les catégories d'aliments")
                print('\n----Catégories----')
                for category in categories:
                    print("{:02d} | {}".format(category.id, category.name))
                print('\n')
                loop = False
            # Display the saved products
            elif home_choice == 2:
                print("\n---- SECTION EN COURS DE DEVELOPPEMENT ----\n")
            else:
                print("Votre choix ne correspond pas à ceux proposés\n")
        except:
            print("\nVotre saisie est incorrect\n")

if __name__ == "__main__":
    main()

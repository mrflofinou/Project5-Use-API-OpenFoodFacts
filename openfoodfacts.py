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
    categories = session.query(Category).all()
    # Choose a category
    print("\nTapez le chiffre correspodant à votre choix:")
    print("\n1 - Catégories")
    print("2 - Aliments enregistrés")
    home_choice = int(input("\nQue voulez-vous faire ? "))
    if home_choice == 1:
        print("Vous voulez afficher les catégories des aliments")
        print('\n----Catégories----')
        for category in categories:
            print("{:02d} | {}".format(category.id, category.name))
        print('\n')



if __name__ == "__main__":
    main()

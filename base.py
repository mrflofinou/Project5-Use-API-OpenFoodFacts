#! /usr/bin/env python3
# coding: utf-8

"""
This file creates the 'link' between the database and our program
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import settings as s

# Creation of engine with our database (here mysql) and the DBAPI (here pymysql)
# DON'T FORGET THE CHARSET UTF8 !
engine = create_engine('mysql+pymysql://{}:{}@localhost/test_projet05?charset=utf8'.format(s.username, s.password))
Session = sessionmaker(bind=engine)

Base = declarative_base()

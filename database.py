#! /usr/bin/env python3
# coding: utf-8

from sqlalchemy import create_engine, Column, Integer, String, Index, Text
from sqlalchemy.ext.declarative import declarative_base

import settings as s
#from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+pymysql://s.username:s.password@localhost/test_projet05')
#Session = sessionmaker(bind=engine)
Base = declarative_base()

class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    name = Column(String(150), nullable=False)
    description = Column(Text)

#!/usr/bin/env python3
# this module creates the database for the item-catalog project
import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
#from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    picture = Column(String(250))


class Category(Base):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    creator_id = Column(Integer, ForeignKey('user.id'))
    creator = relationship(User)


class Item(Base):
    __tablename__ = 'item'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    specific_information = Column(String(2000))
    category_name = Column(String(100), ForeignKey('category.name'))
    category = relationship(Category)
    creator_id = Column(Integer, ForeignKey('user.id'))
    creator = relationship(User)


engine = create_engine('sqlite:///itemcatalog.db')
Base.metadata.create_all(engine)

#make a session and populate the db with default content
Session = sessionmaker(bind=engine)
session = Session()

defaultuser = User(
    name='John Doe',
    email='Johndoe@gmail.com',
    #picture='https://img.com/sdf'
)

session.add(defaultuser)

defaultcategory = Category(
    name='Miscellaneous',
    creator=defaultuser
)
session.add(defaultcategory)

defaultitem = Item(
    name='ExampleItem',
    specific_information='This is an item you can do wonderful things with.',
    category=defaultcategory,
    creator=defaultuser
)

session.add(defaultitem)
session.commit()

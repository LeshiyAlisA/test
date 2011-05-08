__author__ = 'leshiy'
#-*- coding: utf-8 -*-

import forex
import pymongo
from pymongo import Connection

connection=Connection("localhost",27017)
db=connection.db
collection=db.test_collection
post={"id":"id"}






vs=forex.WebService()



  
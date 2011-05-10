__author__ = 'leshiy'
#-*- coding: utf-8 -*-

import forex
from pymongo import Connection
import sys

connection=Connection("localhost",27017)
db=connection.db
rates=db.rates

vs=forex.WebService()
key=vs.GetRatesServerAuth(sys.argv[1],sys.argv[2],sys.argv[3])

while 1==1:
    Rates=vs.GetRatesDataSet(key)
    for i in Rates:
        rates.save(i)




  
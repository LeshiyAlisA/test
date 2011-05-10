__author__ = 'leshiy'
#-*- coding: utf-8 -*-

import forex
from pymongo import Connection
import sys
import pickle
connection=Connection("localhost",27017)
db=connection.db
rates=db.rates

vs=forex.WebService()
f = open('/home/leshiy/str.txt', 'rb+')
y=pickle.load(f)
key=vs.GetRatesServerAuth(y[0],y[1],y[2])

while 1==1:
    Rates=vs.GetRatesDataSet(key)
    for i in Rates:
        rates.save(i)
        print rates.count()




  
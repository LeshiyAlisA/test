__author__ = 'leshiy'
#-*- coding: utf-8 -*-

import forex
from pymongo import Connection
import sys
import pickle

class main:

    def analiz(self,Rate):

        print Rate

    def test(self):

        vs=forex.WebService()
        f = open('/home/leshiy/str.txt', 'rb+')
        y=pickle.load(f)
        key=vs.GetRatesServerAuth(y[0],y[1],y[2])

        while 1==1:
            Rates=vs.GetRatesDataSet(key)
            if Rates!=0:
                for i in Rates:
                    if i["Quote"]=="EUR/USD":
                        self.analiz(i)



    def test2(self):

        #connection=Connection("localhost",27017)

        #db=connection.db
        #rates=db.rates

        vs=forex.WebService()
        f = open('/home/leshiy/str.txt', 'rb+')
        y=pickle.load(f)
        key=vs.GetRatesServerAuth(y[0],y[1],y[2])

        while 1==1:
            Rates=vs.GetRatesBlotter(key)
            for i in Rates:
                #rates.save(i)
                #print rates.count()
                if i['PAIR']=='EUR/USD':
                    print i

        
vs=forex.WebService()
f = open('/home/leshiy/str.txt', 'rb+')
y=pickle.load(f)
key=vs.GetRatesServerAuth(y[0],y[1],y[2])
rates=vs.GetRatesBlotter(key)
for rate in rates:
    if rate['PAIR']=='EUR/USD':
        print rate['BID']
        order=vs.PlaceSingleOrder('delphi7@list.ru','forex123','EUR/USD', 'EOD','B','10000',rate['BID'],'S')
        for i in order:
            str=order[i]
            if str!=None:
                print i+':'+str
            else:
                print i+':None'


#print vs.PlaceSingleOrder('delphi7@list.ru','forex123','EUR/USD', 'EOD','B','10000',,'S')

#q=main()
#q.test2()

  




  
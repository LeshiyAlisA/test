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
#key=vs.GetRatesServerAuth(y[0],y[1],y[2])

tmarge=vs.GetMarginBlotterDataSet(y[0],y[1])
print tmarge['MarginBalance']
MarginBalance=tmarge['MarginBalance']
UnrealizedProfit=tmarge['UnrealizedProfit']
bal=float(MarginBalance)-float(UnrealizedProfit)
print "balance:"+str(bal)


print vs.DealRequestAtBest(y[0],y[1],'EUR/USD','B','100000')

tmarge=vs.GetMarginBlotterDataSet(y[0],y[1])
print tmarge['MarginBalance']
MarginBalance=tmarge['MarginBalance']
UnrealizedProfit=tmarge['UnrealizedProfit']
bal=float(MarginBalance)-float(UnrealizedProfit)

print "balance:"+str(bal)

#print vs.GetAccount(y[0],y[1],y[2])
#vs.GetMarginBlotterDataSet(y[0],y[1])


#print vs.PlaceSingleOrder('delphi7@list.ru','forex123','EUR/USD', 'EOD','B','10000',,'S')

#q=main()
#q.test2()

  




  
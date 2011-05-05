__author__ = 'leshiy'
#-*- coding: utf-8 -*-

import urllib
import sys
from lxml import etree

class WebService:
    def PlaceSingleOrder(self,UserID,PWD,Pair,Expiry,BuySell,Amount,Rate,OrderBasis):
        print "PlaceSingleOrder"




    def GetRatesDataSet(self,key):
        dataset=[]
        u = urllib.urlopen('http://api.efxnow.com/DEMOWebServices2.8/Service.asmx/GetRatesDataSet?Key='+key)
        root = etree.XML(u.read())
        rates=root.findall(".//Rates")

        for rate in rates:
            quote=[rate.find("Quote").text,rate.find("Display").text,rate.find("UpdateTime").text]
            dataset.append(quote)

        return dataset

            
        
    def GetRatesServerAuth(self,UserID,PWD,Brand):
        u = urllib.urlopen('http://api.efxnow.com/DEMOWebServices2.8/Service.asmx/GetRatesServerAuth?UserID='+UserID+'&PWD='+PWD+'&Brand='+Brand)
        root = etree.XML(u.read())
        return root.text


ws=WebService()
key= ws.GetRatesServerAuth(sys.argv[1],sys.argv[2],sys.argv[3])
ds=ws.GetRatesDataSet(key)
print key
for i in ds:
    for j in i:
        print j



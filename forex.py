__author__ = 'leshiy'
#-*- coding: utf-8 -*-

import urllib
import sys
from lxml import etree
import re
import string

class WebService:
    def PlaceSingleOrder(self,UserID,PWD,Pair,Expiry,BuySell,Amount,Rate,OrderBasis):
        print "PlaceSingleOrder"

    def GetRatesDataSet(self,key):
        dataset=[]
        try:
            u = urllib.urlopen('http://api.efxnow.com/DEMOWebServices2.8/Service.asmx/GetRatesDataSet?Key='+key)
            root = etree.XML(u.read())
            rates=root.findall(".//Rates")


            for rate in rates:
                quote={"Quote":rate.find("Quote").text,"Display":rate.find("Display").text,"UpdateTime":rate.find("UpdateTime").text}
                dataset.append(quote)

            return dataset

        except :
            return 0

    
        
    def GetRatesServerAuth(self,UserID,PWD,Brand):
        u = urllib.urlopen('http://api.efxnow.com/DEMOWebServices2.8/Service.asmx/GetRatesServerAuth?UserID='+UserID+'&PWD='+PWD+'&Brand='+Brand)
        root = etree.XML(u.read())
        return root.text

    def GetRatesBlotter(self,key):
        u = urllib.urlopen('http://api.efxnow.com/DEMOWebServices2.8/Service.asmx/GetRatesBlotter?Key='+key)
        root = etree.XML(u.read())
        str=root.text

        rates=[]
        
        str=string.split(str,"$")
        for i in str:
            j=string.split(i,"\\")
            if len(j)==11:
                rate={"PAIR":j[0],"BID":j[1],"OFFER":j[2],"STATUS":j[3],"HIGH":j[4],"LOW":j[5],
                      "DECIMALPLACES":j[6],"NOTATION":j[7],"CLOSINGBID":j[8],"COUNTERPAIR":j[9],"UPDATEDATETIME":j[10]}
                rates.append(rate)

        return rates

            




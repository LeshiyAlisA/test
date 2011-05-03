__author__ = 'leshiy'
#-*- coding: utf-8 -*-

import urllib
import sys
import html5lib
from html5lib import treebuilders
from lxml import etree






class WebService:
    def PlaceSingleOrder(self,UserID,PWD,Pair,Expiry,BuySell,Amount,Rate,OrderBasis):
        print "PlaceSingleOrder"

    def GetRatesDataSet(self,key):
        print "GetRates"
        print key
        u = urllib.urlopen('http://api.efxnow.com/DEMOWebServices2.8/Service.asmx/GetRatesDataSet?Key='+key)
        root = etree.XML(u.read())
        rates=root.findall(".//Rates")
        for rate in rates:
            print "Quote: " + rate.find("Quote").text
            print "Display: "+rate.find("Display").text
            print "UpdateTime: "+rate.find("UpdateTime").text

        
    def GetRatesServerAuth(self,UserID,PWD,Brand):
        u = urllib.urlopen('http://api.efxnow.com/DEMOWebServices2.8/Service.asmx/GetRatesServerAuth?UserID='+UserID+'&PWD='+PWD+'&Brand='+Brand)

        parser = html5lib.HTMLParser(tree=treebuilders.getTreeBuilder("dom"))
        doc = parser.parse(u)

        n=doc.getElementsByTagName("string")[0]       

        for nchild in n.childNodes:
            if nchild.nodeType==3:
                return nchild.data.strip()






ws=WebService()
key= ws.GetRatesServerAuth(sys.argv[1],sys.argv[2],sys.argv[3])
ws.GetRatesDataSet(key)



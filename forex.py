__author__ = 'leshiy'
#-*- coding: utf-8 -*-

import urllib
import sys
from lxml import etree
import re
import string
import html5lib
from html5lib import treebuilders
from xml.etree import cElementTree

class WebService:

    def DealRequestAtBest(self):
        return 0

    def GetAccount(self,UserID,PWD,Brand):
        u=urllib.urlopen('http://api.efxnow.com/DEMOWebServices2.8/Service.asmx/GetAccountDetails?UserID='+UserID+'&PWD='+PWD+'&Brand='+Brand+'&ApplicationName=&Language=')
        str=u.read()


        parser = html5lib.HTMLParser(tree=treebuilders.getTreeBuilder("lxml"))
        tree=parser.parse(str)
        temproot=tree.getroot()
        lstr=temproot.find('.//{http://www.w3.org/1999/xhtml}string')
        root=etree.XML(lstr.text)
        Account=root.find('.//Account')

        return {'LogonEnabled':Account.find('LogonEnabled').text,
                'LockoutDescription':Account.find('LockoutDescription').text,
                'CustCode':Account.find('CustCode').text,
                'GUID':Account.find('GUID').text,
                'Features':Account.find('Features').text,
                'BaseCCY':Account.find('BaseCCY').text,
                'LastOrderSEQ':Account.find('LastOrderSEQ').text,
                'LastDealSEQ':Account.find('LastDealSEQ').text,
                'OrderLotSize':Account.find('OrderLotSize').text,
                'MaxOrderPips':Account.find('MaxOrderPips').text,
                'CancelOrderPips':Account.find('CancelOrderPips').text,
                'TradeLotSize':Account.find('TradeLotSize').text,
                'MaxTradeLots':Account.find('MaxTradeLots').text,
                'TierCount':Account.find('TierCount').text,
                'Tier1MinLots':Account.find('Tier1MinLots').text,
                'Tier1MaxLots':Account.find('Tier1MaxLots').text,
                'Tier1PipDifference':Account.find('Tier1PipDifference').text,
                'Tier2MinLots':Account.find('Tier2MinLots').text,
                'Tier2MaxLots':Account.find('Tier2MaxLots').text,
                'Tier2PipDifference':Account.find('Tier2PipDifference').text,
                'Tier3MinLots':Account.find('Tier3MinLots').text,
                'Tier3MaxLots':Account.find('Tier3MaxLots').text,
                'Tier3PipDifference':Account.find('Tier3PipDifference').text,
                'NFARegulated':Account.find('NFARegulated').text}









    def PlaceSingleOrder(self,UserID,PWD,Pair,Expiry,BuySell,Amount,Rate,OrderBasis):
        u = urllib.urlopen('http://api.efxnow.com/DEMOWebServices2.8/Service.asmx/PlaceSingleOrder?UserID='+UserID+'&PWD='+PWD+'&Pair='+Pair+'&Expiry='+Expiry+'&BuySell='+BuySell+'&Amount='+Amount+'&Rate='+Rate+'&OrderBasis='+OrderBasis)
        root = etree.XML(u.read())
        return {'Success':root.find('{https://api.efxnow.com/webservices2.3}Success').text,
                'ErrorDescription':root.find('{https://api.efxnow.com/webservices2.3}ErrorDescription').text,
                'ErrorNumber':root.find('{https://api.efxnow.com/webservices2.3}ErrorNumber').text,
                'CustomerOrderReference':root.find('{https://api.efxnow.com/webservices2.3}CustomerOrderReference').text,
                'OrderConfirmation':root.find('{https://api.efxnow.com/webservices2.3}OrderConfirmation').text,
                'CustomerDealRef':root.find('{https://api.efxnow.com/webservices2.3}CustomerDealRef').text,}


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

            




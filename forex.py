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

    def GetMarginBlotterDataSet(self,UserID,PWD):
        u=urllib.urlopen('http://api.efxnow.com/DEMOWebServices2.8/Service.asmx/GetMarginBlotterDataSet?UserID='+UserID+'&PWD='+PWD)
        str=u.read()
        
        parser = html5lib.HTMLParser(tree=treebuilders.getTreeBuilder("lxml"))
        tree=parser.parse(str)
        root= tree.getroot()

        PostedMargin=root.find('.//{http://www.w3.org/1999/xhtml}postedmargin').text
        RealizedProfit=root.find('.//{http://www.w3.org/1999/xhtml}realizedprofit').text
        UnrealizedProfit=root.find('.//{http://www.w3.org/1999/xhtml}unrealizedprofit').text
        MarginFactor=root.find('.//{http://www.w3.org/1999/xhtml}marginfactor').text
        MarginBalance=root.find('.//{http://www.w3.org/1999/xhtml}marginbalance').text
        TotalAvailable=root.find('.//{http://www.w3.org/1999/xhtml}totalavailable').text
        OpenPosiiton=root.find('.//{http://www.w3.org/1999/xhtml}openposiiton').text
        MaxDeal=root.find('.//{http://www.w3.org/1999/xhtml}maxdeal').text
        USDPostedMargin=root.find('.//{http://www.w3.org/1999/xhtml}usdpostedmargin').text
        USDRealizedProfit=root.find('.//{http://www.w3.org/1999/xhtml}usdrealizedprofit').text

        return {'PostedMargin':PostedMargin,
                'RealizedProfit':RealizedProfit,
                'UnrealizedProfit':UnrealizedProfit,
                'MarginFactor':MarginFactor,
                'MarginBalance':MarginBalance,
                'TotalAvailable':TotalAvailable,
                'OpenPosiiton':OpenPosiiton,
                'MaxDeal':MaxDeal,
                'USDPostedMargin':USDPostedMargin,
                'USDRealizedProfit':USDRealizedProfit}



    def DealRequestAtBest(self,UserID,PWD,Pair,BuySell,Amount):

        u=urllib.urlopen('http://api.efxnow.com/DEMOWebServices2.8/Service.asmx/DealRequestAtBest?UserID='+UserID+'&PWD='+PWD+'&Pair='+Pair+'&BuySell='+BuySell+'&Amount='+Amount)
        str=u.read()

        parser = html5lib.HTMLParser(tree=treebuilders.getTreeBuilder("lxml"))
        tree=parser.parse(str)

        root=tree.getroot()
        success=root.find('.//{http://www.w3.org/1999/xhtml}success').text
        errordescription=root.find('.//{http://www.w3.org/1999/xhtml}errordescription').text
        errornumber=root.find('.//{http://www.w3.org/1999/xhtml}errornumber').text
        confirmation=root.find('.//{http://www.w3.org/1999/xhtml}confirmation').text

        return {'success':success,'errordescription':errordescription,'errornumber':errornumber,'confirmation':confirmation}


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
        str=u.read()

        parser = html5lib.HTMLParser(tree=treebuilders.getTreeBuilder("lxml"))
        tree=parser.parse(str)
        root=tree.getroot()

        return {'Success':root.find('.//{http://www.w3.org/1999/xhtml}success').text,
                'ErrorDescription':root.find('.//{http://www.w3.org/1999/xhtml}errordescription').text,
                'ErrorNumber':root.find('.//{http://www.w3.org/1999/xhtml}errornumber').text,
                'CustomerOrderReference':root.find('.//{http://www.w3.org/1999/xhtml}customerorderreference').text,
                'OrderConfirmation':root.find('.//{http://www.w3.org/1999/xhtml}orderconfirmation').text,
                'CustomerDealRef':root.find('.//{http://www.w3.org/1999/xhtml}customerdealref').text,}


    def GetRatesDataSet(self,key):

        u = urllib.urlopen('http://api.efxnow.com/DEMOWebServices2.8/Service.asmx/GetRatesDataSet?Key='+key)
        str=u.read()
        root = etree.XML(u.read())
            rates=root.findall(".//Rates")

            for rate in rates:
                quote={"Quote":rate.find("Quote").text,"Display":rate.find("Display").text,"UpdateTime":rate.find("UpdateTime").text}
                dataset.append(quote)

            return dataset


    
        
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

            




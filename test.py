__author__ = 'leshiy'
#-*- coding: utf-8 -*-

from forex import WebService
import unittest
import pickle

class TestWebService(unittest.TestCase):
    tlogin=''
    tpass=''
    tbrand=''

    def setUp(self):
        self.Webservice=WebService()
        f = open('/home/leshiy/str.txt', 'rb+')
        y=pickle.load(f)
        self.tlogin=y[0]
        self.tpass=y[1]
        self.tbrand=y[2]


    def testGetRatesServerAuth(self):
        str=self.Webservice.GetRatesServerAuth(self.tlogin,self.tpass,self.tbrand)
        self.assertEqual('859F296AEA2CF46F54FBFA3DDFD6B8CE',str)

    def testGetRatesBlotter(self):
        str=self.Webservice.GetRatesServerAuth(self.tlogin,self.tpass,self.tbrand)
        rates=self.Webservice.GetRatesBlotter(str)
        self.assertEquals(54,len(rates))

    def testGetRatesDataSet(self):
        str=self.Webservice.GetRatesServerAuth(self.tlogin,self.tpass,self.tbrand)
        rates=self.Webservice.GetRatesDataSet(str)
        self.assertEquals(54,len(rates))

    def testPlaceSingleOrder(self):
        str=self.Webservice.GetRatesServerAuth(self.tlogin,self.tpass,self.tbrand)
        order=self.Webservice.PlaceSingleOrder(self.tlogin,self.tpass,'EUR/USD', 'EOD','B','1','1','B')
        self.assertEqual('false',order['Success'])






def main():
    unittest.main()
    return  0

if __name__ == "__main__":
	unittest.main()
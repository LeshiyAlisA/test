__author__ = 'leshiy'
#-*- coding: utf-8 -*-

from forex import WebService
import unittest
import pickle

class TestWebService(unittest.TestCase):

    def setUp(self):
        self.Webservice=WebService()

    def testGetRatesServerAuth(self):
        f = open('/home/leshiy/str.txt', 'rb+')
        y=pickle.load(f)
        str=self.Webservice.GetRatesServerAuth(y[0],y[1],y[2])
        self.assertEqual('859F296AEA2CF46F54FBFA3DDFD6B8CE',str)


def main():
    unittest.main()
    return  0

if __name__ == "__main__":
	unittest.main()
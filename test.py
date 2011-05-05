__author__ = 'leshiy'
#-*- coding: utf-8 -*-

from main import WebService
import unittest
import sys

class TestWebService(unittest.TestCase):

    def setUp(self):
        self.Webservice=WebService()

    def testGetRatesServerAuth(self):
        str=self.Webservice.GetRatesServerAuth(sys.argv[1],sys.argv[2],sys.argv[3])
        self.assertEqual(str, 0)



if __name__ == "__main__":
	unittest.main()
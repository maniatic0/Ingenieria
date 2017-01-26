'''
Created on Jan 25, 2017

@author: christian
@author: alexander
'''
import unittest
from funcion import Tarifa, calcularPrecio
from datetime import datetime, timedelta

class Test(unittest.TestCase):
    tarifaPrueba = None

    def setUp(self):
        self.tarifaPrueba = Tarifa(1, 2)


    def tearDown(self):
        self.tarifaPrueba = None


    def testBasicoSemana(self):
        tiempo = [datetime(2017, 1, 25), datetime(2017, 1, 25) + timedelta(hours=1)]
        self.assertEqual(calcularPrecio(self.tarifaPrueba, tiempo), 1)
    
    def testBasicoFinDeSemana(self):
        tiempo = [datetime(2017, 1, 28), datetime(2017, 1, 28) + timedelta(hours=1)]
        self.assertEqual(calcularPrecio(self.tarifaPrueba, tiempo), 2)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
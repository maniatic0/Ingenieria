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
        
    def testExcepcionPasado(self):
        with self.assertRaises(Exception) as context:
            a = Tarifa(0,0)
            tiempo = [datetime(2017, 1, 28), datetime(2017, 1, 27)]
            calcularPrecio(a, tiempo)
        self.assertTrue('No puedes ir al pasado' in str(context.exception))
        
    def testExcepcionMinimo(self):
        with self.assertRaises(Exception) as context:
            a = Tarifa(0,0)
            tiempo = [datetime(2017, 1, 28), datetime(2017, 1, 28) + timedelta(minutes=14)]
            calcularPrecio(a, tiempo)
        self.assertTrue('No puede ser menor a 15 minutos' in str(context.exception))
    
    def testExcepcionMaximo(self):
        with self.assertRaises(Exception) as context:
            a = Tarifa(0,0)
            tiempo = [datetime(2017, 1, 28), datetime(2017, 2, 5)]
            calcularPrecio(a, tiempo)
        self.assertTrue('No puede ser mayor a 7 dias' in str(context.exception))
        
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
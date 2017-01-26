'''
Created on Jan 25, 2017

@author: christian
@author: alexander
'''
import unittest
from funcion import Tarifa, calcularPrecio
from datetime import datetime, timedelta
from _datetime import date

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
        
    def testBasico2Semana(self):
        tiempo = [datetime(2017, 1, 25), datetime(2017, 1, 25) + timedelta(hours=5, minutes=15)]
        self.assertEqual(calcularPrecio(self.tarifaPrueba, tiempo), 6)
        
    def testBasico2FinDeSemana(self):
        tiempo = [datetime(2017, 1, 28), datetime(2017, 1, 28) + timedelta(hours=3, minutes=1)]
        self.assertEqual(calcularPrecio(self.tarifaPrueba, tiempo), 4*2)
        
    def testPasoDeSemanaAFinDeSemana(self):
        tiempo = [datetime(2017, 1, 28) - timedelta(hours=2, minutes=15), datetime(2017, 1, 28) + timedelta(hours=3, minutes=1)]
        self.assertEqual(calcularPrecio(self.tarifaPrueba, tiempo), 3+4*2)
    
    def testPasoDeFinSemanaASemana(self):
        tiempo = [datetime(2017, 1, 30) - timedelta(hours=2, minutes=15), datetime(2017, 1, 30) + timedelta(hours=3, minutes=1)]
        self.assertEqual(calcularPrecio(self.tarifaPrueba, tiempo), (3*2)+4)
        
    def testSemanaCompleta(self):
        tiempo = [datetime(2017, 1, 23), datetime(2017, 1, 23) + timedelta(days=5, microseconds=-1)]
        self.assertEqual(calcularPrecio(self.tarifaPrueba, tiempo), 120)
        
    def testFinSemanaCompleto(self):
        tiempo = [datetime(2017, 1, 28), datetime(2017, 1, 28) + timedelta(days=2, microseconds=-1)]
        self.assertEqual(calcularPrecio(self.tarifaPrueba, tiempo), 48*2)
        
    def testSemanaASemanaDistinta(self):
        tiempo = [datetime(2017, 1, 27), datetime(2017, 1, 31) + timedelta(microseconds=-1)]
        self.assertEqual(calcularPrecio(self.tarifaPrueba, tiempo), 48*2 + 48)
        
    def testSieteDiaz(self):
        tiempo = [datetime(2017, 1, 27), datetime(2017, 1, 27) + timedelta(days=7, microseconds=-1)]
        self.assertEqual(calcularPrecio(self.tarifaPrueba, tiempo), 48*2 + 120)
    
    def testSieteDiazTerminandoEnFinDeSemana(self):
        tiempo = [datetime(2017, 1, 29), datetime(2017, 1, 29) + timedelta(days=7, microseconds=-1)]
        self.assertEqual(calcularPrecio(self.tarifaPrueba, tiempo), 48*2 + 120)
        
    def testMenosDeUnaHoraEntreFinDeSemanaYSemana(self):
        tiempo = [datetime(2017, 1, 30) + timedelta(minutes=-22), datetime(2017, 1, 30) + timedelta(minutes=6)]
        self.assertEqual(calcularPrecio(self.tarifaPrueba, tiempo), 1*2 + 1)
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
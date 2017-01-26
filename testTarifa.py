'''
Created on Jan 25, 2017

@author: alexander
'''
import unittest
from funcion import Tarifa

class Test(unittest.TestCase):
    
    def testTarifaExists(self):
        Tarifa(0,0)

    def testTarifaExistsSemana(self):
        t = Tarifa(1,0)
        self.assertEqual(t.getSemana()==1,True)
        
    def testTarifaExistsFinde(self):
        t = Tarifa(0,1)
        self.assertEqual(t.getFinde()==1, True)
        
    def testTarifaNoAceptaNegativos(self):
        with self.assertRaises(Exception) as context:
            Tarifa(-1,0)
        self.assertTrue('No existen las Tarifas Negativas' in str(context.exception))
        
    def testTarifaFloats(self):
        t = Tarifa(1.366,3.1416)
        self.assertEqual(t.getSemana()==1.366,True)
        self.assertEqual(t.getFinde()==3.1416,True)
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
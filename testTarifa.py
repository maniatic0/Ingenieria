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
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
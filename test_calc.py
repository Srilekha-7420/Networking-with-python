import calc
import unittest

class testCalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc.add(10,25),25)
        #self.assertEqual(calc.add(10,25),25.53)

if __name__=="__main__":
    unittest.main(verbosity=2)


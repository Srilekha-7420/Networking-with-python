from inherit import Product
import unittest
productObj=Product("milk",10,9,5)
class test_product:
    @classmethod
    def setUpClass(self):
        print("\nsetup")
    @classmethod
    def tearDownClass(self):
        print("\nteardown")
    def test_display_product_details(self):
        productObj.display_product_details()
        self.assertEqual(productObj.name,"milk")
if __name__=="__main__":
    unittest.main()



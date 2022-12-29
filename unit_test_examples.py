import unittest
class upper_class(unittest.TestCase):
    def test_upper(self):
        self.assertEqual('foo'.upper(),'FOO')

if __name__=="__main__":
    unittest.name()
############################################################
import unittest
class TestStringMethods(unittest.TestCase):
    def test_upper(self):
        self.assertEqual('foo'.upper(),'FOO')
    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())
    def test_split(self):
        s='hello world'
        self.assertEqual(s.split(),['hello','world'])
    #check the s.split fails when the seperator is not a string with
        self.assertRaises(TypeError)
        s.split(" ")
if __name__=="__main__":
    unittest.main()

#######################################################################
import unittest
class DefaultWidgetSizeTestCase(unittest.TestCase):
    def test_default_widget_size(self):
        widget=Widget("the widget")
        self.assertEqual(widget.size(),(50,50))
class MyTestCase(unittest.TestCase):
    @unittest.skip("demonstrating skipping")
    def test_nothing(self):
        self.fail("should not happen")
    @unittest.skipif(mylib._version_<(1,3),"not supported in this library version")
    def test_format(self):
        #tests that work for only a certain version of the library
        pass
    @unittest.skipUnless(sys.platform.startswith("win"),"requires windows")
    def test_windows_support(self):
        #windows specific testing code
        pass
    def test_maybe_skipped(self):
        if not external_resource_availble():
            self.skipTest("external resource not available")
            #test code that depends on the external resource
            pass
#skip classes
@unittest.skip("showing class skipping")
class MySkippedTestCase(unittest.TestCase):
    def test_not_run(self):
        pass
class NumersTest(unittest.TestCase):
    def test_even(self):
        '''test that numbers between o and 5 are all even'''
        for i in range(0,6):
            with self.subTest(i=i):
                self.assertEqual(i%2,0)
####################################################################
import unittest
class LetsTest(unittest.TestCase):
    def testMethod(self):
        self.assertTrue(False)
if __name__=="__main__":
    unittest.main()

#####################################################################
#python code to demonstrate working of unittest
#assertLessEqual()
#test suite
import unittest
class TestAssertLessEqual(unittest.TestCase):
    #negative test function to test if values1 is less or equal than
    def test_less_equal(self):
        first=5
        second=6


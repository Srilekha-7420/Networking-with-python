from student import Student
import unittest
class test_student(unittest.TestCase):
    def setUpClass(self):
        print("\nsetup")
    def tearDownClass(self):
        print("\nteardown")
    def test_email(self):
        print("test email")
        self.assertEqual(st.email,"sr.le@gmail.com ")
    def test_fullname(self):
        print("test fullname")
        self.assertEqual(st.fullname,"sr le")
    '''def test_apply_bonus(self):
        self.assertEqual(st.marks,45)
        st.apply_bonus()'''
    def test_fun(self):
        st.fun()
        self.assertEqual(Student.year,2022)
    def test_funct(self):
        st.function("HCL")
        self.assertEqual(st.somevalue,"sr lesr.le@gmail.com HCL")
st = Student("sr", "le", 30)
if __name__=='__main__':
    unittest.main()



import unittest
from student import *

class TestStudent(unittest.TestCase):
    def test_init(self):
        tomas = Student("Tomas", "Bejar")
        self.assertIsInstance(tomas, Student)
        self.assertEqual(tomas.first_name, "Tomas")
        self.assertEqual(tomas.last_name, "Bejar")

    def test_eq(self):
        tomas = Student("Tomas", "Bejar")
        tomas_clone = Student("Tomas", "Bejar")
        self.assertTrue(tomas == tomas_clone)
        self.assertEqual(tomas, tomas_clone) # identical as pvs
        david = Student("David", "Beamer")
        other_david = Student("David", "Fang")
        self.assertFalse(david == other_david)
        kayley = Student("Kayley", "Xu")
        shirley = Student("Shirley", "Xu")
        self.assertFalse(kayley == shirley)
        # with open("filename.txt", "r") as f:
        #     lines = f.readlines()
        # Equivalent to:
        # f = open("filename.txt", "r")
        # lines = f.readlines()
        # f.close()
        with self.assertRaises(TypeError):
            tomas == 1
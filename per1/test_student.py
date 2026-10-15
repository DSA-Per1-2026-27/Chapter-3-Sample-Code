import unittest
from student import *

class TestStudent(unittest.TestCase):
    def test_init(self):
        me = Student("Marcus", "Jaiclin")
        self.assertIsInstance(me, Student)

    def test_eq(self):
        me = Student("Marcus", "Jaiclin")
        my_clone = Student("Marcus", "Jaiclin")
        self.assertTrue(me == my_clone)
        aaron = Student("Aaron", "Cheng")
        self.assertFalse(me == aaron)
        henry_hou = Student("Henry", "Hou")
        henry_james = Student("Henry", "James")
        self.assertFalse(henry_hou == henry_james)
        # # This is better because it automatically closes the file
        # with open('filename.txt', 'r') as f:
        #     lines = f.readlines()
        # # Than this
        # f = open('filename.txt', 'r')
        # lines = f.readlines()
        # f.close() # A lot of people forget this
        with self.assertRaises(TypeError):
            me == 1
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 12:43:46 2026

@author: 20163372
"""
import unittest

class TestMathOperations(unittest.TestCase):
   def test_addition(self):
       self.assertEqual(1 + 1, 2)


def test_subtraction(self):
   self.assertEqual(5 - 3, 2)
   
if __name__ == '__main__':
   unittest.main()
   
   
# Code to be tested (math_operations.py)
def add(a, b):
   return a + b
# Test file (test_math_operations.py)
import unittest
from math_operations import add
class TestMathOperations(unittest.TestCase):
   def test_add_positive_numbers(self):
       self.assertEqual(add(2, 3), 5)
   def test_add_negative_numbers(self):
       self.assertEqual(add(-1, -1), -2)
if __name__ == '__main__':
   unittest.main()
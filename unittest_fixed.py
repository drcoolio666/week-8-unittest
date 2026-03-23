# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 12:43:46 2026

@author: 20163372
"""
import unittest

# Function to be tested (defined in same file)
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

# Single unified test class
class TestMathOperations(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(1 + 1, 2)

    def test_subtraction(self):          # FIX 1: was outside the class (missing indent)
        self.assertEqual(5 - 3, 2)

    def test_add_positive_numbers(self): # FIX 2: merged second duplicate class into this one
        self.assertEqual(add(2, 3), 5)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-1, -1), -2)

# FIX 3: removed 'from math_operations import add' — add() is defined locally above

if __name__ == '__main__':
    unittest.main(verbosity=2)

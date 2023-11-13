#!/usr/bin/python3
"""unittest for max_integer([...])"""


import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
        def test_max_integer(self):
                self.assertEqual(max_integer([1,2,3,4]), 4)
                self.assertEqual(max_integer([1,3, 2, 5]), 5)
        
if __name__ == '__main__':
        unittest.main()
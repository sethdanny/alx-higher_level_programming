#!/usr/bin/python3
"""unittest for max_integer([...])"""


import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
        def test_regular_list(self):
                self.assertEqual(max_integer([1,2,3,4]), 4)
                self.assertEqual(max_integer([1,3, 2, 5]), 5)

        def test_empty_list(self):
                self.assertIsNone(max_integer([]))

        def test_negative_list(self):
                self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

        def test_mixed_numbers(self):
                self.assertEqual(max_integer([1, -2, 4, -6]), 4)

        def test_one_element(self):
                self.assertEqual(max_integer([6]), 6)
        
if __name__ == '__main__':
        unittest.main()
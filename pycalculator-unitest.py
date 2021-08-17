import unittest
import pycalculator
from pycalculator import add, subtract, multiply


class MyTestCase(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(4, 5), 9)
        self.assertNotEqual(add(3, 7), 9)
        

    def test_subtract(self):
        self.assertEqual(subtract(4, 5), -1)
        self.assertNotEqual(subtract(2, 1), 0)
        

    def test_multiply(self):
        self.assertEqual(multiply(4, 5), 20)
        self.assertNotEqual(multiply(3, 7), 9)
        


if __name__ == '__main__':
    unittest.main()



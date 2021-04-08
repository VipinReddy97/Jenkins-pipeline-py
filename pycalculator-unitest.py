import unittest
import calci
from calci import add, subtract, multiply


class MyTestCase(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(4, 5), 9)
        self.assertNotEqual(add(3, 7), 9)
        msg = "error"
        self.assertEqual(add(-3, 2), msg)

    def test_subtract(self):
        self.assertEqual(subtract(4, 5), -1)
        self.assertNotEqual(subtract(2, 1), 0)
        msg = "error"
        self.assertEqual(subtract(-5, 2), msg)

    def test_multiply(self):
        self.assertEqual(multiply(4, 5), 20)
        self.assertNotEqual(multiply(3, 7), 9)
        msg = "error"
        self.assertEqual(multiply(-3, -2), msg)


if __name__ == '__main__':
    unittest.main()

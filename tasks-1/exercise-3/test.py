import unittest
import code

class TestClac(unittest.TestCase):

    def test_add(self):
        result = code.add(10, 5)
        self.assertEqual(result, 15)

    def test_subtract(self):
        result = code.subtract(10, 5)
        self.assertEqual(result, 5)
    
    def test_multiply(self):
        result = code.multiply(10, 5)
        self.assertEqual(result, 50)
    
    def test_divide(self):
        result = code.divide(10, 5)
        self.assertEqual(result, 2)


if __name__ == '__main__':
    unittest.main()
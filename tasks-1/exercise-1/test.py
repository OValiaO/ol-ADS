import unittest
from code import simple_sum

class TestSimpleSum(unittest.TestCase):

    def test_simple_sum_positive_numbers(self):
        result = simple_sum(2, 3)
        self.assertEqual(result, 5)

    def test_simple_sum_negative_numbers(self):
        result = simple_sum(-2, -3)
        self.assertEqual(result, -5)

    def test_simple_sum_mixed_numbers(self):
        result = simple_sum(2, -3)
        self.assertEqual(result, -1)

    def lol(self):
        result = simple_sum(1, 1)
        self.assertEqual(result, 2)

if __name__ == '__main__':
    unittest.main()

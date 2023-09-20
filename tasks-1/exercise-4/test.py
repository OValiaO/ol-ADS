import unittest
from code import find_min_max

class TestMinMaxFunction(unittest.TestCase):
    
    def test_empty_list(self):
        self.assertEqual(find_min_max([]), (None, None))

    def test_single_element_list(self):
        self.assertEqual(find_min_max([5]), (5, 5))

    def test_positive_numbers(self):
        self.assertEqual(find_min_max([1, 2, 3, 4, 5]), (1, 5))

    def test_negative_numbers(self):
        self.assertEqual(find_min_max([-5, -4, -3, -2, -1]), (-5, -1))

    def test_mixed_numbers(self):
        self.assertEqual(find_min_max([-2, 0, 3, 7, -1]), (-2, 7))

if __name__ == '__main__':
    unittest.main()
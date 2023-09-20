import unittest
from code import reverseList

class TestReverseList(unittest.TestCase):

    def test_reverse_list(self):
        # Test case 1: Reverse the entire array
        arr1 = [1, 2, 3, 4, 5]
        self.assertEqual(reverseList(arr1, 0, 4), [5, 4, 3, 2, 1])

        # Test case 2: Reverse a portion of the array
        arr2 = [10, 20, 30, 40, 50]
        self.assertEqual(reverseList(arr2, 1, 3), [10, 40, 30, 20, 50])

        # Test case 3: Reverse an empty array
        arr3 = []
        self.assertEqual(reverseList(arr3, 0, 0), [])

        # Test case 4: Reverse a single-element array
        arr4 = [99]
        self.assertEqual(reverseList(arr4, 0, 0), [99])

if __name__ == '__main__':
    unittest.main()
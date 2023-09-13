import unittest
from code import reverseList

class TestReverseList(unittest.TestCase):

    def first_test(self):
        result = reverseList([1, 2, 3, 4, 5, 6], 0, 5)
        self.assertEqual(result, [6, 5, 4, 3, 2, 1])

if __name__ == '__main__':
    unittest.main()

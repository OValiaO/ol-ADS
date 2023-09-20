import unittest
import code

class TestClac(unittest.TestCase):

    def test_add(self):
        result = code.add(10, 5)
        self.assertEqual(result, 15)
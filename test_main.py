import unittest

def add(a, b):
    return a + b

class TestAddFunction(unittest.TestCase):
    def test_add_two_positives(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_two_negatives(self):
        self.assertEqual(add(-2, -3), -5)

if __name__ == '__main__':
    unittest.main()
import unittest
from sigma import calculate_sigma


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(calculate_sigma(['a','b','|','c','&']), [[5, 6, 7], ['c', 'b', 'a']])
        self.assertEqual(calculate_sigma(['a', 'b', '&', 'c', '>']), [[0, 1, 2, 4, 5, 6, 7], ['c', 'b', 'a']])
        self.assertEqual(calculate_sigma(['a','b','|','c','&']), [[5, 6, 7], ['c', 'b', 'a']])


if __name__ == '__main__':
    unittest.main()

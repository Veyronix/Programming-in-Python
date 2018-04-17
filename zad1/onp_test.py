import unittest
from onp import changing_to_onp

class MyTestCase(unittest.TestCase):
    def test_changing_to_onp(self,):
        self.assertEqual(changing_to_onp("a & l > a"),['a', 'l', '&', 'a', '>'])
        self.assertEqual(changing_to_onp("a > l > a"),['a', 'l', 'a', '>', '>'])
        self.assertEqual(changing_to_onp("a ^ l > a"),['a', 'l', '^', 'a', '>'])
        self.assertEqual(changing_to_onp("abc & l | o"),['abc', 'l', '&', 'o', '|'])


if __name__ == '__main__':
    unittest.main()

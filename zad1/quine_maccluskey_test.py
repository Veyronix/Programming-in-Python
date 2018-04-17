import unittest
import quine_mccluskey


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(quine_mccluskey.if_diffrence_in_one_char("1xx1","1xx0"), True)
        self.assertEqual(quine_mccluskey.if_diffrence_in_one_char("1xx0","1xx0"), False)
        self.assertEqual(quine_mccluskey.if_diffrence_in_one_char("1000","1xx0"), False)

        self.assertEqual(quine_mccluskey.comparator("0,1", "2,3"), -1)
        self.assertEqual(quine_mccluskey.comparator("4,6", "2,3"), 1)
        self.assertEqual(quine_mccluskey.comparator("14,26", "2,3"), 1)
        self.assertEqual(quine_mccluskey.comparator("2,3", "2,3"), 0)


if __name__ == '__main__':
    unittest.main()

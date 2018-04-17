import unittest
from property import propriety_of_expression

class MyTestCase(unittest.TestCase):
    def test_propriety_of_expression(self):
        self.assertEqual(propriety_of_expression("ala ma kota"), False)
        self.assertEqual(propriety_of_expression("ala & ma | kota"), True)
        self.assertEqual(propriety_of_expression("ala & ma ^ kota | "), False)
        self.assertEqual(propriety_of_expression("& ala | ma | kota"), False)
        self.assertEqual(propriety_of_expression("@ ala & ma & kota"), False)
        self.assertEqual(propriety_of_expression("((ala) ^ (ma ^ kota))"), True)



if __name__ == '__main__':
    unittest.main()

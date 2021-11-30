import unittest
from primality_check import is_prime

class TestPrimalityCheck(unittest.TestCase):

    def test_wrong_number(self):
        for i in [-10, 0]:
            with self.assertRaises(ValueError):
                is_prime(i)
    
    def test_prime(self):
        for i in [1,2,3,5,7,11,17,19,223]:
            self.assertTrue(is_prime(i))
        
    def test_not_prime(self):
        for i in [4,6,9,10]:
            self.assertFalse(is_prime(i))

if __name__=="__main__":
    unittest.main()

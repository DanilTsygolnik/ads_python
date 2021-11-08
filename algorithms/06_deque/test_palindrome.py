import unittest
from palindrome import palindrome

class TestPalindrome(unittest.TestCase):

    def test_main(self):
        with self.assertRaises(TypeError):
            palindrome(1234)
        with self.assertRaises(ValueError):
            palindrome("")
        self.assertTrue(palindrome("aa"))
        self.assertTrue(palindrome("aba"))
        self.assertTrue(palindrome("abba"))
        self.assertTrue(palindrome("abcba"))
        self.assertFalse(palindrome("ab"))
        self.assertFalse(palindrome("abb"))
        self.assertFalse(palindrome("abbb"))
        self.assertFalse(palindrome("abcaa"))

if __name__=="__main__":
    unittest.main()

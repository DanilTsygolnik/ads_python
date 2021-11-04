import unittest
from extra_1_brackets import check_balance

class TestFunc(unittest.TestCase):
    def test_type_error(self):
        with self.assertRaises(TypeError):
            check_balance(123)
        with self.assertRaises(TypeError):
            check_balance(1.23)
        with self.assertRaises(TypeError):
            check_balance(True)
        with self.assertRaises(TypeError):
            check_balance(None)

    def test_type_error_list(self):
        with self.assertRaises(TypeError):
            check_balance([123])

    def test_type_error_tuple(self):
        with self.assertRaises(TypeError):
            check_balance((345, 123))

    def test_type_error_dict(self):
        with self.assertRaises(TypeError):
            check_balance({})

    def test_output(self):
        self.assertEqual(check_balance("((()))"), "String is balanced")
        self.assertEqual(check_balance("((())"), "String is not balanced")

if __name__=="__main__":
    unittest.main()

import unittest
from sets import PowerSet


class TestPowerSetBasicMethods(unittest.TestCase):

    def test_main(self):

        # __init__()
        PS = PowerSet()
        self.assertEqual(PS.size(), 0)

        # put(value)
        PS.put("a")
        self.assertEqual(PS.size(), 1)

        # get(value)
        self.assertTrue(PS.get("a"))
        self.assertFalse(PS.get("b"))

        # remove(value)
        self.assertFalse(PS.remove("b"))
        self.assertTrue(PS.remove("a"))
        self.assertEqual(PS.size(), 0)


if __name__ == '__main__':
    unittest.main()

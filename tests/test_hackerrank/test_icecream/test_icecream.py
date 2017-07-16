import unittest
from icecream.icecream import match


class TestIceCream(unittest.TestCase):

    def t0(self):
        self.assertEqual(match([1,4,5,3,2], 4), (1,4))

    def t0(self):
        self.assertEqual(match([2,2,4,3], 4), (1,2))

if __name__ == "__main__":
    unittest.main()
import unittest

from hackerrank.icecream.icecream import match


class TestIceCream(unittest.TestCase):
    def test_0(self):
        self.assertEqual(match([1, 4, 5, 3, 2], 4), (1, 4))

    def test_1(self):
        self.assertEqual(match([2, 2, 4, 3], 4), (1, 2))

    def test_2(self):
        self.assertEqual(match([22, 108, 2, 2, 4, 3, 4, 11, 15, 19, ], 15), (5, 8))


if __name__ == "__main__":
    unittest.main()

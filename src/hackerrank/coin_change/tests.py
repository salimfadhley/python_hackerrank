import unittest

from hackerrank.coin_change.impl import change


class test_coin_change(unittest.TestCase):

    def test_trivial0(self):
        self.assertEqual(change(0,frozenset()), 1)

    def test_trivial1(self):
        self.assertEqual(change(0,frozenset({1,2,3})), 1)

    def test_trivial2(self):
        self.assertEqual(change(2,frozenset({6,9})), 0)

    def test_trivial3(self):
        self.assertEqual(change(4,frozenset({1,2})), 0)

    def test_trivial4(self):
        self.assertEqual(change(1,frozenset({1})), 1)

    def test_trivial5(self):
        self.assertEqual(change(2,frozenset({1})), 1)

    def test_trivial6(self):
        self.assertEqual(change(2,frozenset({1,2})), 2)

    def test_trivial7(self):
        self.assertEqual(change(3,frozenset({1,2})), 2)


if __name__ == "__main__":
    unittest.main()
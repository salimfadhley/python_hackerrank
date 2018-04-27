import unittest

from hackerrank.contacts.impl import find, add


def get_trie_node():
    return [{}, 0]


class TestFoo(unittest.TestCase):

    def test_zero(self):
        t = get_trie_node()
        self.assertEqual(find(t, ""), 0)

    def test_zero_with_content(self):
        t = get_trie_node()
        add(t, list("a"))
        add(t, list("b"))
        add(t, list("c"))
        self.assertEqual(find(t, ""), 3)

    def test_one(self):
        t = get_trie_node()
        self.assertEqual(find(t, "x"), 0)

    def test_two(self):
        t = get_trie_node()

        add(t, list("abc"))
        add(t, list("abd"))

        self.assertEqual(find(t, "ab"), 2)

    def test_three(self):
        t = get_trie_node()

        add(t, list("aa"))
        add(t, list("ab"))
        add(t, list("ac"))

        self.assertEqual(find(t, ""), 3)
        self.assertEqual(find(t, "a"), 3)
        self.assertEqual(find(t, "aa"), 1)
        self.assertEqual(find(t, "ad"), 0)
        self.assertEqual(find(t, "aax"), 0)

    def test_four(self):
        t = get_trie_node()

        add(t, list("aa"))

        self.assertEqual(find(t, "xxxxxxxxxxxxxxxxx"), 0)


if __name__ == "__main__":
    unittest.main()

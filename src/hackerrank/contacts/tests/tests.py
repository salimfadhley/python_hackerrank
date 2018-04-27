import unittest

from hackerrank.contacts.impl import find, add

def get_trie_node():
    return {}, {}


class TestFoo(unittest.TestCase):

    def test_zero(self):
        t = get_trie_node()
        self.assertEqual(find(t, ""), 0)

    def test_zero_with_content(self):
        t = get_trie_node()
        add(t, "a")
        add(t, "b")
        add(t, "c")
        self.assertEqual(find(t, ""), 3)

    def test_one(self):
        t = get_trie_node()
        self.assertEqual(find(t, "x"), 0)

    def test_two(self):
        t = get_trie_node()

        add(t, "abc")
        add(t, "abd")

        self.assertEqual(find(t, "ab"), 2)

if __name__ == "__main__":
    unittest.main()

import unittest

from hackerrank.primality.impl import is_prime


PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]


class test_coin_change(unittest.TestCase):

    def test_prime(self):
        for p in PRIMES:
            return self.assertTrue(is_prime(p), "%i is expected to be prime" % p)

    def test_non_prime(self):
        for p in range(2,200):
            if p not in PRIMES:
                return self.assertFalse(is_prime(p), "%i is not to be prime" % p)

if __name__ == "__main__":
    unittest.main()
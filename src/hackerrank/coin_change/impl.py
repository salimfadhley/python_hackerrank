# https://www.hackerrank.com/challenges/ctci-coin-change/problem
import functools
from typing import FrozenSet


def readints(inputlines):
    text = next(inputlines)
    try:
        return (int(x) for x in (text.split(" ")))
    except ValueError:
        raise ValueError("Cannot convert %r" % text)

found_solutions = {}

@functools.lru_cache(maxsize=None)
def change(n: int, coins: FrozenSet[int]) -> int:
    if n == 0:
        return 1

    coins = frozenset(c for c in coins if c <= n)

    if not coins:
        return 0

    return sum(change(n - c, frozenset(C for C in coins if c <= c)) for c in coins)


def impl(inputlines):
    n, *_ = readints(inputlines)
    coins = frozenset(readints(inputlines))
    yield change(n, coins)


if __name__ == "__main__":
    import sys

    for line in impl((l.strip() for l in sys.stdin)):
        print(line)

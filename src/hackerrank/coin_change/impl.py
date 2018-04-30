# https://www.hackerrank.com/challenges/ctci-coin-change/problem
import functools


def readints(inputlines):
    text = next(inputlines)
    try:
        return tuple(int(x) for x in (text.split(" ")))
    except ValueError:
        raise ValueError("Cannot convert %r" % text)


@functools.lru_cache(maxsize=None)
def change(n: int, coins) -> int:
    if n == 0:
        return 1

    if not coins:
        return 0

    return sum(change(n - c, tuple(C for C in coins if C <= n and C <= c)) for c in coins)


def impl(inputlines):
    n, *_ = readints(inputlines)
    coins = readints(inputlines)
    yield change(n, coins)


if __name__ == "__main__":
    import sys

    for line in impl((l.strip() for l in sys.stdin)):
        print(line)

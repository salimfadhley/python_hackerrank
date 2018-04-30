# https://www.hackerrank.com/challenges/ctci-big-o/problem

import math


def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False
    i = 5
    while i <= math.sqrt(n):
        if n % i == 0:
            return False
        if n % (i + 2) == 0:
            return False
        i += 6
    return True


def impl(inputlines):
    next(inputlines)

    for l in inputlines:
        yield is_prime(int(l)) and "Prime" or "Not prime"


if __name__ == "__main__":
    import sys

    for line in impl((l.strip() for l in sys.stdin)):
        print(line)

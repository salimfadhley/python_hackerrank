from bisect import bisect_left, bisect_right
from itertools import count
from typing import Tuple, Sequence, IO
import sys


def match(prices: Sequence[int], t: int) -> Tuple[int, int]:
    menu = sorted(list(zip(prices, count(1))))

    l_ptr = 0
    r_ptr = len(menu) - 1

    def l_val():
        return menu[l_ptr][0]

    def max_r_val():
        return t - l_val()

    def r_val():
        return menu[r_ptr][0]

    def min_l_val():
        return t - r_val()

    prices = [x[0] for x in menu]

    side = True
    while l_val() + r_val() != t:
        if side:
            r_ptr = bisect_right(prices, max_r_val()) - 1
        else:
            l_ptr = bisect_left(prices, min_l_val())
        side = not side

    return sorted((menu[l_ptr][1], menu[r_ptr][1]))


def numbers_iterator(f):
    for line in f:
        numbers = line.strip().split(" ")
        yield [int(i) for i in numbers]


def main(inp: IO=sys.stdin, out: IO=sys.stdout):
    ni = numbers_iterator(inp)
    repeats, *_ = next(ni)

    for r in range(repeats):
        t, *_ = next(ni)
        _ = next(ni)
        prices = next(ni)
        out.write(" ".join(str(n) for n in match(prices, t)) + "\n")


if __name__ == "__main__":
    main(open("icecream_1.txt"))

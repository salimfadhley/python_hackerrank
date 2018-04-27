import bisect
from typing import Callable, Sequence, Tuple


def chop(fn_bisect: Callable[[Sequence, int], Tuple[Sequence, Sequence]], l: Sequence, i: int):
    x = fn_bisect(l, i)
    return l[:x], l[x:]


def cov(l: Sequence, k: int):

    count = 0

    while True:
        if not l:
            return count

        first_address = l[0]
        furthest_possible_transmitter_address = first_address + k
        possible_transmitter_locations = l[:bisect.bisect_right(
            l, furthest_possible_transmitter_address)]
        transmitter_location = max(
            a for a in possible_transmitter_locations if a - k <= first_address)
        last_covered_location = transmitter_location + k

        remainder_index = bisect.bisect_right(l, last_covered_location)
        l = l[remainder_index:]
        count = count + 1

# 5 1
# 1 2 3 4 5


def numbers_iterator(f):
    for line in f:
        numbers = line.strip().split(" ")
        yield [int(i) for i in numbers]


inp = numbers_iterator(open("input.txt"))


n, k = next(inp)
l = next(inp)

print(cov(sorted(l), k))

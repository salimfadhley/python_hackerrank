import bisect
import sys
from collections import defaultdict
from typing import Tuple, Sequence


def numbers_iterator(f):
    for line in f:
        numbers = line.strip().split(" ")
        try:
            yield [int(i) for i in numbers]
        except ValueError:
            raise RuntimeError("Error parsing line %r" % line)


def count(row:Sequence[Tuple[int,int]])->int:
    if not row:
        return 0
    row_sorted = sorted(row)
    compacted = [row_sorted.pop(0)]

    for n in row_sorted:

        if n[0] > compacted[-1][1]:
            compacted.append(n)
            continue

        if n[1] > compacted[-1][1]:
            compacted[-1] = (compacted[-1][0], n[1])

    return sum((1+t[1]-t[0]) for t in compacted)


def main(inp=sys.stdin):
    ni = numbers_iterator(inp)
    n,m,k = next(ni)
    rows = defaultdict(list)
    for ri, s, e in ni:
        track = (s,e)
        rows[ri].append(track)
    res = sum(m - count(rows[i]) for i in range(1, n+1))
    print(res)

if __name__ == "__main__":
    main(open("trains_input.txt"))

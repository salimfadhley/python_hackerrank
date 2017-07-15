import bisect
import sys
from collections import defaultdict
from typing import Tuple, Sequence


def numbers_iterator(f):
    for line in f:
        numbers = line.strip().split(" ")
        yield [int(i) for i in numbers]


def insert(tracks:list, track:Tuple[int, int]):
    i = bisect.bisect_left(tracks, track)
    tracks.insert(i, track)

def count(row:Sequence[Tuple[int,int]])->int:
    if not row:
        return 0

    print(row)

    return 0



def main(inp=sys.stdin):
    ni = numbers_iterator(inp)
    n,m,k = next(ni)
    rows = defaultdict(list)
    for ri, s, e in ni:
        track = (s,e)
        insert(rows[ri], track)
    res = sum(m - count(rows[i]) for i in range(1, n+1))
    print(res)

if __name__ == "__main__":
    main(open("trains_input.txt"))

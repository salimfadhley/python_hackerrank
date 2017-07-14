import sys
from collections import defaultdict


def numbers_iterator(f):
    for line in f:
        numbers = line.strip().split(" ")
        yield [int(i) for i in numbers]


def main(inp=sys.stdin, out=sys.stdout):
    ni = numbers_iterator(inp)
    n,m,k = next(ni)

    rows = defaultdict(int)

    for (ri, start, end) in ni:
        rows[ri-1] = rows[ri-1] | int("1"*(1 + end-start) + "0"*(m-end), 2)

    res = sum((
        m - bin(rows[ri])[2:].count("1")
               ) for ri in range(n))

    print(res, sys.stdout)



if __name__ == "__main__":
    main(open("trains_input.txt"))

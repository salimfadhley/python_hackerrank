def numbers_iterator(f):
    for line in f:
        numbers = line.strip().split(" ")
        yield [int(i) for i in numbers]


ni = numbers_iterator(sys.stdin)

n, m, k = next(ni)

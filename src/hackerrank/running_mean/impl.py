# https://www.hackerrank.com/challenges/ctci-find-the-running-median/problem
from _bisect import insort_left


def impl(inputlines):
    state = []

    next(inputlines)
    input = (int(i) for i in inputlines)

    for c, i in enumerate(input):
        insort_left(state, i)
        index = int(c / 2)
        if c % 2 == 0:
            yield state[index] * 1.0
        else:
            yield sum(state[index:index+2]) / 2.0


if __name__ == "__main__":
    import sys
    for line in impl((l.strip() for l in sys.stdin)):
        print(line)

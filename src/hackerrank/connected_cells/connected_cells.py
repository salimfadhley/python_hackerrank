import sys
from typing import IO, TextIO, List, Tuple, Set


class G:
    ADJACENCT = [
        (0, 1),
        (1, 1),
        (1, 0),
        (1, -1),
        (0, -1),
        (-1, -1),
        (-1, 0),
        (-1, 1)
    ]

    def __init__(self, n, m, matrix: List[List[int]]):
        self.n = n
        self.m = m
        self.matrix = matrix

    def nodes(self):
        for i in range(self.n):
            for j in range(self.m):
                if self.is_node((i, j)):
                    yield (i, j)

    def adjacent(self, cell: Tuple[int, int]):
        return (c for c in
                [(cell[0]+i, cell[1]+j) for i, j in self.ADJACENCT] if
                self.is_node(c))

    def is_node(self, n: Tuple[int, int]) -> bool:
        i, j = n
        if 0 <= i < self.n:
            if 0 <= j < self.m:
                return bool(self.matrix[i][j])
        return False

    def visit(self, cell: Tuple[int, int], visited: Set[Tuple[int, int]]) -> int:
        visited.add(cell)
        return 1 + sum(self.visit(c, visited) for c in self.adjacent(cell) if c not in visited)


def numbers_iterator(f):
    for line in f:
        numbers = line.strip().split(" ")
        yield [int(i) for i in numbers]


def main(inp: TextIO = sys.stdin, out: IO = sys.stdout):
    ni = numbers_iterator(inp)
    n, *_ = next(ni)
    m, *_ = next(ni)

    graph = G(n, m, list(ni))
    nodes = list(graph.nodes())

    visited = set()

    res = max(graph.visit(n, visited)
              for n in graph.nodes() if not n in visited)

    print(res)


if __name__ == "__main__":
    main(open("input.txt"))

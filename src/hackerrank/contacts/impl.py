import sys


def add(t, word)->None:
    while word:
        head = word.pop(0)
        t[1][head] = t[1].setdefault(head, 0) + 1
        t = t[0].setdefault(head, ({}, {}))


def find(t, word)->int:
    for c in word:
        try:
            t = t[0][c]
        except KeyError:
            return 0
    return sum(t[1].values())


def impl(inputlines):
    next(inputlines)


    commands = {
        "add": add,
        "find": find
    }

    trie = ({}, {})

    for l in inputlines:
        command, word = l.strip().split(" ")

        result = commands[command](trie, list(word))
        if result is not None:
            yield str(result)

if __name__ == "__main__":
    for line in impl((l.strip() for l in sys.stdin)):
        print(line)








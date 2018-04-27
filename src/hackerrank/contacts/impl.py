import sys


def add(t, word)->None:
    while word:
        head = word.pop(0)
        d, c = t
        c[head] = c.get(head, 0) + 1
        t = d.setdefault(head, ({}, {}))


def find(t, word)->int:
    if word:
        head, *rest = word
        if rest:
            try:
                return find(t[0][head], rest)
            except KeyError:
                return 0
        else:
            return t[1].get(head,0)
    else:
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

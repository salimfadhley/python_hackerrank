import sys


def add(t, word):
    d, c = t
    t[1] = c + 1
    if word:
        head, *tail = word
        add(d.setdefault(head, [{}, 0]), tail)


def find(t, word):
    while word:
        head, *word = word
        try:
            t = t[0][head]
        except KeyError:
            return 0

    return t[1]



def impl(inputlines):
    next(inputlines)

    commands = {
        "add": add,
        "find": find
    }

    trie = [{}, 0]

    for l in inputlines:
        command, word = l.strip().split(" ")

        result = commands[command](trie, list(word))
        if result is not None:
            yield str(result)


if __name__ == "__main__":
    for line in impl((l.strip() for l in sys.stdin)):
        print(line)

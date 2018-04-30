# Re-usable test-harness
# This code allows me to run HackerRank test-cases
# locally and paste the code into HackerRank without modification

import sys
import os
import difflib

from hackerrank.coin_change.impl import impl


def main(inp=sys.stdin):
    return (str(o) for o in impl(l.strip() for l in inp))


def get_test_files(maxn=10, input_template="input%i.txt", expected_template="expected%i.txt"):
    for i in range(maxn):
        input_filename = input_template % i
        output_filename = expected_template % i
        if os.path.exists(input_filename) and os.path.exists(output_filename):
            yield i, input_filename, output_filename


if __name__ == "__main__":
    test_files = list(get_test_files())
    if test_files:
        # If local files exist, run, and then diff actual vs expected.
        for i, input_filename, expected_filename in test_files:
            with open(input_filename) as inf, open(expected_filename) as exf:
                result = list(main(inf))
                expected_text = list(l.strip() for l in exf)

                differences = list(difflib.context_diff(
                    result, expected_text, input_filename, expected_filename))
                if differences:
                    for diff in differences:
                        print(diff)
                else:
                    print("Test Case %i passed" % i)
    else:
        # Or just run and report the output back to stdout
        sys.stdout.write("\n".join(main(list(sys.stdin))))

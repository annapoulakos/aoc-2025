import argparse
import pathlib
import sys


def load_file(filename):
    with (pathlib.Path(filename)).open(mode="r") as f:
        lines = [x.strip() for x in f.readlines()]
    return lines


def parse_args():
    parser = argparse.ArgumentParser()

    group = parser.add_mutually_exclusive_group()
    group.add_argument("--test", action="store_true", dest="action_test")
    group.add_argument("--run", action="store_true", dest="action_run")

    return parser.parse_args(sys.argv[1:])


# from ap.tools.itertools
def _index(i, n, k):
    return i * (n // k) + min(i, n % k)


def n_chunks(lst, k):
    """Split list into k approximately even lists"""
    n = len(lst)
    for i in range(k):
        yield lst[_index(i, n, k) : _index(i + 1, n, k)]


def chunk(lst, k):
    # print(lst, k)
    """Split list into pieces of approximately k-size"""
    for i in range(0, len(lst), k):
        yield lst[i : i + k]

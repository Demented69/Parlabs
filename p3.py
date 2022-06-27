import sys
import os
from time import perf_counter
from collections import Counter
from functools import reduce
from concurrent.futures import ThreadPoolExecutor


def searchtxt(path):
    filetxt = []
    for fnames in os.listdir(path):
        if fnames.split('.')[-1] == 'txt':
            filetxt.append(os.path.join(path, fnames))
    return filetxt


def countfiles(filename):
    with open(filename) as f:
        return Counter(f.read().split())


def update(c_1, c_2):
    c_1.update(c_2)
    return c_1


if __name__ == '__main__':
    file_PATH = sys.argv[1]
    files_DIR = searchtxt(file_PATH)

    stopwatch_start = perf_counter()
    with ThreadPoolExecutor() as executor:
        file_word_counters = executor.map(countfiles, files_DIR)
        allinfiles = reduce(update, file_word_counters)
    stopwatch_stop = perf_counter()

    print(dict(allinfiles))
    print(round(stopwatch_stop - stopwatch_start, 2))

import sys
import os
from time import perf_counter
from collections import Counter


def searchtxt(path):
    filetxt = []
    for fnames in os.listdir(path):
        if fnames.split('.')[-1] == 'txt':
            filetxt.append(os.path.join(path, fnames))
    return filetxt


def countall(counts):
    count_1 = counts[0]
    for count in counts[1:]:
        count_1.update(count)
    return count_1


def countfiles(text):
    return Counter(text.split())


if __name__ == '__main__':
    file_PATH = sys.argv[1]
    files_DIR = searchtxt(file_PATH)

    stopwatch_start = perf_counter()
    counts = []
    for filename in files_DIR:
        with open(filename) as f:
            file_text = f.read()
        count = countfiles(file_text)
        counts.append(count)
    allinfiles = countall(counts)
    stopwatch_stop = perf_counter()

    print(dict(allinfiles))
    print(round(stopwatch_stop - stopwatch_start, 2))


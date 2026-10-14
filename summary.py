#!/usr/bin/env python3

import sys
from collections import Counter

def init():
    al=len(sys.argv)
    fp = sys.argv[1]
    pos = int(sys.argv[2]) if al > 2 else 7

    with open(fp) as file:
        lines = file.readlines();

    print("Total lines:",len(lines))
    print()

    counts = Counter()
    for line in lines:
        fields = line.split()
        if len(fields) > pos:
            key = fields[pos]
            counts[key] += 1

    print("Top 5:\n")
    for item, n in counts.most_common(5):
        print(item, n)


if __name__=='__main__':
    init()

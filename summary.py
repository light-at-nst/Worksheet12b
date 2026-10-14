#!/usr/bin/env python3

import sys
from collections import Counter

def init():
    al=len(sys.argv)
    fp = sys.argv[1]
    pos = int(sys.argv[2]) if al > 2 else 7
    word = sys.argv[3].lower() if al > 3 else ""

    with open(fp) as file:
        lines = file.readlines();

    print("Total lines:",len(lines))
    print()

    counts = Counter()
    for line in lines:
        fields = line.lower().split()
        if len(fields) > pos:
            key = fields[pos]
            counts[key] += 1

    print("Top 5:\n")
    for item, n in counts.most_common(5):
        print(item, n)
    print()

    if word:
        c=0
        w=word.lower()
        for line in lines:
            c += line.lower().count(w)
        print(f"Occurences of {word}: {c}")


if __name__=='__main__':
    init()

#!/usr/bin/env python

import fileinput
import re
from collections import defaultdict

ENTRIES_TO_SHOW = 25

word_requencies = defaultdict(int)
stop_words = ('all', 'am', 'an', 'and', 'are', 'as', 'at', 'be', 'been', 'but',
              'by', 'could', 'do', 'for', 'from', 'had', 'have', 'he', 'her', 'him', 'his',
              'if', 'in', 'is', 'it', 'me', 'must', 'my', 'no', 'not', 'of', 'on',
              'or', 'said', 'she', 'so', 'that', 'the', 'their', 'them', 'there', 'they', 'this',
              'to', 'was', 'were', 'what', 'when', 'which', 'will', 'with', 'would', 'you', 'your')


for line in fileinput.input():
    line = re.sub(r"[^A-Za-z]", " ", line.rstrip())  # Replace non-letters with space.
    words_on_line = line.split()
    words_on_line = [word for word in words_on_line if len(word) > 1]
    words_on_line = map(lambda s: s.lower(), words_on_line)
    words_on_line = filter(lambda word: word not in stop_words, words_on_line)

    for word in words_on_line:
        word_requencies[word] += 1


def comparator(x, y):
    # Sort tuples (word, freq) first according to freq, within the same freq in alphabetical order.
    if x[1] == y[1]:
        if x[0] == y[0]:
            return 0
        elif x[0] < y[0]:
            return -1
        else:
            return 1
    elif x[1] < y[1]:
        return 1
    else:
        return -1

top_entries = sorted(word_requencies.items(), cmp=comparator)[:ENTRIES_TO_SHOW]
for item in top_entries:
    print "%s\t- %s" % item

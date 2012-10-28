#!/usr/bin/env python

import sys
from collections import Counter

word_file = sys.argv[1]
letters = sys.argv[2]

letters_count = Counter(letters)
print letters
print letters_count

words = open(word_file).readlines()
for word in words:
    word = word.strip()

    word_count = Counter(word)

    # is the word a subset of the letters

    total = 0
    found = 0
    for letter, count in word_count.items():
        total += 1
        if letters_count[letter] >= count:
            found += 1

    if found >= total:
        print word, len(word)

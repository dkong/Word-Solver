#!/usr/bin/env python

import sys
from collections import Counter

word_file = sys.argv[1]
letters = sys.argv[2]

letters_count = Counter(letters)
letters = set(letters)

possible_words = []

words = open(word_file).readlines()
for word in words:
    word = word.strip()

    word_set = set(word)

    if word_set.issubset(letters):
        #print word, len(word)
        possible_words.append(word)

for word in possible_words:
    word_count = Counter(word)

    total = 0
    found = 0
    for letter, count in word_count.items():
        total += 1
        if letters_count[letter] >= count:
            found += 1

    if found >= total:
        print word, len(word)



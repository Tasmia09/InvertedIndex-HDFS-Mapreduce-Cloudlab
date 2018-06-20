#!/usr/bin/python

import sys

for line in sys.stdin:

    line = line.strip()

    words = line.split()

    documentId = words.pop(0)
    lineNumber = words.pop(0)

    for index in range(len(words)):
        word = words[index]
        print '{0}, {1}, {2}, {3}'.format(word, documentId, lineNumber, index)
    

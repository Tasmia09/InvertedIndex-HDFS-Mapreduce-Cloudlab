#!/usr/bin/python


from operator import itemgetter
import sys

def update(current_values, documentId, lineNumber, index):
  if (documentId in current_values):
    if (lineNumber in current_values[documentId]):
      current_values[documentId][lineNumber].append(index)
    else:
      current_values[documentId][lineNumber] = [index]
  else:
    current_values[documentId] = {lineNumber : [index]}

  return current_values


current_word = None
current_values = { }

word = None

for line in sys.stdin:

  line = line.strip()

  word, documentId, lineNumber, index = line.split(',', 3)

  try:
    lineNumber = int(lineNumber)
    index = int(index)
  except ValueError:
    continue

  if current_word == word:
    current_values = update(current_values, documentId, lineNumber, index)
  else:
    if current_word:
        print '{0}'.format({current_word : current_values})

    current_word = word
    current_values = { }
    current_values = update(current_values, documentId, lineNumber, index)

if current_word == word:
  print '{0}'.format({current_word : current_values})


#!/usr/bin/python

import logging
import sys
import ast

USAGE = 'usage: ./query.py dataFile'

logging.basicConfig( level=logging.INFO )
logger = logging.getLogger( __name__ )

result = ''
words = { }
with open( sys.argv[1], 'r' ) as f:
  fileContent = f.read()

fileContent = fileContent.split( '\n' )

for line in fileContent:
  if not line:
    continue

  word = ast.literal_eval(line)
  words.update(word)

print ("Type \":quit\" to quit.")

while sys.stdin:
  realQuery = input('Query: ')
  query = realQuery.lower()

  if query == ":quit":
    break

  if query not in words:
    continue

  result = '\nQuery Word: ' + str(realQuery) 
  for documentId in words[ query ]:
    result += '\n' + 'Document: ' + str( documentId ) 

    lineNumbers = words[ query ][ documentId ].keys()
    sorted(lineNumbers)

    result += '\n' +"Line: " + ', '.join( str(x) for x in lineNumbers ) + '\n'

  print (str(result))


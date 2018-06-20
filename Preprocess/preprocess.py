#!/usr/bin/python
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import re
import string
import logging
import sys

licenseStarts = [
  '*** START OF THIS PROJECT GUTENBERG EBOOK',
  '*END*THE SMALL PRINT! FOR PUBLIC DOMAIN',
  '\*\*\* START OF THIS PROJECT GUTENBERG EBOOK',
  '\*END\*THE SMALL PRINT! FOR PUBLIC DOMAIN'
]

USAGE = 'usage: ./preprocess documentId'

logging.basicConfig( level=logging.INFO )
logger = logging.getLogger( __name__ )
if len( sys.argv ) != 2:
  logger.error( USAGE )
  sys.exit(0)

documentId = sys.argv[1]  
fileContent = sys.stdin.read()

def removePunc(fileContent):
  fileContent = fileContent.translate(string.maketrans("",""), string.punctuation)
  fileContent = fileContent.decode('utf-8-sig')
  return fileContent


def lines(fileContent,documentId):
  fileContent = fileContent.split('\n')
  
  for i in range(len(fileContent)):
    fileContent[i].encode('ascii', 'ignore')
    fileContent[i] = '{0} {1} {2}'.format(documentId, i, fileContent[i])	
  return '\n'.join(fileContent)


def removeLicense(fileContent):
  index = -1  
  fileContent = fileContent.split("This Project Gutenberg eBook was originally marked as having a copyright.",1)[0]  

  for licenseStart in licenseStarts:
    index = fileContent.find(licenseStart)
    if ( index > 0 ):
      index = fileContent.find('\n', index)
      fileContent = fileContent[index+1:]
      
  return fileContent


fileContent = removeLicense(fileContent)

fileContent = fileContent.lower()

fileContent = removePunc(fileContent)

fileContent = lines(fileContent, documentId)

print (fileContent)

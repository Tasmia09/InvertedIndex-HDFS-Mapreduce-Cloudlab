#!/usr/bin/python

from numpy import *
import sys

f = open("WordCountOutput/processed.txt")
lines = f.read().splitlines()
counts = zeros(len(lines), dtype=int)
words = empty(len(lines), dtype=object)

for i in range(len(lines)):
  line = lines[i].replace('\t\n', '').split(", ")
  words[i] = line[0]
  counts[i] = int(line[1])

avg = mean(counts)

output = open ("stop_list.txt","w")

#threshold is half of average value. so words occured less than threshold value is considered as stop words
for i in range(len(counts)):
  if counts[i] > avg * .5:
    output.writelines((words[i]))
    output.write("\n")




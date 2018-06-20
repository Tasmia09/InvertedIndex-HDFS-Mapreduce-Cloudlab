#!/bin/bash

# Cleans and stores all data

mkdir -p raw_input/clean

DIRTY_FILES="$(ls raw_input/dirty)"

for f in $DIRTY_FILES
do
  python preprocess_removestop.py $f < raw_input/dirty/$f > raw_input/clean/$f
  python preprocess_removestop.py $f < raw_input/dirty/$f > ./../InvertedMapReduce/$f
done

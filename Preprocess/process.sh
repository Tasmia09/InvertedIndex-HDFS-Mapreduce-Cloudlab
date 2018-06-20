#!/bin/bash

# Cleans and stores all data

mkdir -p raw_input/clean
mkdir -p ./../WordCountMapReduce_Stop/processed_input

DIRTY_FILES="$(ls raw_input/dirty)"


for f in $DIRTY_FILES
do
  cp raw_input/dirty/$f ./../GenerateStopList/raw_input/dirty
  python preprocess.py $f < raw_input/dirty/$f > raw_input/clean/$f
  python preprocess.py $f < raw_input/dirty/$f > ./../WordCountMapReduce_Stop/processed_input/$f
done

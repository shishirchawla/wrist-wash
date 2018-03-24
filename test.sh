#!/bin/bash

# Read user and session info
while getopts u:s: option
do
  case "${option}" in
    u) USR=${OPTARG};;
    s) SESSION=${OPTARG};;
  esac
done

train_steps=3
activities=(1 2 3 4 5 6 7 9 10 11 12 13 14 15)

# Classify
HVite -A -D -T 1 -w def/wdnet -H model/hmm$((train_steps))/all -i hvite_user${USR}_session${SESSION}.mlf -S user${USR}-test-data/testlist${SESSION}.txt def/dict.txt hmmlist.txt > reco_user${USR}_session${SESSION}.mlf


#!/bin/bash

train_steps=3
activities=(1 2 3 4 5 6 7 9 10 11 12 13 14 15)

# Classify
HVite -A -D -T 1 -w def/wdnet -H model/hmm$((train_steps))/all -i hvite.mlf -S user1-test-data/testlist1.txt def/dict.txt hmmlist.txt > reco.mlf


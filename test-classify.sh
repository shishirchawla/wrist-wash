#!/bin/bash

# Read user and session info
while getopts ":u:s:t:z:" option
do
  case "${option}" in
    u) USR=${OPTARG};;
    s) SESSION=${OPTARG};;
    t) TYPE=${OPTARG};;
    z) UADAPTNUMSESSION=${OPTARG};;
  esac
done

train_steps=3
activities=(4 5 6 7 8 9 10 11 12 13 14 15 16)

# Classify
if [ ${TYPE} = "lopo" ]; then
  HVite -A -D -T 1 -p 5.0 -w def/wdnet -H model/hmm$((train_steps))/all -i hvite_user${USR}.mlf -S user${USR}-test-data/testlist.txt def/dict.txt hmmlist.txt > reco_user${USR}.mlf
elif [ ${TYPE} = "uadapt" ]; then
  HVite -A -D -T 1 -p 5.0 -w def/wdnet -H model/hmm$((train_steps))/all -i hvite_user${USR}_ses_${UADAPTNUMSESSION}.mlf -S user${USR}-test-data/testlist-ua.txt def/dict.txt hmmlist.txt > reco_user${USR}_ses_${UADAPTNUMSESSION}.mlf
else
  HVite -A -D -T 1 -w def/wdnet -H model/hmm$((train_steps))/all -i hvite_user${USR}_session${SESSION}.mlf -S user${USR}-test-data/testlist${SESSION}.txt def/dict.txt hmmlist.txt > reco_user${USR}_session${SESSION}.mlf
fi


#!/bin/bash

# script for LOPO
users=(1 2 3 4 5 6 7 8 9 11)
sessions=(1 2 3 4 5 6 7 8 9)

# for each user
for usr in ${users[@]}
do
  cat /dev/null > ${usr}-truth.txt
  cat /dev/null > ${usr}-pred.txt

  for session in ${sessions[@]}
  do
    awk '/mfcc$/{nr[NR+1]}; NR in nr' reco_user${usr}_session${session}.mlf | awk '{print $1}' >> ${usr}-pred.txt
    sed -n 's/^.*_act_\([0-9]*\).*$/\1/p' user${usr}-test-data/testlist${session}.txt | grep --color=never -o '[0-9]\+' | awk '{print "ACTIVITY"$0}' >> ${usr}-truth.txt
  done
done


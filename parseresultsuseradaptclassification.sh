#!/bin/bash

# script for LOPO

users=(1 2 3 4 5 6 7 8 9 11)
num_adapt_sessions=6

# for each user
for usr in ${users[@]}
do

  for num_sess in `seq 0 ${num_adapt_sessions}`
  do
    cat /dev/null > ${usr}-truth-${num_sess}.txt
    cat /dev/null > ${usr}-pred-${num_sess}.txt

    awk '/mfcc$/{nr[NR+1]}; NR in nr' reco_user${usr}_ses_${num_sess}.mlf | awk '{print $1}' >> ${usr}-pred-${num_sess}.txt
    sed -n 's/^.*_act_\([0-9]*\).*$/\1/p' user${usr}-test-data/testlist-ua.txt | grep --color=never -o '[0-9]\+' | awk '{print "ACTIVITY"$0}' >> ${usr}-truth-${num_sess}.txt
  done
done


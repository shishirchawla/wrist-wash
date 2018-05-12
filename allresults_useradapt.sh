#!/bin/bash

users=(1 2 3 4 5 6 7 8 9 11)
num_adapt_sessions=6

for usr in ${users[@]}
do

  for num_sess in `seq 0 ${num_adapt_sessions}`
  do
    echo user - ${usr}, num of user sessions used - ${num_sess}
    python scripts/results.py ${usr}-pred-${num_sess}.txt ${usr}-truth-${num_sess}.txt
    printf \\n
  done
done

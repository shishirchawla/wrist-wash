#!/bin/bash

users=(1 2 3 4 5 6 7 8 9 11)
#users=(1)

num_sessions=6

# for each user do leave one subject out
for usr in ${users[@]}
do
  for sess in `seq 0 ${num_sessions}`
  do
    cd ..
    ./train.sh -u ${usr} -t uadapt -z ${sess}
    ./test.sh -u ${usr} -t uadapt -z ${sess}

    cd ./scripts
  done
done


#!/bin/bash

users=(1 2 3 4 5 6 7 8 9 11)
sessions=(1 2 3 4 5 6 7 8 9)

# for each user do leave one session out
for usr in ${users[@]}
do
  for session in ${sessions[@]}
  do
    cd ..
    ./train-classify.sh -u $usr -s $session -t loso -z 100 # FIXME fix -z
    ./test-classify.sh -u $usr -s $session -t loso -z 100

    cd ./scripts
  done
done


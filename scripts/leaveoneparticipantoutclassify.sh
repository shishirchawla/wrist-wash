#!/bin/bash

users=(1 2 3 4 5 6 7 8 9 11)

# for each user do leave one subject out
for usr in ${users[@]}
do
  cd ..
  ./train-classify.sh -u $usr -t lopo
  ./test-classify.sh -u $usr -t lopo

  cd ./scripts
done


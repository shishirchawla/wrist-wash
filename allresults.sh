#!/bin/bash

users=(1 2 3 4 5 6 7 8 9 11)
#users=(10 12)

for usr in ${users[@]}
do
  python scripts/results.py ${usr}-pred.txt ${usr}-truth.txt
done

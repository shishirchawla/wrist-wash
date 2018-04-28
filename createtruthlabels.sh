#!/bin/bash

for filename in $(find dataset/3.11-withoutnull -name 'session_*_labels_withoutnull.csv')
do
  echo $filename
  python parse_truth_to_human.py $filename
done

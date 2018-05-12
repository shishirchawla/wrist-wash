#!/bin/bash

# script for LOPO

users=(1 2 3 4 5 6 7 8 9 11)
#users=(10 12)
sessions=(1 2 3 4 5 6 7 8 9)

# for each user
for usr in ${users[@]}
do
  cat /dev/null > $usr-pred.txt
  cat /dev/null > $usr-truth.txt

  # this will classify all sessions for the user
  python parse_htk_to_human.py hvite_user$usr.mlf

  # for each session
  for session in ${sessions[@]}
  do
    gt_file=dataset/3.11-withoutnull/${usr}/session_${session}_labels_withoutnull.csv_completesession.lab
    pred_file=htkdata/${usr}/session_${session}_labels_withoutnull.csv_completesession.rec

    gtcount=$(wc -l < $gt_file)
    predcount=$(wc -l < $pred_file)

    count_diff=$(expr ${gtcount} - ${predcount})
    echo $count_diff

    if [ "$count_diff" -gt 0 ]
    then
      pred_last_line=$(tail -n 1 $pred_file)
      for i in `seq 1 ${count_diff}`
      do
        echo $pred_last_line >> $pred_file
      done
    fi

    cat $gt_file >> $usr-truth.txt
    awk '{print $2}' $pred_file >> $usr-pred.txt

  done

done


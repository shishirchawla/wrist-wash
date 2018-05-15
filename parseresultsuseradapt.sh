#!/bin/bash

# script for LOPO

users=(1 2 3 4 5 6 7 8 9 11)
sessions=(7 8 9)
num_adapt_sessions=6

# for each user
for usr in ${users[@]}
do

  for num_sess in `seq 0 ${num_adapt_sessions}`
  do
    cat /dev/null > ${usr}-truth-${num_sess}.txt
    cat /dev/null > ${usr}-pred-${num_sess}.txt

    # this will classify all sessions for the user
    python parse_htk_to_human_useradapt.py hvite_user${usr}_ses_${num_sess}.mlf ${num_sess}

    # for each session
    for session in ${sessions[@]}
    do
      gt_file=dataset/3.11-withoutnull/${usr}/session_${session}_labels_withoutnull.csv_completesession.lab
      pred_file=htkdata/${usr}/session_${session}_labels_withoutnull.csv_completesession.rec-${num_sess}

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
      elif [ "$count_diff" -lt 0 ]
      then
        count_diff=$(expr ${predcount} - ${gtcount})
        gtac $pred_file | sed "1,${count_diff}d" | gtac > tmp && mv tmp $pred_file
      fi

      cat $gt_file >> ${usr}-truth-${num_sess}.txt
      awk '{print $2}' $pred_file >> ${usr}-pred-${num_sess}.txt

    done
  done
done


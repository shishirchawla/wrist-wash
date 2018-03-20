#!/bin/bash

# FIXME the train directory should be passed as an argument and this file needs
# to be called from another script
train_data_dir='user1-train-data'
train_steps=3
activities=(1 2 3 4 5 6 7 9 10 11 12 13 14 15)

# Train
# Cleanup old hmms
rm -rf ./model/hmm*
for i in $(seq 0 $train_steps)
do
  mkdir ./model/hmm$i
done

# Init and train hmms
for i in ${activities[@]}
do
  echo "Initialize HMM..."
# FIXME trainlist1_act_ needs to fixed
  HInit -A -D -w 1.0 -T 1 -S $train_data_dir/trainlist1_act_$i.txt -M model/hmm0 model/proto/Activity$i

  echo "Training HMMS..."
  for j in $(seq 1 $train_steps)
  do
# FIXME trainlist1_act_ needs to fixed
    HRest -A -D -T 1 -v 0.00000000001 -S $train_data_dir/trainlist1_act_$i.txt -M model/hmm$j -H model/hmm$((j-1))/Activity$i Activity$i
  done
done

# Concat hmms into one file
echo 'Compiling hmms into one file..'
hmm_file=./model/hmm$train_steps/all
counter=0

rm -f $hmm_file
for filename in ./model/hmm$train_steps/*
do
  if [ $filename != $hmm_file ] && [ $filename != "./model/hmm$train_steps/*" ]; then
    if [ $counter -eq 0 ]; then
      cp $filename $hmm_file
    else
      awk '/Activity/,/ENDHMM/' $filename >> $hmm_file
    fi
    let counter+=1
  fi
done


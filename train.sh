#!/bin/bash

# Read user and session info
while getopts ":u:s:t:z:" option
do
  case "${option}" in
    u) USR=${OPTARG};;
    s) SESSION=${OPTARG};;
    t) TYPE=${OPTARG};;
    z) UADAPTNUMSESSION=${OPTARG};;
  esac
done

train_data_dir="user${USR}-train-data"
train_steps=3
activities=(4 5 6 7 8 9 10 11 12 13 14 15 16)

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

  if [ ${TYPE} = "lopo" ] || [ ${UADAPTNUMSESSION} = "0" ]; then
    HInit -A -D -w 1.0 -T 1 -S $train_data_dir/trainlist_act_${i}.txt -M model/hmm0 model/proto/Activity$i
  elif [ ${TYPE} = "uadapt" ]; then
    HInit -A -D -w 1.0 -T 1 -S $train_data_dir/trainlist_act_${i}_ses_${UADAPTNUMSESSION}.txt -M model/hmm0 model/proto/Activity$i
  else
    HInit -A -D -w 1.0 -T 1 -S $train_data_dir/trainlist${SESSION}_act_${i}.txt -M model/hmm0 model/proto/Activity$i
  fi

  echo "Training HMMS..."
  for j in $(seq 1 $train_steps)
  do
    if [ ${TYPE} = "lopo" ] || [ ${UADAPTNUMSESSION} = "0" ]; then
      HRest -A -D -T 1 -v 0.00000000001 -S $train_data_dir/trainlist_act_${i}.txt -M model/hmm$j -H model/hmm$((j-1))/Activity$i Activity$i
    elif [ ${TYPE} = "uadapt" ]; then
      HRest -A -D -T 1 -v 0.00000000001 -S $train_data_dir/trainlist_act_${i}_ses_${UADAPTNUMSESSION}.txt -M model/hmm$j -H model/hmm$((j-1))/Activity$i Activity$i
    else
      HRest -A -D -T 1 -v 0.00000000001 -S $train_data_dir/trainlist${SESSION}_act_${i}.txt -M model/hmm$j -H model/hmm$((j-1))/Activity$i Activity$i
    fi
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

## Embedded training
#mkdir ./model/hmm4
#mkdir ./model/hmm5
#
#if [ ${TYPE} = "lopo" ]; then
#  HERest -S $train_data_dir/sessionlist.txt -H model/hmm$((train_steps))/all -M model/hmm$((train_steps+1)) hmmlist.txt
#  HERest -S $train_data_dir/sessionlist.txt -H model/hmm$((train_steps+1))/all -M model/hmm$((train_steps+2)) hmmlist.txt
#elif [ ${TYPE} = "loso" ]; then
#  HERest -S $train_data_dir/sessionlist${SESSION}.txt -H model/hmm$((train_steps))/all -M model/hmm$((train_steps+1)) hmmlist.txt
#  HERest -S $train_data_dir/sessionlist${SESSION}.txt -H model/hmm$((train_steps+1))/all -M model/hmm$((train_steps+2)) hmmlist.txt
#fi


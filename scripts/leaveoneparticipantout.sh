#!/bin/bash

users=(1 2 3 4 5 6 7 8 9 11)
#users=(1)

# for each user do leave one subject out
for usr in ${users[@]}
do
  # empty pred and truth files
  #cat /dev/null > $usr-pred.txt
  #cat /dev/null > $usr-truth.txt

  cd ..
  ./train.sh -u $usr -t lopo
  ./test.sh -u $usr -t lopo

  cd ./scripts
  #awk '/mfcc$/{nr[NR+1]}; NR in nr' ../reco_user${usr}.mlf | awk '{print $1}' >> $usr-pred.txt
  #sed -n 's/^.*_act_\([0-9]*\).*$/\1/p' ../user${usr}-test-data/testlist.txt | grep --color=never -o '[0-9]\+' | awk '{print "ACTIVITY"$0}' >> $usr-truth.txt
done



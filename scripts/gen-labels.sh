#!/bin/bash

for filename in ./*.dat; do
  echo ${filename##*/}
  labfile=$(echo ${filename##*/} | cut -f 1 -d '.').lab
  awk '{print "Activity"$NF}' $filename > $labfile
  uniq $labfile > $labfile.tmp
  mv $labfile.tmp $labfile
done

#!/bin/bash

for filename in /coc/pcba1/Datasets/public/OpportunityUCIDataset/dataset/*.dat; do
  echo ${filename##*/}
  awk '($NF != 0)' $filename > ${filename##*/}
done

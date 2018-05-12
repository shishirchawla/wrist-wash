#!/bin/bash

# 10 and 12 are the wild participants
cd ..
./train.sh -u 10 -t lopo
./test.sh -u 10 -t lopo
./test.sh -u 12 -t lopo

cd ./scripts


#!/bin/bash

find . -maxdepth 1 -iname \*.mlf -exec rm {} \;
find . -maxdepth 1 -iname *pred\*.txt -exec rm {} \;
find . -maxdepth 1 -iname *truth\*.txt -exec rm {} \;

#!/bin/bash
for filename in $1
do

grep -o '[^/]*\.js' $1 | sort -u | uniq 

done
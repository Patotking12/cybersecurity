#! /bin/bash
for filename in $1
do
 if [ -f $filename ]
 then
 echo "File exists"
 else
 echo "File does not exist"
 fi
done
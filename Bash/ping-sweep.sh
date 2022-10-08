#! /bin/bash
for ip in $(seq $2 $3)
do
ping -c 1 $1.$ip | grep "64 bytes" | cut -d " " -f  4 | cut -d ":" -f  1
done
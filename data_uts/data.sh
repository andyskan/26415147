#!/bin/bash

rm data.txt

perl -w data.pl > data.txt


rm data2.txt
filename="data.txt"

cat $filename|awk -F'|' '{printf "%s|%s|%s|%s\n",$2,$1,$4,$3}' >>data2.txt

cat data2.txt

grep -v "sananya" data2.txt > data3.txt 
cat data3.txt


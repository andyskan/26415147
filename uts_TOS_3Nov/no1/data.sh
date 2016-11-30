#!/usr/bin/bash

wget http://api.worldbank.org/v2/en/indicator/SI.POV.GINI?downloadformat=csv||unzip API_SI.POV.GINI_DS2_en_csv_v2.zip||mv API_SI.POV.GINI_DS2_en_csv_v2.csv data.csv||sed -i -e '1-4d' data.csv
awk -F '",' 'BEGIN {print $2} {count=0;total=0;}{for (i=5;i<=NF;i++) if ( /^[0-9]*$/) count+=1;total+=$i}' meong.csv


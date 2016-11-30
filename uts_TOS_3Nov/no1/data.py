#!/usr/bin/python
import csv

reader = csv.DictReader(open('meong.csv'))
#with open('API_SI.POV.GINI_DS2_en_csv_v2.csv') as f:
 #   f.readline() # ignore first line (header)
  #  mydict = dict(csv.reader(f, delimiter=','))

#print reader
#print type(reader)
average=[]
#for x in range(1960,2016):
for row in reader:
	print row['2016']


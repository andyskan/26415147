#!/usr/bin/python
import json
import urllib
rata=[]

for x in range (1,12):
  urllib.urlretrieve('http://infopangan.jakarta.go.id/api/price/series_by_location?public=1&type=market&lid=7&m='+str(x)+'&y=2015','pangan.json')
  from pprint import pprint
  with open('pangan.json') as data_file:
	data=json.load(data_file)
  for temp in data['data']:
	if(type(temp['average'==str):
      		rata.append(temp['average'])
                print temp['average'] 


print (sum(rata))





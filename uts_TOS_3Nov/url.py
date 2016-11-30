#!/usr/bin/python

import json
import urllib
import urllib2

url = 'https://aplikasi.pertanian.go.id/smshargakab/qrylapharprov.asp'
values = {'selprop':'Prov. Jawa Timur', 'selrepo':'lhk03prov','seltgl':'01','sebul':'10','seltah':'16'}
data = urllib.urlencode(values)
req = urllib2.Request(url=url, data=data)
#response = urllib2.urlopen(req)
#result = response.read()
#print result

#url = 'http://myserver/post_service'
#data = urllib.urlencode({'name' : 'joe',
#                         'age'  : '10'})
#req = urllib2.Request(url=url,data=data)
content = urllib2.urlopen(req).read()
print content

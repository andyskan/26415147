#!/usr/bin/python

import json
import urllib
import urllib2
import requests
url = 'http://sportfolio.petra.ac.id/bakabootsrap/baka/skkk.php'
#values = {'selprop':'Prov. Jawa Timur', 'selrepo':'lhk03prov','seltgl':'01','sebul':'10','seltah':'16'}
#data = urllib.urlencode(values)
#req = urllib2.Request(url, data)
#response = urllib2.urlopen(req)
#result = response.read()
#print result

requests.packages.urllib3.disable_warnings()
#requests.post(url='https://aplikasi.pertanian.go.id/smshargakab/lhk03prov.asp', data={'selprop':'Prov. Jawa Timur', 'selrepo':'lhk03prov','seltgl':'01','sebul':'10','seltah':'16'}
#)

print requests.api.request('post', url, data{'nrp':'26415147'}, json=None, verify=False)

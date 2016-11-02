#!/usr/bin/python

import json
import urllib
meong=12
urllib.urlretrieve('http://infopangan.jakarta.go.id/api/price/series_by_location?public=1&type=market&lid='+str(meong)+'7&m=11&y=2015','pangan.json')


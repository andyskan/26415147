#!/usr/bin/python

import json
import urllib
urllib.urlretrieve('http://infopangan.jakarta.go.id/api/price/series_by_location?public=1&type=market&lid=7&m=11&y=2016','pangan.json')


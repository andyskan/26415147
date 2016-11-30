#!/usr/bin/python


 json1_file = open('data.txt')
     json1_str = json1_file.read()
     json1_data = json.loads(json1_str)
json1_data = json.loads(json1_str)[0]

print json1_data

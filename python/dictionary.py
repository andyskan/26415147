#!/usr/bin/python

dict = {'Name': 'Andy', 'NRP': 26415147, 'Subject': 'TOS','Language': 'Python'}

print "Name :", dict['Name']
print "NRP  :", dict['NRP']
print "Subject :",dict['Subject']
print "Language :" ,dict['Language']

print len(dict) #check variable length
print type(dict)  #check variable type

dict2=dict.copy() #copy dictionary to dictionary 2

dict.clear() #clear dictionary

print "Dict 2",dict2

print "Dict 1",dict

print dict2.items() #return a list of dictionaries
print dict2.values() #return a list of values
dict.update(dict2)

print "Dictionary :",dict

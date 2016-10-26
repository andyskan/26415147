#!/usr/bin/python


#Learning time in python
import calendar;
import time;
#unformatted time
localtime=time.localtime(time.time())

print "Sekarang waktunya :",localtime

#timeformatting
localtime= time.asctime( time.localtime(time.time()))

print localtime

tanggalan=calendar.month(2016,10)

print "Calendar bulan oktober  ini :"

print tanggalan

#leap year
print "Is 2016 a leap year?",calendar.isleap(2016)

print time.asctime(time.localtime(time.clock()))

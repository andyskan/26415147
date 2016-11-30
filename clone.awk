#! /bin/awk -F ","
 
 BEGIN{printf"git clone git@github.com:%s/%s.git\n",$5,$2}

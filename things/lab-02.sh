#!/bin/bash
/sbin/ifconfig|grep 'inet addr'|cut -d : -f2|awk '{print $1}'|sort|xargs>>meong.txt

awk '{printf"%s ==>%s %s\n",d,$1,$2}' "d=$(date)" meong.txt

rm meong.txt


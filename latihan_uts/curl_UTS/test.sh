#!/bin/bash


curl -s http://bankmandiri.co.id/resource/kurs.asp| grep "SGD"|grep -o '[0-9]*'|xargs|awk '{printf" Harga Beli : %d\n Harga Jual : %d\n Selisih : %d\n",$1,$2,$2-$1}
'

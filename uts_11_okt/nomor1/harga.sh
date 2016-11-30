#!/bin/bash

price= curl -s http://www.elevenia.co.id/prd-apple-iphone-7-plus-black-128gb-garansi-6242166|grep "var prdPrc"|grep -o '[0-9]*'
harga=15000000
TO_ADDRESS="andysukanto.ask@gmail.com"
FROM_ADDRESS="m26415147@john.petra.ac.id"
SUBJECT="Iphone 7 price update"
BODY="Iphone 7 price is now $price"

echo "$price" > ~/iphone7price.txt
if [ $price < $harga ]; then
echo ${BODY}| mail -s ${SUBJECT} ${TO_ADDRESS} -- -r ${FROM_ADDRESS}
fi



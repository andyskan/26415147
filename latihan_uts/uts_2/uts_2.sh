#!/bin/bash
rm jawaban.txt
sort -t$'-' -k3 -k2 namelist0 <<jawaban.txt

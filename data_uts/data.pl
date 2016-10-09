#!/usr/bin/perl

@nama=();
@nrp=();
@alamat=();
@nomor=();

$number=0;
$n=<stdin>;


while ($number < $n ) {

print"NRP  	: ";$nrp[$number]=<stdin>;
print"Nama	: ";$nama[$number]=<stdin>;
print"Alamat 	: ";$alamat[$number]=<stdin>;
print"Nomor	: ";$nomor[$number]=<stdin>;

$number += 1;

}
printf"%s",$nama[1];
printf"%s",$nama[0];
$number = 0;

while ($number < $n ) {
printf"%d %s %s %d\n",$nrp[$number],$nama[$number],$alamat[$number],$nomor[$number];
$number += 1;
}



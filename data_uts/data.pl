#!/usr/bin/perl

@nama=();
@nrp=();
@alamat=();
@nomor=();
@string=();
$number=0;
$n=<stdin>;


while ($number < $n ) {

chomp($nrp[$number]=<>);
chomp($nama[$number]=<>);
chomp($alamat[$number]=<>);
chomp($nomor[$number]=<>);

$number += 1;

}

$number = 0;

while ($number < $n ) {

$string[$number] = join "|" ,($nrp[$number],$nama[$number],$alamat[$number],$nomor[$number] );
print "$string[$number]\n";
$number += 1;
}





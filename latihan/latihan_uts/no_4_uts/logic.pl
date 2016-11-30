#!/usr/bin/perl

print "Jumlah uang  :";$uang=<>;
print "Jumlah Bulan :";$bulan=<>;
print "Jumlah Bunga :";$bunga=<>;

$count = 1;
$range = 100;
$minimum = 1.5;
$maximum = 2.0;
$bonus;
while($count <=$bulan){

if($count > 1)
{
 $uang += ($uang * $bunga / 100);
   if ($count % 12 == 0)
    {
	$bunga += 5;
	print "Interest raised, current interest is $bunga%\n";
    }
  if(rand($range) <= 20)
  {
   $bonus = $minimum + rand( $maximum - $minimum );
   $uang *= $bonus;
   print " $bonus X Bonus gained\n";
  }
  if (rand($range ) <=5)
   {
    print"MONEY STOLEN\n";
    $uang = 100;
   }
}
print "Balance on the  month -$count is $uang\n";
$count += 1;
}








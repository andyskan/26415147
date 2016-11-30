
#!/usr/bin/perl

$string=<>;
$string=lc($string);
$string =~ s/[^a-z]//g;
@chars= split //,$string;
@array=();

$charsize = @chars;

foreach $chars(@chars){
	@array{$chars}++;
}

%hash = map { $_,1} @chars;
@filtered= keys %hash;



foreach $chars (@filtered){
	print"$chars= $array{$chars}\n";
}





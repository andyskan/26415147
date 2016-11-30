#!usr/bin/perl

use HTML::TableExtract;
use WWW::Mechanize;
use strict;

my $te = HTML::TableExtract->new(keep_html=>0, depth => 1, count => 1, br_translate => 0 );
$te->parse("http://stats.labs.apnic.net/ipv6/ID");

foreach $ts ($te->tables) {
   print "Table (", join(',', $ts->coords), "):\n";
   foreach $row ($ts->rows) {
      print join(',', @$row), "\n";
   }
 }

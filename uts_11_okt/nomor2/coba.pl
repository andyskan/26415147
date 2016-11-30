#!/usr/bin/perl

use strict;
use warnings;

use HTML::TableExtract;

my $content;
{
    local $/ = undef; # slurp mode
    $content = "http://stats.labs.apnic.net/ipv6/ID";
}

my $te = HTML::TableExtract->new();
$te->parse( $content );

foreach my $ts ( $te->tables() )
{
    foreach my $row ( $ts->rows() )
    {
        print join ( ";", @$row ), "\n";
    }
}

#!/usr/bin/perl -w
use strict;
my @num = 1..9;
foreach my $i(@num)
{
		foreach my $j(@num)
		{
			my $data = $i * $j;
			printf "%3d",$data,"\n";
		}
	print "\n";
}

#!/usr/bin/perl

use strict;

while ( my $line = <STDIN> )
{
	$line =~ s,http://www.pagelines.com/,/pl2/,g;
	$line =~ s,/pl2/([^/'"]+/)+,/pl2/,g;
	print $line;
}


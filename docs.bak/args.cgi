#!/usr/bin/perl

print "Content-type: text/html\n\n";

print "<body>\n";

print "<p>\n";

foreach my $k ( keys %ENV )
{
	print "$k: $ENV{$k}<br>\n";
}


























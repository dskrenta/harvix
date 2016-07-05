#!/usr/local/bin/perl

use URI::Fetch;
use Data::Dumper;

    my $re = URI::Fetch->fetch('https://en.wikipedia.org/wiki/Steve_jobs');

#my $page = $re->http_response->content();
my $page = $re->content();

print "page length = ", length($page), "\n";

# dehtml

$page =~ s/<[^>]*>//gs;
$page =~ s/\&lt;/</gs;
$page =~ s/\&gt;/>/gs;
$page =~ s/\&lt/</gs;
$page =~ s/\&gt/>/gs;
$page =~ s/\&(#\d+|[a-z0-9]+);/ /gsi;
$page =~ s/\s+/ /gs;

#my @sentences = ( $page =~ /([A-Z].*?[a-z]\.\s)/gs);
my @sentences = ( $page =~ /([A-Z][^{}\(\)]*?[a-z]\.\s)/gs);

#my @sentences = ( $page =~ /([A-Z].*?\sis\s.*?[a-z]\.\s)/g);
#my @sentences = ( $page =~ /([A-Z].*?\s(:?is|was|it|has)\s.*?[a-z]\.\s)/g);

#my @sentences = ( $page =~ /([A-Z][^{}\(\)]*?\s(?:is|was|it|has)\s[^{}\(\)]*?[a-z]\.\s)/g);

foreach my $s ( @sentences )
{
	next if $s !~ /(\sis\s|\swas\s)/;
	next if length($s) > 200;
	next if $s =~ /(Wikipedia)/;

	print "Presumed Fact: $s\n\n";
}

if ( ! @sentences )
{
	print Dumper($res);
}


#$page =~ [A-Z].*?[a-z]\.\s;

#print $page;


#!/usr/bin/perl

use strict;
use Data::Dumper;
use Yahoo::Search AppId      => 'Bobs Fish Mart',
                 Count      => 100,
                 AllowAdult => 0,
                 PostalCode => 94070;

my $query;
if ( $ENV{QUERY_STRING} =~ /\bq=([^\&\?]*)/ )
{
	$query = $1;
}

print "Content-type: text/html\n\n";
print <<EOF
<html>
<head>
<title>Harvix</title>
</head>
<body>

EOF
;


print "<p>Search Results: \"$query\"<p>\n";


#print join "<p>", Yahoo::Search->HtmlResults( Doc => $query );
print join "<p>", Yahoo::Search->HtmlResults( Image => $query );
print "<p><center>&copy; 2010 Harvix, inc.</center> </p>\n";


#!/usr/bin/perl

#HTTP/1.1 200 OK
#Server: Apache/2.2.15 (CentOS)
#X-CreationTime: 0.063
#Last-Modified: Sun, 20 Sep 2015 10:23:14 GMT
#Content-Type: application/json; charset=UTF-8
#Expires: Sun, 20 Sep 2015 10:23:14 GMT
#Cache-Control: max-age=0, no-cache
#Pragma: no-cache
#Date: Sun, 20 Sep 2015 10:23:14 GMT
#Connection: keep-alive
#Set-Cookie: DT=1442744594:16503:365-c7; path=/; expires=Fri, 01-Jan-2020 00:00:00 GMT; domain=.wunderground.com

use strict;

print "Content-Type: text/html\n";
print "Access-Control-Allow-Origin: *\n";
print "Access-Control-Allow-Credentials: true\n";
print "\n";

sub parse_query
{   
        my $query = $ENV{QUERY_STRING} || shift || 1;
    
        $query =~ s/\+/ /g;
        #$query =~ s/q=//;
    
        return $query;
}

my $query = parse_query();

die if $query =~ /\//;

open(FILE, "</home/david/harvix/docs/weather/weather/$query" );
while (my $line = <FILE> )
{
	print $line;
}
close(FILE);



#!/usr/bin/perl

use strict;
use WebService::Yahoo::BOSS;
use Data::Dumper;

#Yahoo test API script

my $ckey = "dj0yJmk9UHowSk13Yzd2bG1DJmQ9WVdrOU0wOXVXRlJzTkhNbWNHbzlNQS0tJnM9Y29uc3VtZXJzZWNyZXQmeD05MA--";
my $csecret = "de55df25ba316c3683395ed0fdacc69565475958";

my $Boss = WebService::Yahoo::BOSS->new( ckey => $ckey, csecret => $csecret );

my $response = $Boss->Web(q => 'steve jobs', count => 20);

#print $response->totalresults;

print Dumper($response->results);

#foreach my $value ($response->results)
#{
#	print Dumper($value);
#	$count ++;
#}

sub header
{
	print qq{
	};
}

sub footer
{
	print qq{
	};
}

sub urlencode
{
    my $url = shift;

    $url =~ s/([^A-Za-z0-9\-_.!~*\'()])/$escapes{$1}/ge if defined $url;
    return $url;
}

sub urldecode
{
    my $url = shift;

    $url =~ tr/+/ / if defined $url;
    $url =~ s/%([0-9A-Fa-f]{2})/chr(hex($1))/eg if defined $url;

    return $url;
}

sub parse_query
{
        my $query = $ENV{QUERY_STRING} || shift || 1;

        $query =~ s/q=//;
        $query = urldecode($query);
        #$query =~ s/\+/ /g;
        $query =~ s/[\[\]\(\)\.\?]/ /g;
        $query =~ s/^\s*//;
        $query =~ s/\s*$//;
        $query =~ s/\s+/ /g;
        
        return $query;
}














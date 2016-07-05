#!/usr/bin/perl

use strict;
use WebService::Yahoo::BOSS;
use Data::Dumper;

#Yahoo test API script

my $ckey = "dj0yJmk9UHowSk13Yzd2bG1DJmQ9WVdrOU0wOXVXRlJzTkhNbWNHbzlNQS0tJnM9Y29uc3VtZXJzZWNyZXQmeD05MA--";
my $csecret = "de55df25ba316c3683395ed0fdacc69565475958";

my $Boss = WebService::Yahoo::BOSS->new( ckey => $ckey, csecret => $csecret );

my $response = $Boss->Images(q => 'steve jobs', count => 20);

#print $response->totalresults;

print Dumper($response->results);

#foreach my $value ($response->results)
#{
#	print Dumper($value);
#	$count ++;
#}



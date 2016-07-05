#!/usr/bin/perl

use strict;

# see http://search.cpan.org/~makamaka/JSON-2.57/lib/JSON.pm

use JSON;
use URI::Fetch;
use Data::Dumper;

my $query = "foo";

my $json_page = URI::Fetch->fetch("http://blekko.com/api/p1?q=$query&auth=c31c6fd0");
my $json_text = $json_page->content();
my $json = decode_json( $json_text );

print Dumper($json), "\n";

if ( ! defined $json )
{
    print "no results\n";
    exit(0);
}

if ( ! defined $json->{img_map} )
{
    print "no tags\n";
    exit(0);
}

        print Dumper($json->{img_map});

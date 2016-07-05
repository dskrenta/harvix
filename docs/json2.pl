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

# print Dumper($json), "\n";

if ( ! defined $json )
{
    print "no results\n";
    exit(0);
}

if ( ! defined $json->{tags} )
{
    print "no tags\n";
    exit(0);
}

foreach my $tag ( @{ $json->{tags} } )
{
    my $category = $tag->{name};
    my $results = $tag->{results};

    my $num = scalar @{ $results };
    print "=== $category ($num results):\n\n";

    foreach my $result ( @{ $results } )
    {

	if(0)
        {
                foreach my $key ( keys %$result )
                {
                        print "$key => ", Dumper( $result->{$key} );
                }
        }
	else
	{
		my $title = $result->{'t'};
		print"TITLE=> $title\n";
		my $url = $result->{'u'};
		my $snippet = $result->{'s'};
		print"SNIPPET=> $snippet\n";
		print"URL=> $url\n";
		print"\n\n";
		#print Dumper($result);
	}

    }
    print "\n\n";
}

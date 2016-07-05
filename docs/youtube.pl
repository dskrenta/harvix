#!/usr/bin/perl

use strict;
use warnings;
use WebService::GData::YouTube;
use Data::Dumper;

my $q = shift(@ARGV);

$q = 'iphone 5' if $q eq '';

print "query = $q\n";

my $yt = new WebService::GData::YouTube();

#my $videos = $yt->get_top_rated_videos('JP','Comedy');


$yt->query()->q($q)->limit(10,0);
#$yt->query($q);

my $videos = $yt->search_video();

foreach my $video (@$videos) {
   print $video->title,"\n";
   print $video->description,"\n";
	print "\n";
}

#print Dumper($videos);


#!/usr/bin/perl

use strict;
use warnings;
use WebService::GData::YouTube;
use Data::Dumper;

print "Content-type: text/html\n\n";

my $q = shift(@ARGV);

$q = 'hr puff n stuff' if $q eq '';

print "query = $q<p>\n";

my $yt = new WebService::GData::YouTube();


$yt->query()->q($q)->limit(10,0);

my $videos = $yt->search_video();

foreach my $video (@$videos) {
my $thumb = $video->thumbnails->[0];
$thumb = $video->thumbnails->[0] if !defined $thumb;
         
print "<table><tr><td>";   
 print "<a href=\"http://www.youtube.com/watch?v=", $video->video_id, "\">";
        print "<img src=\"", $thumb->url, "\" height=", $thumb->heigth, " width=", $thumb->width, "></a>\n";
print"</td><td>";
print $video->title, "<br>\n<p>";
   print $video->description,"<br>\n";
print"</td></tr></table>";
    
   	 print "<p>\n";

    # there are three thumbnails, 0 1 2. 0 is the smallest, 2 is the biggest
    # let's take 1 by default, if it's not there for some reason, take the small one

}

exit(0);

        #!/usr/bin/perl -w

        use strict;
        use warnings;

        use WWW::Yahoo::Movies;
	



print <<EOF
<html>
<head>
<title>Harvix Search</title>
<link rel="stylesheet" href="/style.css" type="text/css">
</head>
<body>




<a href="index.html">Home</a>
|
<a href="search.html">Harvix Search</a>
|
<a href="man.html">About</a>
|
<a href="http://aple100.blogspot.com/">Blog</a>
|
<a href="lobberhead.com">Lobberhead</a>
|
<a href="harnews.html">Top News</a>
|
<a href="links.html">Links</a>


<hr></hr>
<center>
<h1>Search Images</h1>
<h3>2.0 beta</h3>

<form action="/video.cgi" method="GET">
<input size="45" name="q" value="">
<input type=submit value="Search">
</form>
<p>
<a href="y2search.html">Web Search</a>|<a href="videos.html">Search Videos</a>|<a href="images.html">Search Images</a>|<a href="blogs.html">Search Blogs</a>|<a href="jokes.html">Search Jokes</a>
<p>





</center>
EOF
;






        my $title = shift || 'troy';

        my $matched = get_movie_info($title, 1);

        for(@$matched) {
                print "\nGet [$_->{title}] ...\n";
                get_movie_info($_->{id});
        }

        sub get_movie_info {
                my $title = shift;
                my $ret_match = shift || 0;
                
                my $ym = new WWW::Yahoo::Movies(id => $title);

                print "Get info about [$title] ...";

                print "\n\tID: ".$ym->id;
                print "\n\tTITLE: ".$ym->title;
                print "\n\tYEAR: ".$ym->year;
                print "\n\tMPAA: ".$ym->mpaa_rating;
                print "\n\tCOVER: ".$ym->cover_file;
                print "\n\tPLOT: ".substr($ym->plot_summary, 0, 90)." ...";
                print "\n\tDATE: ".$ym->release_date;
                print "\n\tDISTR: ".$ym->distributor;
                print "\n\tGENRES: ".join(", ", @{ $ym->genres }) if $ym->genres;

                return $ym->matched if $ret_match;
        }     

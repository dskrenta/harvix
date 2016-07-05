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

<form action="/ysearch.cgi" method="GET">
<input size="45" name="q" value="">
<input type=submit value="Search">
</form>
<p>
<a href="y2search.html">Web Search</a>|<a href="videos.html">Search Videos</a>|<a href="images.html">Search Images</a>|<a href="blogs.html">Search Blogs</a>|<a href="jokes.html">Search Jokes</a>
<p>





</center>
EOF
;


print "<p>Search Results: \"$query\"<p>\n";


#print join "<p>", Yahoo::Search->HtmlResults( Doc => $query );
print join "<p>", Yahoo::Search->HtmlResults( Image => $query );
print "<p><center>&copy; 2010 Harvix, inc.</center> </p>\n";


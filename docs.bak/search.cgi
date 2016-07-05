#!/usr/bin/perl

# magic - do not change
print "Content-type: text/html\n\n";
$page = $ENV{QUERY_STRING} || shift || 1;
# end magic


#foreach my $k ( keys %ENV )
#{
#	print "$k: $ENV{$k}<br>\n";
#}

my $query;
if ( $ENV{QUERY_STRING} =~ /\bq=([^\&\?]*)/ )
{
	$query = $1;
}

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
<h1>Jokes Search</h1>

<form action="/search.cgi" method="GET">
<input size="45" name="q" value="">
<input type=submit value="Search">
</form>
<p>
<a href="y2search.html">Web Search</a>|<a href="videos.html">Search Videos</a>|<a href="images.html">Search Images</a>|<a href="blogs.html">Search Blogs</a>|<a href="jokes.html">Search Jokes</a>
<p>





</center>
EOF
;







print "<p>You searched for: \"$query\"<p>\n";

# Now let's do a little searching...o

open(FILE, "</usr/local/lib/yukko.dat");

my $joke;

print "<pre>\n";

while ( my $line = <FILE> )
{
	chomp($line);
	if ( $line eq '/' )
	{
		if ( $joke =~ /\b\Q$query\E\b/is )
		{
			$joke =~ s/\b(\Q$query\E)\b/<b>$1<\/b>/gsi;

			print $joke, "\n* * *\n\n";
		}

		$joke = '';
	}
	else
	{
		$joke .= $line . "\n";
	}
}

print "</pre>\n";

close(FILE);


print "<p><center>&copy; 2010 Harvix, inc.</center> </p>\n";

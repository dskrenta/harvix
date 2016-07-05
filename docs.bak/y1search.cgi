#!/usr/bin/perl

use strict;

# magic - do not change
print "Content-type: text/html\n\n";
my $page = $ENV{QUERY_STRING} || shift || 1;
# end magic

print <<EOF

<html>
<head>
<title>
harvix
</title>
<link rel="stylesheet" href="/style.css" type="text/css">
<style type="text/css">

div.footer
{
color:#a0a0a0;
}

div.bar
{
float:right;
}


div.q
{
float:right;
}

</style>
</head>
<body>
<div class="bar">
<a href="signi.html">sign in</a> &middot <a href="signu.html">sign up</a>
</div>

<b>search bar:</b>  <a href="y2search.html">web</a> &middot <a href="ysearch.html">images</a> &middot <a href="search.html">jokes</a>
<hr></hr>

<p>
<p>
<img src="http://harvix.com/harvix-logo.png"/>
<p>
<p>
<form action="/y1search.cgi" method="get">
<input size="60" name="q" value="">
<input type=submit value="harvix search">
</form>
<b>examples:</b> <a href="http://harvix.com/y1search.cgi?q=iphone">iphone</a> &middot <a href="http://harvix.com/y1search.cgi?q=blekko">blekko</a>





</center>
EOF
;
    
print"<center>";


#print "Query was: $page<br>\n";
$page =~ s/q=//;
#print "Now query is: $page<p>\n";

#start args

 use Yahoo::Search;
 my @Results = Yahoo::Search->Results(Doc => $page,
                                      AppId => "YahooDemo",
                                      # The following args are optional.
                                      # (Values shown are package defaults).
                                      Mode         => 'all', # all words
                                      Start        => 0,
                                      Count        => 100,
                                      Type         => 'any', # all types
                                      AllowAdult   => 0, # no porn, please
                                      AllowSimilar => 0, # no dups, please
                                      Language     => undef,
                                     );
 warn $@ if $@; # report any errors

#end args




#Resualts statments

 for my $Result (@Results)
 {
#     printf "Result: #%d<br>\n",  $Result->I + 1,
#     printf "Url:<a href=\"%s\">%s</a><br>\n",       $Result->Url, $Result->Url;
#     printf "%s<br>\n",           $Result->ClickUrl;
#     printf "Summary: %s<br>\n",  $Result->Summary;
#     printf "Title: %s<br>\n",    $Result->Title;
#     printf "In Cache: %s<br>\n", $Result->CacheUrl;


	

	print"<hr></hr>";
	print "###";
	print "<a href=", '"', $Result->Url, '">', $Result->Title, "</a><br>\n";
	print $Result->Summary, "<br>\n";
	 print "Url:<a href=\"%s\">%s</a><br>\n",       $Result->Url, $Result->Url;
	
	
     print "<p>\n";
 }


print" </center> ";


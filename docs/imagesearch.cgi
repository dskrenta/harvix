#!/usr/bin/perl

use Data::Dumper;

use strict;

my %escapes;
for (0..255)
{
    $escapes{chr($_)} = sprintf("%%%02X", $_);
}
$escapes{' '} = '+';

sub urlencode
{
    my $url = shift;

    $url =~ s/([^A-Za-z0-9\-_.!~*\'()])/$escapes{$1}/ge if defined $url;
    return $url;
}


# magic - do not change
print "Content-type: text/html\n\n";
my $page = $ENV{QUERY_STRING} || shift || 1;
# end magic

$page =~ s/\+/ /g;
$page =~ s/q=//;

my $cat;
my $orig_page = $page;
if ( $page =~ /^(.*)(?::|%3A)([a-z]+)(.*)$/i )
{
	$page = "$1 $3";
	$cat = $2;
}
$orig_page =~ s/%3A/:/g;

print <<EOF
<html>
<head>
<title>Harvix | Search</title>
<style type="text/css">
div.page {
        margin:0 auto;
        width:990px;
        text-align:center;
}
a:link {color:#1a54e1; font-size:14px;}    /* unvisited link */
a:visited {color:#1a54e1;} /* visited link */
a:active {color:#1a54e1;}  /* selected link */
body { font-size: 13px; font-family: Arial, sans-serif; font-size: normal; line-height: normal; }
div.1footer{color:gray;}
div.bar{float:right;}
div.footer{clear:both;text-align:center;}
div.t{text-align:center;}
body {background-color:white;}
div.header{font-size:60px;}
div.hi{width:100%; padding:0px; border:1px solid:#ffffff; margin:0px; background-color:#BDBDBD;}
div.h{font-size:20px;}
</style>
</head>
<body style="margin:0px;">
<form action="imagesearch.cgi" method="get">
    <input id="search_box" autocomplete="off" spellcheck="false" type="text" name="q" style="font-size: 16pt" size="60" value="$page" class="field" style="width:429px;margin-bottom: 10px;" /><br />
</form>
EOF
;


#print "query = $page<br>\n";
#print "cat = $cat<br>\n";

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

 my @Images = Yahoo::Search->Results(Image => $page,
                                      AppId => "YahooDemo",
                                      Count        => 10,
                                     );
 warn $@ if $@; # report any errors

my @dym = Yahoo::Search->Results( Spell => $page, AppId => "YahooDemo" );
if ( scalar @dym > 0 )
{
	my $res = shift @dym;
	my $qq = $res->Term;
	$qq =~ s/ /+/g;
	print "Did you mean: <a href=\"/y1search.cgi?q=$qq\">", $res->Term, "</a> ?<p>\n";
}



#end args


#Resualts statments

#print "results = ", scalar(@Images), "<p>\n";

print "<ol>\n";
show_results(4);
show_images(4);
show_results(50);
print "</ol>\n";





print <<EOF
<form action="/imagesearch.cgi" method="get">
<input size="60" name="q" value="$orig_page">
<input type=submit value="search the web">
</form>
EOF
;
               

sub show_images
{
	my ( $howmany ) = @_;

	$howmany = 10 if $howmany < 1;

	while ( $howmany > 0 && @Images )
	{
		my $Result = shift @Images;
		$howmany--;

		my $thumbnail = $Result->{Thumbnail}->{Url};
		my $width = $Result->{Thumbnail}->{Width};
		my $height = $Result->{Thumbnail}->{Height};
		my $url = $Result->Url;
				
		print"Image Results:\n";
		print "<a href=\"$url\"><img src=\"$thumbnail\" width=$width height=$height></a>\n";
		print "<a href=\"$url\"><img src=\"$thumbnail\" height=100></a>\n";
		#print "<p>\n";
		#print "$url\n";
		print "\n";
        }
}


sub show_results
{
        my ( $howmany ) = @_;

        $howmany = 10 if $howmany < 1;

        while ( $howmany > 0 && @Results )
        {
                my $Result = shift @Results;
                $howmany--;

		print"<hr></hr>";

		print "<p>\n";
		print" <div>";
		print "<p>\n";
	print"<li>";       
	 print "<a href=", '"', $Result->Url, '">', $Result->Title, "</a><br>\n";
	

		print $Result->Summary, "<br>\n";
		 print "url:<a class=urlbar href=\"%s\">%s</a><br>\n",       $Result->Url, $Result->Url;


	my $etitle = $Result->Title;
	my $eurl = urlencode( $Result->Url );

	my $title = $Result->Title;
	my $url = $Result->Url;

	# <a class="a2a_dd" href="http://www.addtoany.com/share_save?linkurl=http%3A%2F%2Fharvix.com&amp;linkname=Harvix.com">Share</a>

		print <<EOF
<!-- AddToAny BEGIN -->
<div class="a2a_kit a2a_default_style">
<a class="a2a_dd" href="http://www.addtoany.com/share_save?linkurl=$eurl&amp;linkname=$etitle">Share</a>
<span class="a2a_divider"></span>
<a class="a2a_button_facebook"></a>
<a class="a2a_button_twitter"></a>
<a class="a2a_button_email"></a>
<a class="a2a_button_google_gmail"></a>
<a class="a2a_button_google_buzz"></a>
<a class="a2a_button_yahoo_mail"></a>
<a class="a2a_button_aol_mail"></a>
<a class="a2a_button_digg"></a>
<a class="a2a_button_live"></a>
<a class="a2a_button_yahoo_messenger"></a>
<a class="a2a_button_yahoo_buzz"></a>
<a class="a2a_button_myspace"></a>
<a class="a2a_button_hotmail"></a>
<a class="a2a_button_blogger_post"></a>
</div>
<script type="text/javascript">
var a2a_config = a2a_config || {};
a2a_config.linkname = "$title";
a2a_config.linkurl = "$url";
</script>
<script type="text/javascript" src="http://static.addtoany.com/menu/page.js"></script>
<!-- AddToAny END -->
<p>
EOF
;

	#a2a_config.linkname = "Harvix.com";
	#a2a_config.linkurl = "http://harvix.com";
		
	     print "\n";
		print" </div>";
	}
}




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
<title>
Harvix
</title>
<link rel="shortcut icon" href="http://harvix.com/harvix-logo-2.png" type="image/x-icon" /> 
<style type="text/css"> 
a:link {color:#1a54e1; text-decoration:none;}  
a:visited {color:#1a54e1; text-decoration:none;}
a:hover {color:#1a54e1; text-decoration:underline;}
body { font-size: 13px; font-family:  Arial, sans-serif; font-size: normal; line-height: normal; margin: 0; padding: 0; } 
div.header{font-size:150px;}
div.hi{width:100%; padding:0px; border:1px solid:#ffffff; margin:0px; background-color:#BDBDBD;}
div.1footer{color:gray;}
div.bar{float:right;}
div.footer{clear:both;text-align:center;}
div.t{text-align:center;}
div.large{font-size:20px;}
div.h{font-size:18px;}
div.t{font-size:15px;}
div.o{width:20%; padding:2px; border:1px solid:#ffffff; margin:0px; background-color:#b31c1c;}
div.center{text-align:center;}
div.ex{width:80%; padding:2px; border:1px solid black;  margin:0px; -moz-border-radius: 15px; border-radius: 15px; background-color: white;}
			/* The CSS Code for the menu starts here */
			#menu {
				font-family: Arial, sans-serif;
				font-weight: bold;
				text-transform: uppercase;
				margin: 0;
				padding: 0;
				list-style-type: none;
				background-color: #eee;
				font-size: 17px;
				height: 50px;
				border-top: 2px solid #eee;
				border-bottom: 2px solid #ccc;
			}
			#menu li {
				float: left;
				margin: 0;				
			}
			#menu li a {
				text-decoration: none;
				display: block;
				padding: 0 20px;
				line-height: 40px;
				color: #666;
			}
			#menu li a:hover, #menu li.active a {
				background-color: #f5f5f5;
				border-bottom: 2px solid #DDD;
				color: #999;
			}
			#menu_wrapper ul {margin-left: 0px;}
			#menu_wrapper {padding: 0 0 0 0; background: url(images/grey.png) no-repeat right;}
			#menu_wrapper div {float: left; height: 44px; width: 0px; background: url(images/grey.png) no-repeat left;}
			
			/* Black Menu */
			#menu_wrapper.black ul {
				border-top: 2px solid #333;
				border-bottom: 2px solid #000;
				background: #333;}
			#menu_wrapper.black a {color: #CCC;}
			#menu_wrapper.black li a:hover, #menu_wrapper.black li.active a {color: #999; background: #555; border-bottom: 2px solid #444;}
			#menu_wrapper.black {background: url(images/black.png) no-repeat right;}
			#menu_wrapper.black div {background: url(images/black.png) no-repeat left;}
</style>

</head>
<body>
<div id="menu_wrapper" class="black"> 
		<div class="left"></div> 
			<ul id="menu"> 
				
				<li><a href="index.html">Search</a></li> 
				<li><a href="social.html">Social</a></li> 
				<li><a href="games.html">Games</a></li> 
 
			</ul> 
		</div> 

<a href="index.html"><div class="header"><span style="color:black;">Har</span><span style="color:#b31c1c;">vix</span></div></a> <div class="bar">




<form action="/y1search.cgi" method="get">
<input size="60" name="q" value="$page">
<input type=submit value="Harvix Search">
</form>
</div>



</center>
EOF
;



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

print" <div class=\"wi\">";

 for my $Result (@Results)
 {
#     printf "Result: #%d<br>\n",  $Result->I + 1,
#     printf "Url:<a href=\"%s\">%s</a><br>\n",       $Result->Url, $Result->Url;
#     printf "%s<br>\n",           $Result->ClickUrl;
#     printf "Summary: %s<br>\n",  $Result->Summary;
#     printf "Title: %s<br>\n",    $Result->Title;
#     printf "In Cache: %s<br>\n", $Result->CacheUrl;


        print "<p>\n";
        print" <div>";
        print "<p>\n";
print"<ol>";
print"<li>";       
 print "<a href=", '"', $Result->Url, '">', $Result->Title, "</a><br>\n";
print" <p> \n";

        print $Result->Summary, "<br>\n";
         print "url:<a class=urlbar href=\"%s\">%s</a><br>\n",       $Result->Url, $Result->Url;

print"</ol>";

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
EOF
;

#a2a_config.linkname = "Harvix.com";
#a2a_config.linkurl = "http://harvix.com";
	
     print "\n";
        print" </div>";
 }

print" </div> ";

print" \n";



print <<EOF
<form action="/y1search.cgi" method="get">
<input size="60" name="q" value="$page">


<input type=submit value="search the web">
</form>
EOF
;
               

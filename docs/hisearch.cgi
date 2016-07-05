#!/usr/bin/perl

use strict;

use Data::Dumper;
use WebService::Blekko;

my %escapes;
setup_escapes();

print "Content-type: text/html\n\n";

my $query = parse_query();

my $blekko = WebService::Blekko->new( auth => 'c31c6fd0', );


my $res = $blekko->query( $query );

#if ( $res->error ) ...

print_header();

while ( my $r = $res->next ) {
	#print $r->title, "<br>\n";
	#print $r->snippet, "<br>\n";
	#print $r->url, "<br>\n";
	#print "<br>\n";

 	print "<a href=", '"', $r->url, '">', $r->title, "</a><br>\n";

	#print $r->snippet, "<br>\n";
	my $snippet = $r->snippet;
	if ( length($snippet) > 350 )
	{
		$snippet = substr($snippet, 0, 350);
		$snippet =~ s/\s[^\s]*$//;
		$snippet .= ' ...';
	}
	print $snippet, "<br>\n";

	print "<span style=\"color:green;\">";
	print $r->url, "<br>\n";
	print "</span>";
	print "<p>\n";
	
	EOF
	;


print_footer();

sub setup_escapes
{
	for (0..255)
	{
	    $escapes{chr($_)} = sprintf("%%%02X", $_);
	}
	$escapes{' '} = '+';
}

sub urlencode
{
    my $url = shift;

    $url =~ s/([^A-Za-z0-9\-_.!~*\'()])/$escapes{$1}/ge if defined $url;
    return $url;
}

sub urldecode
{
    my $url = shift;

    $url =~ tr/+/ / if defined $url;
    $url =~ s/%([0-9A-Fa-f]{2})/chr(hex($1))/eg if defined $url;

    return $url;
}

sub parse_query
{
	my $query = $ENV{QUERY_STRING} || shift || 1;

	$query =~ s/q=//;
	$query = urldecode($query);
	$query =~ s/\+/ /g;

	return $query;
}

sub print_header
{
print <<EOF
<html>
<head>
<title>Harvix</title>
<style type="text/css">
a:link {color:#1a54e1; text-decoration:none;}  
a:visited {color:#1a54e1; text-decoration:none;}
a:hover {color:#1a54e1; text-decoration:underline;}
body { font-size: 13px; font-family:  Arial, sans-serif; font-size: normal; line-height: normal; }
div.header{font-size:200px;}
div.hi{width:100%; padding:3px; padding-left: 10px; border:1px solid:#ffffff; margin:0px; background-color:#BDBDBD;}
div.1footer{color:gray;}
div.bar{float:right; padding-right: 15px; }
div.footer{clear:both;text-align:center;}
div.t{text-align:center;}
div.large{font-size:100px;}
body {background-color:white;}
div.h{font-size:20px;}
div.t{font-size:17px;}
#sideCol-l { width: 180px; padding-right: 10px; float: left; border-right: 1px solid #edf4fb;  margin-right:15px;}
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
<body style="margin:0px;">
<div id="menu_wrapper" class="black"> 
		<div class="left"></div> 
			<ul id="menu"> 
				
				<li><a href="index.html">Search</a></li> 
				<li><a href="social.html">Social</a></li> 
				<li><a href="games.html">Games</a></li> 
 
			</ul> 
		</div> 
<table width="100%" cellpadding="0" cellspacing="0">
<tr><td colspan=5><span class="hh">

<div class="h">
<div class="hi">
<div class="bar">
<a href="help.html">Help</a> | <a href="login.html">Login</a>
</div>
<b>Web</b> | <a href="images.html">Images</a> | <a href="video.html">Video</a>
</div>
</div>

</span></td><td></td></tr>
<tr height="30"><td></td></tr>

<tr>
<td width=15></td>

<td width=175 valign=top>
<div style="font-size:36pt"><b>
<span style="color:black;">Har</span><span style="color:#b31c1c;">vix</span></b>
</div>
Checkout:
<p>
<b>Web</b>
<p>
<a href="images.html">Images</a>
<p>
<a href="video.html">Video</a>
<p>
<a href="news.html">News</a>
<p>
<a href="shopping.hmtl">Shopping</a>
</td>
<td>

<table width="100%" cellpadding="0" cellspacing="0">

<tr><td valign=top>

<form action="hsearch.cgi" method="get">
<input style="font-size: 18pt" size="40" name="q" value="$query">
<input type=submit style="font-size: 18pt" value="Search"> 
</div>
</form>
<p>
&nbsp;
<p>
EOF
;

}

sub print_footer
{
print <<EOX

</td>

<td width=100>&nbsp;</td>

<td valign=top align=right width=175>
Web Results from Blekko<br>
<p>
&nbsp;
<p>
&nbsp;
<p>
&nbsp;
<p>

<script type="text/javascript"><!--
google_ad_client = "ca-pub-7936635528512943";
/* harvix */
google_ad_slot = "3595106781";
google_ad_width = 160;
google_ad_height = 600;
//-->
</script>
<script type="text/javascript"
src="http://pagead2.googlesyndication.com/pagead/show_ads.js">
</script>

</td>

<td width=15>&nbsp;</td>

</tr>

</table>
</td></tr></table>

<p>
<p>
<p>
<p>
<center>
<div class="t">
<a href="about.html.html">About</a>&nbsp;&middot;
<a href="help.html">Help</a>&nbsp;&middot;
<a href="jobs.html">Jobs</a>&nbsp;&middot;
<a href="co.html">Contact</a>&nbsp;&middot;
<a href="terms.html">Terms &amp; Conditions</a>&nbsp;&middot;
<a href="privacy.html">Privacy Policy - We don't track you!</a>&nbsp;
</div>
<p>
<span style="color:gray;">&copy; Harvix inc. | <a href="privacy.html">Privacy</a> - We don't track you!</span>
</center>
</body>

EOX
;
}



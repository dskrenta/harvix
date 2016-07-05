#!/usr/bin/perl

use strict;

use Data::Dumper;
use WebService::Blekko;
use Encode;

my %escapes;
setup_escapes();

print "Content-type: text/html\n\n";


sub utf8_on
{
    my($str) = @_;

    if( $str )
    {
        String::Charset::utf8_clean( $str );

        Encode::_utf8_on($str);

        if(! Encode::is_utf8($str, 1) )
        {
            Encode::_utf8_off($str);
        }
    }

    return $str;
}

=head2 utf8_off($string)

Unconditionally marks a string as not UTF-8. If the string isn't
valid UTF-8, chaos is in your immediate future.

=cut

sub utf8_off
{
    my( $str ) = @_;

    if( $str )
    {
        Encode::_utf8_off($str);
    }

    return $str;
}




print"
<div id=\"fb-root\"></div>
<script>(function(d, s, id) {
  var js, fjs = d.getElementsByTagName(s)[0];
  if (d.getElementById(id)) return;
  js = d.createElement(s); js.id = id;
  js.src = \"//connect.facebook.net/en_US/all.js#xfbml=1\";
  fjs.parentNode.insertBefore(js, fjs);
}(document, 'script', \'facebook-jssdk\'));</script>
\n";


my $query = parse_query();

my $wiki = wiki_query($query);

my $blekko = WebService::Blekko->new( auth => 'c31c6fd0', );


my $res = $blekko->query( $query );

#if ( $res->error ) ...


print_header();

	if ( $wiki )
	{
	    my ( $wiki_best, $wiki_rank, $wiki_fnam, $wiki_title, $wiki_page, $wiki_image, $wiki_url ) = @$wiki;

		utf8_off($wiki_title);
		utf8_off($wiki_page);
		utf8_off($wiki_url);

		print "<img src=\"$wiki_image\"><br>\n" if $wiki_image ne '';
		print "<a href=", '"', $wiki_url, '">', $wiki_title, "</a><br>\n";
		print $wiki_page, "<br>\n";
		print "<span style=\"color:green;\">";
		print $wiki_url, "<br>\n";
		print "</span>";
		print "<p>\n";
	}

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
	#print "<div class=\"fb-like\" data-href=\"$r->url\" data-send=\"false\" data-width=\"450\" data-show-faces=\"false\"></div>\n";
	print "<p>\n";
}

print_footer();

sub wiki_query
{
	my ( $query ) = @_;

	$query =~ s/^\s*//;
	$query =~ s/\s*$//;
	$query =~ s/\s+/ /g;

	$query =~ s/^(who|what|where|when|why|how) (is|was|do|did) (the )?//i;

	my ( $wiki_rank, $wiki_url, $wiki_fnam, $wiki_title, $wiki_page, $wiki_image );

	my @wiki_res;

	open(DB, "</home/david/harvix/wikidb2.out") or warn "can't read /home/david/harvix/wikidb2.out";

	while ( my $line = <DB> )
	{
	    chomp($line);
	    ( $wiki_rank, $wiki_fnam, $wiki_title, $wiki_page, $wiki_image ) = split( "\t", $line );
	    $wiki_url = "http://en.wikipedia.org/wiki/$wiki_fnam";
	    $wiki_title =~ s/_/ /g;

	    if ( $wiki_title =~ /^$query$/i )
	    {
		push @wiki_res, [ 1, $wiki_rank, $wiki_fnam, $wiki_title, $wiki_page, $wiki_image, $wiki_url ];
	    }
	    elsif ( $wiki_title =~ /\b$query\b/i )
	    {
		push @wiki_res, [ 2, $wiki_rank, $wiki_fnam, $wiki_title, $wiki_page, $wiki_image, $wiki_url ];
	    }
	    else
	    {
		my $q2 = $query;
		$q2 =~ s/ /\\b\.\*\\b/g;

		if ( $wiki_title =~ /\b$q2\b/i )
		{
		    push @wiki_res, [ 3, $wiki_rank, $wiki_fnam, $wiki_title, $wiki_page, $wiki_image, $wiki_url ];
		}
		elsif ( ( $wiki_title . ' ' . $wiki_page ) =~ /\b$query\b/i )
		{
		    push @wiki_res, [ 4, $wiki_rank, $wiki_fnam, $wiki_title, $wiki_page, $wiki_image, $wiki_url ];
		}
		elsif ( ( $wiki_title . ' ' . $wiki_page ) =~ /\b$q2\b/i )
		{
		    push @wiki_res, [ 5, $wiki_rank, $wiki_fnam, $wiki_title, $wiki_page, $wiki_image, $wiki_url ];
		}
	    }

	    ( $wiki_fnam, $wiki_title, $wiki_page, $wiki_image, $wiki_url ) = undef;
	}
	close(DB);

	@wiki_res = sort { $a->[0] <=> $b->[0] or $b->[1] <=> $a->[1] } @wiki_res;

	return if ! scalar @wiki_res;
	return $wiki_res[0];
}

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

div.po{width:100%; padding:2px; border:1px solid:gray; margin:0px; background-color:gray;}



</style>
</head>


<body style="margin:0px;">

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
<input style="font-size: 17pt" size="40" name="q" value="$query"><input type=submit style="font-size: 18pt" value="Search"> 
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
<form action="hsearch.cgi" method="get">
<input style="font-size: 17pt" size="40" name="q" value="$query"><input type=submit style="font-size: 18pt" value=" Harvix Search"> 
</div>
</form>
</center>
</body>

EOX
;
}



#!/usr/bin/perl

use strict;

use Data::Dumper;
use WebService::Blekko;

my %escapes;
setup_escapes();

print "Content-type: text/html\n\n";



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


printsay ( " HELP NOT AVALIBLE ");

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
	#print "<div class=\"fb-like\" data-href=\"$r->url\" data-send=\"false\" data-width=\"450\" data-show-faces=\"false\"></div>\n";
	print "<p>\n";
}

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

}

sub print_footer
{

}


sub printsay
{
    my ( $line ) = @_;

    print $line, "\n";
    `say "$line"`;
}

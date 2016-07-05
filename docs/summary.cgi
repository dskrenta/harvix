#!/usr/bin/perl

#       Harvix Summarization version 1.O
#       
#       Coppyright (C) 2013 Harvix Search
#       Designed and Built by David Skrenta CEO, the Harvix Team 
#       All Contents of File and Related Files Protected by Harvix

use strict;
use URI::Fetch;
use JSON;
use Encode;
use Data::Dumper;

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

my $query = parse_query();
my $url = parse_url();

#JSON 
my $json_page = URI::Fetch->fetch("http://api.diffbot.com/v2/article?token=5db92311c3bd3c1a34bc9f2e1855f419&url=$url");
my $json_text = $json_page->content();
my $json = decode_json( $json_text );

if ( ! defined $json )
{
    print "no results\n";
    exit(0);
}


#START
print_header();

#foreach my $tag ( @{ $json->{tags} } )
#{
	#my $category = $tag->{name};
	#print $category;
	print Dumper($json), "\n";

#}
print_footer();
#END

#SUBS

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
	#$query =~ s/\+/ /g;
	$query =~ s/[\[\]\(\)\.\?]/ /g;
	$query =~ s/^\s*//;
	$query =~ s/\s*$//;
	$query =~ s/\s+/ /g;
	
	return $query;
}


sub parse_url
{
        my $url = $ENV{QUERY_STRING} || shift || 1;

        $url =~ s/url=//;
        $url = urldecode($url);

        return $url;
}


sub print_header
{
	my ( $query ) = @_;

	$query =~ s/[<>\&]//g;

print <<EOF



<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>$query | Harvix</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="">
    <meta name="author" content="">

    <!-- Le styles -->
<link href="bootstrap.css" rel="stylesheet">

    <style type="text/css">
      
a:link {text-decoration:none;}      /* unvisited link */
a:visited {text-decoration:none;}  /* visited link */
a:hover {text-decoration:none;}  /* mouse over link */
a:active {text-decoration:none;}  /* selected link */

	body {
	background-color:#eeeeee;;
      }
      .sidebar-nav {
        padding: 9px 0;
      }

	div.hero-unit{overflow:hidden; min-height: 330px;}

    </style>

   <!-- Fav and touch icons -->
    <link rel="apple-touch-icon-precomposed" sizes="144x144" href="http://www.harvix.com/images/harvixshort2.jpg">
    <link rel="apple-touch-icon-precomposed" sizes="114x114" href="http://www.harvix.com/images/harvixshort2.jpg">
      <link rel="apple-touch-icon-precomposed" sizes="72x72" href="http://www.harvix.com/images/harvixshort2.jpg">
                    <link rel="apple-touch-icon-precomposed" href="http://www.harvix.com/images/harvixshort2.jpg">
                                   <link rel="shortcut icon" href="http://www.harvix.com/images/harvixshort2.jpg">
	</head>

  <body>



EOF
;
}

sub print_footer
{
print <<EOX




  </body>
</html>

EOX
;
}


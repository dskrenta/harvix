#!/usr/bin/perl

use strict;
use URI::Fetch;
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

my $query = parse_query();

my $url = parse_url();

print_header($url);

#START OF SEARCH 	

my $btw = 1;

print "<div id=\"upper\"><span class=\"label label-info\"><h5>Facts:</h5></span></div><hr></hr>";
print"<div id=\"scrollable\"><div id=\"items\">";

	my $pokemon = $url;
	print STDERR "pokemon='$pokemon'\n";

   my $pokemon_page = URI::Fetch->fetch($pokemon);

my $pagenew = $pokemon_page->content();


# dehtml

$pagenew =~ s/<[^>]*>//gs;
$pagenew =~ s/\&lt;/</gs;
$pagenew =~ s/\&gt;/>/gs;
$pagenew =~ s/\&lt/</gs;
$pagenew =~ s/\&gt/>/gs;
$pagenew =~ s/\&(#\d+|[a-z0-9]+);/ /gsi;
$pagenew =~ s/\s+/ /gs;

my @sentences = ( $pagenew =~ /([A-Z][^{}\(\)]*?[a-z]\.\s)/gs);

foreach my $s ( @sentences )
{
     next if $s !~ /(\sis\s|\swas\s|\swrote\s|\she\s|\sshe\s|\showever\s|\sdevelop\s|\slasted\s|\sas\s|\sa\s|\swhen\s|\sbegan\s|\sconventional\s|\series\s)/;
     next if length($s) > 200;
     next if length($s) < 50;
     next if $s =~ /(\sWikipedia\s|\sI\s|\s"\s|\sthis\s|\sRating\s|\sWhat\s|\sEveryone\s|\sHmm\s|\sboring\s|\syou\s|\sThis\s|\sour\s|\sApple Store\s|\sPalo Alto Networks\s|\sSurveyMonkey\s|Paused|\^|your|FREE|I|my)/;
     #next if $pokemon =~ "http://en.wikipedia.org/wiki/";
     next if $pokemon =~ "http://makeandtakes.com/";

     print"<div class=\"itemfacts\">";
     print"<div class=\"hero-unit-spec\">";
     print"<blockquote>";    
 
     print "<b>$btw.</b> $s <small><cite title=\"Source Title\">$pokemon</cite></small>";

     print"<form action=\"flag.php\" method=\"post\" target=\"_blank\"> <input type=\"hidden\" name=\"url\" value=\"$pokemon\"> <input type=\"hidden\" name=\"sentence\" value=\"$s\"> <input type=\"hidden\" name=\"query\" value=\"$query\"> <button type=\"submit\" class=\"btn btn-small btn btn-info\">Flag Fact</button> </form>";

     print"</blockquote></div></div>";
     $btw++;
}


if ( ! @sentences )
{
print"No Facts";
}



print"</div></div>";

#END OF SEARCH


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

        $url =~ s/u=//;
        $url = urldecode($url);

        return $url;
}

sub print_pod
{
    my ( $pod ) = @_;

    return if !defined $pod->{title};
    return if !defined $pod->{subpods};

print"<h3>";
    print $pod->{title}, ":\n<p>";
print"</h3>";

    foreach my $subpod ( @{ $pod->{subpods} } )
    {
        next if !defined $subpod->{plaintext};
        if ( defined $subpod->{img} )
        {
            print "    ", $subpod->{img}, "<hr></hr>\n<p>";
        }

        #my $s = $subpod->{plaintext};
        #$s =~ s/\n/\n    /gs;
        #print "    ", $s, "\n";
    }
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
	background-color:white;
      }

	      #scrollable {
       overflow: auto;
       width:100%;
       height:250px; 
    }


   #scrollable-img {
       overflow: auto;
       width:100%;
       height:250px; 
    }


   #items {
     width: 100000000000px; /* itemWidth x itemCount */
    }

  .item{
     float:left;      
  }

  .item2{
        width:400px;
        height:200px;
     float:left;      
  }

 .item3{
        width:350px;
        height:220px;
     float:left;      
  }

.itemfacts{
        width:400px;
        height:200px;
     float:left;      
  }

 .itemwiki{
     width:100%;
     float:left;      
  }


.hero-unit-spec {
  padding: 10px;
  margin-bottom: 30px;
  height:200px;
  font-size: 14px;
  font-weight: 200;
  line-height: 30px;
  color: inherit;
  background-color: white;
  -webkit-border-radius: 6px;
     -moz-border-radius: 6px;
          border-radius: 6px;
        overflow:hidden;
}

#count{
     float:right;      
}

#upper{
text-transform:uppercase;
}

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


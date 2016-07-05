#!/usr/bin/perl

use strict;

use Data::Dumper;
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

print_header();

#START OF SEARCH 	

print"
<div class=\"row-fluid\">
<div class=\"span12\">
";

	my $pokemon = "$url";
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

print"<div class=\"hero-unit\">";

print"  <h2>EXPAND BETA: <small>$url</small></h2><hr></hr> ";

my $btw = 1;

print"<p>";
foreach my $s ( @sentences )
{
     #next if $s !~ /(\sis\s|\swas\s|\swrote\s|\she\s)/;
     next if $s =~ /(your|Your|Invite|Copyright|you're)/;

	if ($btw == 20) {
     	print "$btw $s </p><p> ";
     	}
	
	elsif ($btw == 40) {
        print "$btw $s </p><p> ";
        }

	elsif ($btw == 60) {
        print "$btw $s </p><p> ";
        }

	elsif ($btw == 80) {
        print "$btw $s </p><p> ";
        }

	elsif ($btw == 100) {
        print "$btw $s </p><p> ";
        }

	elsif ($btw == 120) {
        print "$btw $s </p><p> ";
        }

	elsif ($btw == 140) {
        print "$btw $s </p><p> ";
        }

	elsif ($btw == 160) {
        print "$btw $s </p><p> ";
        }

	else
	{
	print"$s";
	}	


     $btw ++;
}
print"<hr></hr><p>Computed by Harvix</p>";


if ( ! @sentences )
{
print"$pokemon";
print "<pre>", Dumper($pagenew),"</pre>" ;
}



print"</div>";
print"</div>";




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


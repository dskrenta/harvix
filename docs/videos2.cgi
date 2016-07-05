#!/usr/bin/perl

use strict;
use WebService::GData::YouTube;
use Encode;

print "Content-type: text/html\n\n";

my $query = parse_query();

my %escapes;
setup_escapes();

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


print_header($query);

#START OF SEARCH 	

print "<div id=\"count\"><span class=\"label\"><h5>10 Videos:</h5></span></div> <div id=\"upper\"><span class=\"label label-important\"><h5>Videos:</h5></span></div><hr></hr>";

print"<div id=\"scrollable-img\"><div id=\"items\">";

my $yt = new WebService::GData::YouTube();
$yt->query()->q($query)->limit(10,0);
my $videos = $yt->search_video();

foreach my $video (@$videos) {
my $thumb = $video->thumbnails->[0];
$thumb = $video->thumbnails->[0] if !defined $thumb;
my $url = $thumb->url;
my $title = $video->title;
my $des = $video->description;

print"
<div class=\"item2\"><div class=\"hero-unit-spec\">
<table cellpadding=\"10\"><tr><td valign=\"top\">
<a href=\"http://www.youtube.com/watch?v=", $video->video_id, "\"><img src=\"$url\" width=\"200px\" alt=\"\"></a>
</td><td valign=\"top\">
<a style=\"color:#333333\" target=\"_blank\" href=\"http://www.youtube.com/watch?v=", $video->video_id, "\"><h3>$title</h3></a>
<p>$des</p>
</td></tr></table>
</div></div>
";

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
       height:300px; 
    }


   #scrollable-img {
       overflow: auto;
       width:100%;
       height:300px; 
    }


   #items {
     width: 100000px; /* itemWidth x itemCount */
    }

  .item{
     float:left;      
  }

  .item2{
        width:600px;
        height:280px;
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
  height:280px;
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


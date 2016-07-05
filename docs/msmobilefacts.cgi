#!/usr/bin/perl

use strict;

use Data::Dumper;
use WebService::Blekko;
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
    
my $querynew = $query." site:en.wikipedia.org";
print STDERR "querynew=$querynew\n";


my $blekkonew = WebService::Blekko->new( auth => 'c31c6fd0', );

my $resnew = $blekkonew->query( $querynew );


print_header($query);

my @resultsnew;

while ( my $rnew = $resnew->next ) {
        push @resultsnew, {
                        title => $rnew->title,
                        snippet => $rnew->snippet,
                        url => $rnew->url,
                };
}


#START OF SEARCH 	


print"  <div class=\"row-fluid\">
        <div class=\"span12\">
        ";



my $countnew = 0;

foreach my $resnew ( @resultsnew )
{
        if ($countnew == 0)
        {
        my $pokemon = $resnew->{url};
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

print"  <h2>Facts: <small>$query</small></h2><hr></hr> ";

my $btw = 1;

foreach my $s ( @sentences )
{
     next if $s !~ /(\sis\s|\swas\s|\swrote\s|\she\s)/;
     next if length($s) > 200;
     next if length($s) < 50;
     next if $s =~ /(Wikipedia)/;

     print "<b>$btw.</b> $s<hr></hr><p>";
     $btw++;
}
print"<p>Computed by Harvix</p>";


if ( ! @sentences )
{
print"$pokemon";
print "<pre>", Dumper($pagenew),"</pre>" ;
}

   }

$countnew ++;

}
    
print"
</div>
</div>
";


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
        padding-top: 20px;
	padding-top: 20px;
	background-color:#303030;
      }
      .sidebar-nav {
        padding: 9px 0;
      }

	div.hero-unit{overflow:hidden; min-height: 330px;}

	/*
 * Metro UI CSS
 * Copyright 2012 Sergey Pimenov
 * Licensed under the MIT Lilcense
 *
 * Tiles.less
 *
 */
.tile-group {
  margin: 0;
  margin-right: 80px;
  float: left;
  width: auto;
  height: auto;
  min-height: 1px;
  width: 802px;
}
.tile {
  display: block;
  float: left;
  background-color: #525252;
  width: 150px;
  height: 150px;
  cursor: pointer;
  box-shadow: inset 0px 0px 1px #FFFFCC;
  text-decoration: none;
  color: #ffffff;
  overflow: hidden;
  position: relative;
  font-family: 'Segoe UI Semilight', 'Open Sans', Verdana, Arial, Helvetica, sans-serif;
  font-weight: 300;
  font-size: 11pt;
  letter-spacing: 0.02em;
  line-height: 20px;
  margin: 0 10px 10px 0;
  overflow: hidden;
}
.tile * {
  color: #ffffff;
}
.tile .tile-content {
  width: 100%;
  height: 100%;
  padding: 0;
  padding-bottom: 30px;
  vertical-align: top;
  padding: 10px 15px;
  overflow: hidden;
  text-overflow: ellipsis;
  position: relative;
  font-family: 'Segoe UI', 'Open Sans', Verdana, Arial, Helvetica, sans-serif;
  font-weight: 400;
  font-size: 9pt;
  color: #000000;
  color: #ffffff;
  line-height: 16px;
}
.tile .tile-content:hover {
  color: rgba(0, 0, 0, 0.8);
}
.tile .tile-content:active {
  color: rgba(0, 0, 0, 0.4);
}
.tile .tile-content:hover {
  color: #ffffff;
}
.tile .tile-content h1,
.tile .tile-content h2,
.tile .tile-content h3,
.tile .tile-content h4,
.tile .tile-content h5,
.tile .tile-content h6,
.tile .tile-content p {
  padding: 0;
  margin: 0;
  line-height: 24px;
}
.tile .tile-content h1:hover,
.tile .tile-content h2:hover,
.tile .tile-content h3:hover,
.tile .tile-content h4:hover,
.tile .tile-content h5:hover,
.tile .tile-content h6:hover,
.tile .tile-content p:hover {
  color: #ffffff;
}
.tile .tile-content p {
  font-family: 'Segoe UI', 'Open Sans', Verdana, Arial, Helvetica, sans-serif;
  font-weight: 400;
  font-size: 9pt;
  color: #000000;
  color: #ffffff;
  line-height: 16px;
  overflow: hidden;
  text-overflow: ellipsis;
}
.tile .tile-content p:hover {
  color: rgba(0, 0, 0, 0.8);
}
.tile .tile-content p:active {
  color: rgba(0, 0, 0, 0.4);
}
.tile .tile-content p:hover {
  color: #ffffff;
}
.tile.icon  > .tile-content {
  padding: 0;
}
.tile.icon  > .tile-content  > img {
  position: absolute;
  width: 64px;
  height: 64px;
  top: 50%;
  left: 50%;
  margin-left: -32px;
  margin-top: -32px;
}
.tile.image  > .tile-content,
.tile.image-slider  > .tile-content {
  padding: 0;
}
.tile.image  > .tile-content  > img,
.tile.image-slider  > .tile-content  > img {
  width: 100%;
  height: auto;
  min-height: 100%;
  max-width: 100%;
}
.tile.image-set  > .tile-content {
  margin: 0;
  padding: 0;
  width: 25% !important;
  height: 50%;
  float: left;
  border: 1px #1e1e1e solid;
}
.tile.image-set  > .tile-content  > img {
  min-width: 100%;
  width: 100%;
  height: auto;
  min-height: 100%;
}
.tile.image-set .tile-content:first-child {
  width: 50% !important;
  float: left;
  height: 100%;
}
.tile.double {
  width: 100%;
}
.tile.triple {
  width: 470px;
}
.tile.quadro {
  width: 630px;
}
.tile.double-vertical {
  height: 350px;
}
.tile.triple-vertical {
  height: 470px;
}
.tile.quadro-vertical {
  height: 630px;
}
.tile .brand,
.tile .tile-status {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  min-height: 30px;
  background-color: transparent;
  *zoom: 1;
}
.tile .brand:before,
.tile .tile-status:before,
.tile .brand:after,
.tile .tile-status:after {
  display: table;
  content: "";
}
.tile .brand:after,
.tile .tile-status:after {
  clear: both;
}
.tile .brand  > .badge,
.tile .tile-status  > .badge {
  position: absolute;
  bottom: 0;
  right: 0;
  right: 5px;
  margin-bottom: 0;
  color: #ffffff;
  width: 34px;
  height: 28px;
  text-align: center;
  font-family: 'Segoe UI Semibold', 'Open Sans', Verdana, Arial, Helvetica, sans-serif;
  font-weight: 600;
  font-size: 11pt;
  letter-spacing: 0.01em;
  line-height: 14pt;
  padding-top: 3px;
}
.tile .brand  > .badge.activity,
.tile .tile-status  > .badge.activity {
  background: #2d89ef url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAGMSURBVDhPvZMtTwNBEIbv2mtScaICcQJRgSgJCQIEhqSiAlEHAlFRwU/ov0AgUEgUsrIkiJIgMOAQJFSQQAIJJBWIu95Hj2eGvXIpB3W8yWTn452Z3dld25pDmqZuFEWdcrm8jr6JK7Bt+wb9Ft85+vsXswBxHHdIfmFNi4TYG7InXAp6ss52kCTJIc6e6KzSVbrdYzrYDaSFXZU4uEQ8x3FW1ZpMJge5Tn3IdQ3kID5iw4zHTqIsUEP3TWCA7WhgDjRZg/eUFRCR3Fl3KYJjyfALIUU46jHcsSlQl8FdmQJnhrcQJFbJ6QZB0LDDMNyS4XBFo1Kp9Gw4/wi247GLHmvNuBaC47Y5gtzIQB1mBmMGdDSdTpfV+QdM8vfcsqkap6ClgQIQa+a4bXViPGRO5ILjuBqYAwk7yIfhXcNz9CljDFkkST6P4JGjnHA7d+gBxAY3tIve1Khljbi1beKvakHQp0uhfTrMjvOL9H3fX9FE8OM7yxAhdem4QWHZkSufSoTYaaVSkY9kYFmfXgyTciI3uacAAAAASUVORK5CYII%3D) 50% no-repeat;
}
.tile .brand  > .badge.alert,
.tile .tile-status  > .badge.alert {
  background: #2d89ef url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAFeSURBVDhPpZMtT8RAEIbb7YoTJ04gkQgQuBNIEpB4LD8AwQ9AkCCQhGAvQSAuKHCIE0gEP+DEISAhQYK4pE0/eWa65a7lSvh4k8nsvDv77sxs67UhSZLNNE0LZ3uO/gLj/J+hAkVRWI1+geqMCuR5fkKZoyiKViX+DuQu094wy7KhEmEYrkAk0qt4Nk5R77GszQCuE8fxIXxY8ZJjgiBY8n3/UcTwlsQDNifGmF29AcBtITyGOyan47gXXFfW2g/q+yi+VeptJhVgR1KRHp4HZI+bzknQlhYcvpQZuHRF8xmnCDyLL8MZEI9o4YkW3h1VB+o73DJp3to08l7xsw9Lng5i1EiSSV/Pcbdwzfk8MLcNqjIyye1STnHD5joln7lYcGWtXaP8gYsFfeJyHvR9waExt3wKsV74L3Brn/geu3OUDqiL1T7nNoEK8mLi9RUoZYqlsv4pqtf459/oeR8seozS7mDHCwAAAABJRU5ErkJggg%3D%3D) 50% no-repeat;
}
.tile .brand  > .badge.available,
.tile .tile-status  > .badge.available {
  background: #2d89ef url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAACXBIWXMAAA7DAAAOwwHHb6hkAAAAIGNIUk0AAHolAACAgwAA+f8AAIDoAABSCAABFVgAADqXAAAXb9daH5AAAAKvSURBVHjahJA/bJR1HMY/31977x33r2LuClc1LYM9TSAUr5gqtkVJjAkSFxYHE3VgaWRw0cUwOagxMZLApoXFBIwuHVSoQYkVMBXUpqSkMW9jaS25plh7/3rv+3scTIwixs/8PHn+2Bk/SVtN2mqxacYOKw13KfNiXtlneihmDONXqs0VVs/VXP1UqJvnc8qBeZoWYWf9JHXVqWkj2EX55G76X86R4W40aDHNzMdzLBwJLLEWm6fTI+o0knvZ+dkgO/cDfGczTNpl5gjxePrpY0SPMKwKT1A5nCe7Y4ofDgQEv/Ghn2AqunZabUmR9Fb8gQoaUVIVFTSiokaV0qDu0T694Y+rGbWktnQ5+nHiuP+IjrFjR4cqevj9wBK8beO87t6jiyzbKJAiIEWSreQxjAm7QGyeAwzRzb39i/7WFbdV2bGs0nxvs7zjxtlOgRwZPP6v7R5PmhQPUOKEneFLd4UECfqs51WXU/opDL6wb/mdDfJkEfrXgUKk2UKbiM/5BoD76d7reujOANwgJH9H8p14PDnSzBGySZsSReecDIAIDxj/jxH/LcQtW7UJ0E8f69RwuP+0Ohwb1CnTS0CCW6zK3Wb9a4AnNcgWktRoYHdpYhgtWvypfRSARVv5yVXd2smGWuzTHo7qeRZZpk7zH00cRos2ITd5yT/HQY0gPKGW3u0YPvZ06HB77tO2hx5jN5HFTNk11lgHRIs2VW5Tp8kRf5g3eYUUSa5y/eKsfn7NTvlPaCjqelwDF3bx4ADAeXeJc1xijpCYmDJ9jKrCIe0H4IaF81/56VGDJTvtPwV1IFmhTO/4AOWDSQIAWmwiRIokADEx08xeXGD5hUjxQp0GnQCdOAKS1RnNP7tO7VDOMmO9bB8qUQRghVVCW7raUOPEvH45W7IidRoA/DEAmmk0pL+n6f4AAAAASUVORK5CYII%3D) 50% no-repeat;
}
.tile .brand  > .badge.3navailable,
.tile .tile-status  > .badge.unavailable {
  background: #2d89ef url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAACXBIWXMAAA7DAAAOwwHHb6hkAAAAIGNIUk0AAHolAACAgwAA+f8AAIDoAABSCAABFVgAADqXAAAXb9daH5AAAAKASURBVHjalJK9axxXFMV/772ZzOysVqvRDgtaSSwpJYFwY3ATEpIm5KNLawgp3Ljz/5E2bu20CYQUBoMNNnaRMkUKqYiQtIgdCQ0TaVc7M29n3nspzC7GMYYcuMWFe7jnHI4YjUY453DOYYyh0+l8opT63vO8L8MwbAshqKqq0lo/c849rqrquXMOIcSbGY1GWGsxxny0urr6MI7jH5RSAFhrAZBSLvc8z3+dTqf3lFL/SCnxAIwxwdra2tP19fXPAC4vL8myjKIoAIiiiF6vR7/fJ0mS75RSH19dXX0hpbwWx8fHrKys/JwkyV1rLYeHh5yenuKc420lzjm2trbY3d3F8zzyPH8ynU6/ERcXF3fiOP7D930ODg44OjoiDMOl7AWstZRlyXA4ZH9/H2MM4/H4K+l53n3f98myjJOTE4Ig+A95kUMURZydnXF+fo5SiiiKHkjf9z9f+AaWst+HRfKL2yiKbssgCNrOOWaz2Xs/vwulFLPZjLquCcPwDcM5x//B2/dyPp9XC3/WWoQQHyQbY2i32/i+T1VVTtZ1/QogSZJlGz/02VpLkiQAlGX5l2ya5mHTNPT7fba3tynLctnAd8llWTIYDNjY2MBaS1EUP0qt9YvJZPI7wM7ODsPhEK01WmuapqFpGrTWVFXFYDBgb28PIQTX19ev67r+TYzHY7TW3W63+zKO41sAaZqSZRk3NzcAtNtter0em5ubAEwmk7/zPP9USjkWaZoyn89xziWdTudRt9v9etGFuq4B8H1/aSXP89dFUdx1zp065xBpmlLXNUIIjDG0Wq1vPc+7H4bhnVarhRCCsiwpiuJPY8xPRVH8EgQBxhistfw7ABpxTL93U9x/AAAAAElFTkSuQmCC) 50% no-repeat;
}
.tile .brand  > .badge.away,
.tile .tile-status  > .badge.away {
  background: #2d89ef url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAACXBIWXMAAA7DAAAOwwHHb6hkAAAAIGNIUk0AAHolAACAgwAA+f8AAIDoAABSCAABFVgAADqXAAAXb9daH5AAAAJ2SURBVHjajJI7iFVnFIW//d9zz52ZO2fG14gzJBgbp5JYKPh+NqKxsxWMRZoBCxu1sAuBKFaClj5KDUQhRXybCIqICjqNYjFDhtExN45e7/uc8y+L/yJGp3A1+2fDWv/ea23zlQvIp0gpRgfrWbZRNrhP0cAOopEyGGSvWmQz15zq59SeuC5LsAis0MJ85SLKG8jXY3pXnKb8/X6iBAB8KLhuzZtQf/gbrWc/WTGetSgnAg9qlCiv/pNk1RYAqz3A6jeg/SyoxMtReRNKNsLAhj24gWW0726H+B3+9Rmyd3fPp5KyXMpf/SqNL5KelEIdH5Ke9Ejj8+SnjyrLWkolZbX7f/jZk5h/e3WN7197j0I/NnMMN3MYoiXgBv6/g+rQmUJDR/Ajv4BP0eylnU5u/pgK/Vj9Ee6/411y8gm5a4b1Qfwt9uYUrnoTXBGLvzvoFCXbDLDaVcjfd38WX0JBRCnUroRW/M1qRzRSxgPt55+NPRc8FJJgbtaB4rBz+phRxtcj//hylr5s4YDScvDVT0KfCw7yGpRGIYohfS2H3v4NoL6tYL3BbWwOsoHawY3y1tDJpp46p8pp5U2UrEcLD0BnCtT4bBIXyJ0J/Pwf0eAu8ELtiROO5uQtazy9LMAvPoKGDoU00n/CSr4K2RTkFfyCMRj+OWg2Ht9RNv27+X/PId8cVN+62/SvWAngqtehdq17yjmURlHfZjRvdxi98fyFr/21GWfT5ivnkQehRfSOnqV35S4KpW4w7ZB/1NNNMYf6wzukk3ulbBI1iIJkBBZX1Bn/gby621wyRrx0DcXhQGzPYOnEY/nmKbVeXLTicNcn+DAArZ4503S5ZjkAAAAASUVORK5CYII%3D) 50% no-repeat;
}
.tile .brand  > .badge.busy,
.tile .tile-status  > .badge.busy {
  background: #2d89ef url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAACXBIWXMAAA7DAAAOwwHHb6hkAAAAIGNIUk0AAHolAACAgwAA+f8AAIDoAABSCAABFVgAADqXAAAXb9daH5AAAAKNSURBVHjajJI9a1RBGIWfGeLdmPXuKkR0Q0RTmFsFUxgQNcaPRonpbAW1sAlY2IhFfoCIVSDaaVImFhYWmkTxAwJBVgttNqTYQFAjAWPi7t3svXeOxeC3hQdeZpiZ887DmTFuchIlCUoSTLOJ6erqV7F4QYXCaTo68hgDHz82WFmZsbXauKrVWYUhBjCNBsZNTaF6HdVqAT09tzlw4BJhyD8Vx1Au36dSuWyC4LPJMlpwDur1HH19jzh48DiAefUK8+QJVCrgHHR3o2PHUH8/HD16jkKhi7m5UwTBF9zdu6RzcxOJpFRSduOG1N4u5XJ+3LlTam2Vtm+XGxlR2mgokZTOzz90o6PgpqcPpRsbP83GSKWSFEXS/v2+okjq7JRA7vp1pZLSZlPJ5OQZqx07hrVtG+b1a+zNm7B7N4ShR/8u56CtDfbswYyNYZ8+hS1bMPv2XbUKw5MGMNPTsLEBhQJIfwco+SZJAo8f+7XOzj5LR0cegIUFb/715j/lnKerVKDZhFLJWlnrN9OU/1aW/Zha8+FDA4Dublhfh+8N/yVr4etXiCIIAvj0SZa1tRcAOnECtm6FWg2M+dtsDGxu8uMsYJaX31q7unpbcYyOHEFXrsDyMtTrv5NY683VKu7iRTQ4CBKqVm/h7twhnZ9/kEhK41ju2jWpWJTa2qRdu3zl81I+r2x4WNnamv8H5fKLZHQU48bHURwXdfjwM3p6egHs7CzMzPi0swyiCA0MoKEhj76wsOiePx/AmPfGTUwgQFI7UXSP3t5BcjmPvrnp37+19Wf65fJLlpbOK02XqNdpAaClBYJgVe/enWV9fciE4TB79x6iVPLGlRVMtfpGcTymxcUpUyr5nIBvAwDWIWcndiwtQAAAAABJRU5ErkJggg%3D%3D) 50% no-repeat;
}
.tile .brand  > .badge.newMessage,
.tile .tile-status  > .badge.newMessage {
  background: #2d89ef url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAC/SURBVDhP1ZE9DgIhFIQhobDYg1haWniMbSw9j0exsfMAeg9L7Sy2kPATnCFI2LgYtjJOMjx4vPkoED+X5OK934cQ+thpFOYvSqmdMMascVDOuQMcGn1GptNaL4W1dgBkMwOSw8jeBJszIKMwexFAN0A+wnQG0Lh4wv0EJIb5AO4fRX8MoDFAlZAyPJSztOSSfiYLAYeyxTcdURcIrqSUJ7iLA4UmAdQbgnqvhakqgEoQXQtTXwEtIuCa9n8pIV67VJf6AmhGmgAAAABJRU5ErkJggg%3D%3D) 50% no-repeat;
}
.tile .brand  > .badge.paused,
.tile .tile-status  > .badge.paused {
  background: #2d89ef url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAArSURBVDhPY/j9+7fDnz9//mPBCQxQgE8NE1QN2WDUgFEDQGDUgIE3gIEBAArtNKc4HT7sAAAAAElFTkSuQmCC) 50% no-repeat;
}
.tile .brand  > .badge.playing,
.tile .tile-status  > .badge.playing {
  background: #2d89ef url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAEXSURBVDhPY4CBnz9/pvz+/dsFyiUaMEFpBiYmJhkgtf3v37/t////Z4GIEgZwA0CAkZGRBai5AmjIYSCtABXGC1AMQAIWf/78OQ/EEVA+ToDLAJBrBIDUcqBrZgNdwwMRxQQ4DYABoOYUoCGngYFsABVCAQQNgAINYCAf//XrVwGUDwfEGgDyEgfQkH5guGwGukoEKky8AUhA5sePH6DwAQOSDAC6YgIzM7MpJyfnHagQcQYAnfwGiD2BmguBhvyBCoMBMQbsYWFh0WVlZd0B5aMAnAYAbfzz79+/SqBmV6CtL6DCGACXAQ+ABliysbF1QPk4AYYBQI0rgH7VBWo+AxXCC+AGADV+AVKJQL9GAp0MYhMBGBgA8v5j1f90TA8AAAAASUVORK5CYII%3D) 50% no-repeat;
}
.tile .brand  > .badge.error,
.tile .tile-status  > .badge.error {
  background: #2d89ef url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAFiSURBVDhPjVM7TsNQELRjy8ISBQeIREtBEYnQUXCINFTkCCBxgNwAJI5AaejSpaCAEqRINBTcIQ1SbD9/mHmfZP3iSIw0ytt9O7O7thMGHpqmGVZVNQnD8AwcMde27RL8rOt6nqbpjy7sA4RTpdQKv20fcbcuy/IOZrGVbIHLpz7RHr52TJCYukuMeU+6WDBjdxej4UyLubMbm0KdBDyTzHWEyY01UEVRnA4Q8IEdaZVAFEW3yD/g+IzzFc6VuTFAHAPXO7vLKQi5q+suuOD+X15yx4ToEXON1QB3B6ZkC3Qd+q8Kaxzbo0TMCTLPefPAfPS8nTeOtnk1YEfMsf11pIm+y/P8BLusmaCZrevsLE1QO3F51FzopJyCQil2pAnFoLLxI7X6z8SxkVjgeMn4H/jGQz3Ht/BrY2MC85nrsI/sjNpDKzMTSODzHPELQ9EY1H9ndFqCHxC/JEnyrgs1guAPTvwreuY0IiIAAAAASUVORK5CYII%3D) 50% no-repeat;
}
.tile .brand  > .badge.attention,
.tile .tile-status  > .badge.attention {
  background: #2d89ef url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAEbSURBVDhPtZI9bsJAEIVZ7ANQ5gApEomChjoNBUUOkSJFivSUQE3JEThCCo4BkotcIVKKNEi2vP7hveVZrMFgKPJJo915szOzf51/Jc/zhbV2Jfc+kiR5QrLNsqzEMJJ8O0hcM1kWlWUZKtQOOo69ZGdpmn4ofB12QsI3k1BoRtP8F7Gell0GnT6rrpJ4HOfzUiU1ww7o9HepAGI2juNHyeegw7Ja3FRA9iW5jv9slSl0WqD2rEYjF7Hy68E7gCPNORpjpk44sg2CYAg969JTxVoywYIXmlyfAS77jRPDZ8PZN5j3KfiEYeh2yG07wQN5P4g/d9H9Hf5ZMkHM/QO5NbCzh6IoJgbVI/iNBdrALnY8An9X+w9rpLPbA/sADga+JgSiAAAAAElFTkSuQmCC) 50% no-repeat;
}
.tile .brand  > .name,
.tile .tile-status  > .name {
  position: absolute;
  bottom: 0;
  left: 0;
  margin-bottom: 5px;
  margin-left: 15px;
  font-family: 'Segoe UI', 'Open Sans', Verdana, Arial, Helvetica, sans-serif;
  font-weight: 400;
  font-size: 9pt;
  color: #ffffff;
}
.tile .brand  > .name:hover,
.tile .tile-status  > .name:hover {
  color: #ffffff;
}
.tile .brand  > .name  > [class*=icon-],
.tile .tile-status  > .name  > [class*=icon-] {
  font-size: 24px;
}
.tile .brand  > .icon,
.tile .tile-status  > .icon {
  margin: 5px 15px;
  width: 32px;
  height: 32px;
}
.tile .brand  > .icon  > [class*=icon-],
.tile .tile-status  > .icon  > [class*=icon-] {
  font-size: 32px;
}
.tile .brand  > .icon  > img,
.tile .tile-status  > .icon  > img {
  width: 100%;
  height: 100%;
}
.tile .brand  > .text,
.tile .tile-status  > .text {
  position: absolute;
  left: 60px;
  top: 5px;
  right: 50px;
  font-family: 'Segoe UI', 'Open Sans', Verdana, Arial, Helvetica, sans-serif;
  font-weight: 400;
  font-size: 9pt;
  color: #000000;
  color: #ffffff;
  line-height: 14px;
}
.tile .brand  > .text:hover,
.tile .tile-status  > .text:hover {
  color: rgba(0, 0, 0, 0.8);
}
.tile .brand  > .text:active,
.tile .tile-status  > .text:active {
  color: rgba(0, 0, 0, 0.4);
}
.tile .brand  > .text:hover,
.tile .tile-status  > .text:hover {
  color: #ffffff;
}
.tile:hover {
  outline: 3px #3a3a3a solid;
}


/*
 * Metro UI CSS
 * Copyright 2012 Sergey Pimenov
 * Licensed under the MIT Lilcense
 *
 * Slider.less
 *
 */
.slider {
  height: 12px;
  width: auto;
  position: relative;
  background-color: #c6c6c6;
  margin-bottom: 10px;
}
.slider .marker {
  height: 12px;
  width: 12px;
  cursor: pointer;
  position: absolute;
  top: 0;
  left: 0;
  background-color: #000000;
  z-index: 3;
}
.slider .complete {
  height: 100%;
  width: auto;
  background-color: #00828b;
  z-index: 2;
}
.slider.vertical {
  height: auto;
  width: 12px;
}
.slider.vertical .complete {
  position: absolute;
  height: auto;
  width: 12px;
  bottom: 0;
}
.slider:hover .complete {
  background-color: #219297;
}
.slider:active .complete,
.slider:active + .marker:active .complete {
  background-color: #25bbc4;

}


div.spacer100{height:35px; }

    </style>

    <!-- HTML5 shim, for IE6-8 support of HTML5 elements -->
    <!--[if lt IE 9]>
      <script src="http://html5shim.googlecode.com/svn/trunk/html5.js"></script>
    <![endif]-->

   <!-- Fav and touch icons -->
    <link rel="apple-touch-icon-precomposed" sizes="144x144" href="http://www.harvix.com/images/harvixshort2.jpg">
    <link rel="apple-touch-icon-precomposed" sizes="114x114" href="http://www.harvix.com/images/harvixshort2.jpg">
      <link rel="apple-touch-icon-precomposed" sizes="72x72" href="http://www.harvix.com/images/harvixshort2.jpg">
                    <link rel="apple-touch-icon-precomposed" href="http://www.harvix.com/images/harvixshort2.jpg">
                                   <link rel="shortcut icon" href="http://www.harvix.com/images/harvixshort2.jpg">
	</head>

  <body>


<div class="spacer100"></div>

<div class="navbar navbar-inverse navbar-fixed-top">
      <div class="navbar-inner">
        <div class="container-fluid">
          <a class="brand" href="index.html"><b><span style="color:white">Har<span style="color:red">vix</span></span></b></a>
            <ul class="nav">
              <li><form class="navbar-search pull-left">
  <input type="text" style="width:140px;" action="http://harvix.com/msmobile.cgi" value="$query" onsubmit="submitted('h'); return false" name="q"  class="search-query">
</li></ul>
</form>
        </div>
      </div>
    </div>



EOF
;
}

sub print_footer
{
print <<EOX
   

<div class="navbar navbar-inverse navbar-fixed-bottom">
      <div class="navbar-inner">
        <div class="container-fluid">
<ul class="nav">
<li><a href="msmobile.cgi?$query">Web</a></li>
<li><a href="msmobilefacts.cgi?$query">Facts</a></li>
<li><a href="msmobileinfo.cgi?$query">Information</a></li>
<li><a href="msmobileimages.cgi?$query">Images</a></li>
</ul>
        </div>
      </div>
    </div>
 

    <!-- Le javascript
    ================================================== -->
    <!-- Placed at the end of the document so the pages load faster -->
    <script src="http://twitter.github.com/bootstrap/assets/js/jquery.js"></script>
    <script src="http://twitter.github.com/bootstrap/assets/js/bootstrap-transition.js"></script>
    <script src="http://twitter.github.com/bootstrap/assets/js/bootstrap-alert.js"></script>
    <script src="http://twitter.github.com/bootstrap/assets/js/bootstrap-modal.js"></script>
    <script src="http://twitter.github.com/bootstrap/assets/js/bootstrap-dropdown.js"></script>
    <script src="http://twitter.github.com/bootstrap/assets/js/bootstrap-scrollspy.js"></script>
    <script src="http://twitter.github.com/bootstrap/assets/js/bootstrap-tab.js"></script>
    <script src="http://twitter.github.com/bootstrap/assets/js/bootstrap-tooltip.js"></script>
    <script src="http://twitter.github.com/bootstrap/assets/js/bootstrap-popover.js"></script>
    <script src="http://twitter.github.com/bootstrap/assets/js/bootstrap-button.js"></script>
    <script src="http://twitter.github.com/bootstrap/assets/js/bootstrap-collapse.js"></script>
    <script src="http://twitter.github.com/bootstrap/assets/js/bootstrap-carousel.js"></script>
    <script src="http://twitter.github.com/bootstrap/assets/js/bootstrap-typeahead.js"></script>
    
    <script type="text/javascript" src="http://metroui.org.ua/js/modern/tile-slider.js"></script>

  </body>
</html>

EOX
;
}


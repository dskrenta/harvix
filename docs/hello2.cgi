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

my $query = parse_query();

my $blekko = WebService::Blekko->new( auth => 'c31c6fd0', );


my $res = $blekko->query( $query );

#if ( $res->error ) ...

print_header($query);

my @results;

while ( my $r = $res->next ) {
        push @results, {
                        title => $r->title,
                        snippet => $r->snippet,
                        url => $r->url,
                };
}

#START OF SEARCH

print_header();


foreach my $res ( @results )
{

        print "<div class=\"large4\"><b><u><a href=", '"', $res->{url}, '">', $res->{title}, "</a></u></b><br></div>\n";

                print "<span style=\"color:#093;\">";
        print $res->{url}, "<br> </span>\n";

        my $snippet = $res->{snippet};
        if ( length($snippet) > 100 )
        {
                $snippet = substr($snippet, 0, 500);
                $snippet =~ s/\s[^\s]*$//;
                $snippet .= ' ...';
        }
        print $snippet, "<br>\n";

        print "<p></p>\n";

        }



print_footer();

#END OF SEARCH 


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
<html>
<head>
<title>Harvix Search - $query</title>
<link rel="shortcut icon" href="http://www.tinychan.org/img/1328039793912825.png" type="image/x-icon" />
<style type="text/css">
body { font-size: 12px; width:100%; font-family:  Helvetica, sans-serif; font-size: normal; line-height: normal; margin: 0; padding: 0; }
div.h7{width:100%; position: fixed; padding:4px; border:0px solid:black; margin:0px; background-color:black; -moz-box-shadow: 0 0 1em black; -webkit-box-shadow: 0 0 1em black; box-shadow: 0 0 1em black;}
div.large4{font-size:18px;}

#footer{clear:both;padding:10px 0;text-transform:uppercase;height:12px;font-size:10.5px;overflow:hidden;background:#2c2c2b;background:-moz-linear-gradient(top, #2c2c2b 0%, #262426 49%, #232222 50%, #1e201e 100%);background:-webkit-gradient(linear, left top, left bottom, color-stop(0%,#2c2c2b), color-stop(49%,#262426), color-stop(50%,#232222), color-stop(100%,#1e201e));background:-webkit-linear-gradient(top, #2c2c2b 0%,#262426 49%,#232222 50%,#1e201e 100%);background:-o-linear-gradient(top, #2c2c2b 0%,#262426 49%,#232222 50%,#1e201e 100%);background:-ms-linear-gradient(top, #2c2c2b 0%,#262426 49%,#232222 50%,#1e201e 100%);background:linear-gradient(top, #2c2c2b 0%,#262426 49%,#232222 50%,#1e201e 100%);filter:progid:DXImageTransform.Microsoft.gradient( startColorstr='#2c2c2b', endColorstr='#1e201e',GradientType=0 );}#footer p{margin:0 10px}#footer a{color:#818181;padding-right:15px;}#footer .copyright{float:right;color:#818181;}  


html {
     height:100%
}
body {
     height:100%
}
#container {
     position:relative;
     min-height:100%;
     _height:100%; /* for IE6 as it doesnt understand min-height */
}
#content {
     padding-bottom:100px; /* assuming your footer height is 100px */
}
 
#footer {
     position: relative;
     margin-top:-50px;
     /* move the footer up negatively exactly the same height
         as the footer so that its back in the view and always
         appears to rest at the bottom
         of the page */
}


#searchBox{width:600px;}
#searchBox{font-size:25px;line-height:30px;height:30px;outline:none;border:1px solid #AAA;}
#searchBox{height:40px;clear:both;}
#search-submit{width:100px;}
#search-submit{height:40px;}
.red-button{height:32px;border:none 0;outline:none 0;font-size:14px;color:#FFF;cursor:pointer;font-weight:bold;background:#ef3625;background:-moz-linear-gradient(top, #ef3625 0%, #d02f20 100%);background:-webkit-gradient(linear, left top, left bottom, color-stop(0%,#ef3625), color-stop(100%,#d02f20));background:-webkit-linear-gradient(top, #ef3625 0%,#d02f20 100%);background:-o-linear-gradient(top, #ef3625 0%,#d02f20 100%);background:-ms-linear-gradient(top, #ef3625 0%,#d02f20 100%);background:linear-gradient(top, #ef3625 0%,#d02f20 100%);filter:progid:DXImageTransform.Microsoft.gradient( startColorstr='#ef3625', endColorstr='#d02f20',GradientType=0 );}
.search-icon{background:url('http://a.blekko-img.com/045/gz/theme21/imgs/serp08.png') no-repeat -212px 0;width:20px;height:20px;display:inline-block;}

div.large{font-size:50px; font-family:  Helvetica, sans-serif; font-size: normal; line-height: normal;}

</style> 
</head>
<body>
<div class="h7">
<table cellpadding="0">
<tr VALIGN=BOTTOM>
<td>
<div class="large">
<a href="index.html"><b><span style="color:white;">Har</span><span style=color:red;">vix</span></b></a>
</div>
</td>
<td>
<form id="searchForm" name="searchForm" action="http://harvix.com/hsearch3.cgi" onsubmit="submitted('h'); return false">
<input id="searchBox" autofocus="autofocus" autocomplete="off" type="text" spellcheck="false" name="q" value="$query"  />
<button type="submit" class="red-button"  href="javascript:void(0);" id="search-submit" ><span class="search-icon"></span></button>
</form>
</td>
</tr>
</table>
</div>
<p>
&nbsp;
<p>
&nbsp;
<p>
&nbsp;
<p>
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


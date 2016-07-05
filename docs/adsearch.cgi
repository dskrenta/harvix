#!/usr/bin/perl

use strict;
use URI::Fetch;
use Data::Dumper;
use Encode;
use XML::Simple;


my %escapes;
setup_escapes();

my $query = parse_query();

my $affiliate   = '78752';
my $token       = 'A814D87FA1154101A8FCC76E8DC915A3';
my $rid         = 'harvix.com';
my $qu          = urlencode($query);
my $ip_address  = $ENV{ 'REMOTE_ADDR' };
my $fwd         = urlencode( $ENV{ 'HTTP_X_FORWARDED_FOR' } );
my $st          = 'typein';     # typein, link, context
my $page_url    = urlencode( 'http://' . $ENV{'SERVER_NAME'} . $ENV{'SCRIPT_NAME'} . $ENV{'QUERY_STRING'} );
my $ua          = urlencode( $ENV{ 'HTTP_USER_AGENT' } );
my $lang        = urlencode( $ENV{ 'HTTP_ACCEPT_LANGUAGE' } );
my $pn          = 1;        # page number
my $r           = 25;       # number of results requested; max is 25
my $filter      = 'yes';    # adult filter
my $mobile      = 'no';       # mobile device user

my $request =   'http://meta.7search.com/feed/xml.aspx?affiliate=' . $affiliate .
                '&token=' . $token .
                '&rid=' . $rid .
                '&qu=' . $qu .
                '&pn=' . $pn .
                '&r=' . $r . 
                '&filter=' . $filter .
                '&ip_address=' . $ip_address .
                '&st=' . $st .
                '&page_url=' . $page_url .
                '&lang=' . $lang .
                '&mobile=' . $mobile .
                '&ua=' . $ua . 
                '&x_forwarded_for=' . $fwd;

# my $request = 'http://meta.7search.com/feed/xml.aspx?affiliate=78752&token=A814D87FA1154101A8FCC76E8DC915A3&rid=valid-rid-goes-here&qu=car&pn=1&r=20&filter=no&ip_address=24.5.9.163&st=typein&page_url=url-of-page-showing-the-ads-goes-here&lang=en-US&mobile=no&ua=Mozilla%2f5.0+(Macintosh%3b+Intel+Mac+OS+X+10_7_5)+AppleWebKit%2f537.36+(KHTML%2c+like+Gecko)+Chrome%2f30.0.1599.69+Safari%2f537.36&x_forwarded_for=HTTP_X_FORWARDED_FOR-value-goes-here';


print "Content-type: text/html\n\n";
print "<body>\n";

#print "<pre>\n";

#print "affiliate = $affiliate<br>\n";
#print "token = $token<br>\n";
#print "rid = $rid<br>\n";
#print "qu = $qu<br>\n";
#print "ip_address = $ip_address<br>\n";
#print "fwd = $fwd<br>\n";
#print "st = $st<br>\n";
#print "page_url = $page_url<br>\n";
#print "ua = $ua<br>\n";
#print "lang = $lang<br>\n";
#print "pn = $pn<br>\n";
#print "r = $r<br>\n";
#print "filter = $filter<br>\n";
#print "mobile = $filter<br>\n";

#print "<p>\n";

#print "request = $request<p>\n";

print "<p><hr><p>\n";

my $xml_page = URI::Fetch->fetch( $request );
my $xml_text = $xml_page->content();
my $xml = XMLin( $xml_text );

if ( defined $xml && defined $xml->{'SITE'} )
{
    foreach my $ad ( @{ $xml->{'SITE'} } )
    {
	
        foreach my $field ( keys %$ad )
        {
       		#print "$field: " . $ad->{ $field } . "<br>\n";
	
		my @values;

		if ($field eq "HTTPLINK")
                {
                        $values[0] = $ad->{ $field };
                }

		if ($field eq "URL")
                {
                        $values[1] = $ad->{ $field };
                }

		if ($field eq "INDEX")
                {
                        $values[2] = $ad->{ $field };
                }
	
		if ($field eq "NAME")
		{
			$values[3] = $ad->{ $field };
		}

		if ($field eq "DESCRIPTION")
                {
                        $values[4] = $ad->{ $field };
                }

		if ($field eq "BID")
                {
                        $values[5] = $ad->{ $field };
                }

		#print"<a href=\"$values[1]\">$values[3]</a><p>$values[4]</p>$values[0]\n";
	
		print "$values[0]<p>\n";
		print "$values[1]<p>\n";
		print "$values[2]<p>\n";
		print "$values[3]<p>\n";
		print "$values[4]<p>\n";
		print "$values[5]<p>\n";
	}
	
	print "<hr></hr><p>\n";
    }
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
	#$query =~ s/\+/ /g;
	$query =~ s/[\[\]\(\)\.\?]/ /g;
	$query =~ s/^\s*//;
	$query =~ s/\s*$//;
	$query =~ s/\s+/ /g;
	
	return $query;
}

# $VAR1 = {
#           'SITE' => [
#                     {
#                       'HTTPLINK' => 'http://www.AnswerGrab.com',
#                       'URL' => 'http://meta.7search.com/click/click.aspx?x=q8DGRawHm9Q9X2jIVSGLvA%3d%3d_pIrf1R9ZQM%2fdy48Yj%2bFy%2bm23qJE4pSacA%2bNsWECoEqxeeuVzngubeERTOjg2w1%2fDatYq%2bhM6oKZf%2f6lRNDLosGOq5wnW9P2yJTnaO2mCDBPQG8YtxFoyYJHyQbbrsIc3atx%2f5qXxirQRPqHNtxR8O%2fVp0KQBJTugT79ETLPwE1OGW7i46kn4dqT4IPypOJ54xwjf0Aa7%2bEIF%2bDD4OjEWWPOr285ck2atPTo%2f52qpVq53Br2gkb6JQXP9YjC6PxO%2f%2fxtv4LWY59AjJI4%2f9DKv6Q%3d%3d',
#                       'NAME' => 'Looking For Car?',
#                       'INDEX' => '1',
#                       'DESCRIPTION' => 'Find What You Need. Search For Car Here Now!',
#                       'BID' => '0.07'
#                     },
#                     {
#                       'HTTPLINK' => 'http://www.VivaSearch.com/',
#                       'URL' => 'http://meta.7search.com/click/click.aspx?x=q8DGRawHm9Q9X2jIVSGLvA%3d%3d_pIrf1R9ZQM%2fdy48Yj%2bFy%2bm4XG3Mjrm1rIpk66qEJ%2bhh5r3KDuERH2jZrCnpGlgHyLYrBp7hQASWhPBFBGp5KrgiRoJxP60TMw36S%2fvnvhVm2zwMWH5PKEdnXsBttQC7siOviCW5Gsyb6hZ%2fhSLGswB2ktXFcLtTGRUK1QB2zfR3kZWtka2ZyKYmJ2VAIGx5Tmx5lv0MasqBbZGGwgG2O9o23A54S7aa1JgEOriJqJ6eMuOSyrifcJHbTKnJ9lIg5SqgrEQZmGfSYatTTVGnprA%3d%3d',
#                       'NAME' => 'Find Car',
#                       'INDEX' => '2',
#                       'DESCRIPTION' => 'Stop searching for Car. Find it here!',
#                       'BID' => '0.06'
#                     },
#                     {
#                       'HTTPLINK' => 'http://Shopr.com',
#                       'URL' => 'http://meta.7search.com/click/click.aspx?x=q8DGRawHm9Q9X2jIVSGLvA%3d%3d_pIrf1R9ZQM%2fdy48Yj%2bFy%2bsNEojw0hUpHE6mbB7SBjmTEBsdqhMNzwlydv%2f%2b0xDvaFbcEZkJJtqQRbbiWvfEWYDiVOwNaCrYeyhbHheg2Ke5H658qCa%2fIsXDWuc2PlvVRLzLVtCvPQa8gOhy0num3vgCVghtl74mg%2bBPumE%2fHGYuElHOkCkbF9IJPqIaM2mCvBSWdlXn7Phq%2fVflxnrxzKrnmdOzf4rDVS1ACmOzgh%2bkqB%2fAG4Ld5uDpUuV7JBS%2fIMO1n9bk9BxOCsAb2OTSkig%3d%3d',
#                       'NAME' => 'Looking For Car?',
#                       'INDEX' => '3',
#                       'DESCRIPTION' => 'Stop searching for Car. Find it here!',
#                       'BID' => '0.05'
#                     },
#                     {
#                       'HTTPLINK' => 'http://www.AnswerGrab.com',
#                       'URL' => 'http://meta.7search.com/click/click.aspx?x=q8DGRawHm9Q9X2jIVSGLvA%3d%3d_pIrf1R9ZQM%2fdy48Yj%2bFy%2bt0QvrgrhbD4LV6ESCE8wPbg8f9KMvlTJd7GsIj1AgUniJHIwi9wFfVKvUt8ml0E6gACDqLhoE2Zk4Jpm62nDdsEyycIiZzRL8zIRoA5%2fGD1OLoF1BFzKA0IxqUKHfm58oe6HpsbDkDMVauto27pInvN4H6vyajACJ1%2fZCI0%2bgHc4HvpX3UnRZR%2bT%2bi36CPCDybKa4%2fYBV%2fhSy4%2fASUIbenK8QeADYxEyuGeQzRZ4chFfNKOSNc3ph80TwXA7OKZTg%3d%3d',
#                       'NAME' => 'Searching For Car?',
#                       'INDEX' => '4',
#                       'DESCRIPTION' => 'Get The Best Deals on Car And More Now!',
#                       'BID' => '0.05'
#                     },
#                     {
#                       'HTTPLINK' => 'http://www.iMotors.com',
#                       'URL' => 'http://meta.7search.com/click/click.aspx?x=q8DGRawHm9Q9X2jIVSGLvA%3d%3d_pIrf1R9ZQM%2fdy48Yj%2bFy%2blc8bgmYzv%2fHvMgSqWc4ZzGlPxIeIUdfTCm%2bCutVftTvHi%2fVStmwJk7yT5cQpYtBUKmpTt8lHaIRTt16RVla7M7q5eaVwgj8YqD%2bV55O6lc2nSKEFLFemVeP92iYSNs9JU6cqoMhao9tp3wC65rNoLSAkLlOxftoRZEC00JG%2fbPSy2BVmvWgPBWgxQhzv5f0h054p4GrjyKbIM8nOeS79qLtGpz%2f%2fhEB2eI%2fOO2rnMEc',
#                       'NAME' => '2013 New Car Clearance',
#                       'INDEX' => '5',
#                       'DESCRIPTION' => 'All Remaining Models Must Be Sold. Act Today to Get Your Free Quote and Save $1000s!',
#                       'BID' => '0.05'
#                     },
#                     {
#                       'HTTPLINK' => 'http://www.VivaSearch.com/',
#                       'URL' => 'http://meta.7search.com/click/click.aspx?x=q8DGRawHm9Q9X2jIVSGLvA%3d%3d_pIrf1R9ZQM%2fdy48Yj%2bFy%2bkyzyYDLv%2fJT9jheEE1Xdtewm3Es8IJ2vYPi%2fuIRyivMvqGnN%2fMFE2T9u%2fBVAhHsJ%2ftifWWCDwuqado83bSOK%2f7Ho19T4imFZj2e%2bbDVCP0rt6StEoPxFurRAzJHywWj0ceJahPmFJybq3AhgNSfRSakQ7i%2fQbXsuIlzrh8Hmn4jYQ7GLb9K%2fF0FYaDD1HXcw%2f1e76XfT2nW4caut40w9QDrQvuX6DtdVgFu6%2bS5f%2buirGH%2fPNTzYIm%2fFvqbG2QDDA%3d%3d',
#                       'NAME' => 'Looking for Car?',
#                       'INDEX' => '6',
#                       'DESCRIPTION' => 'Find Car & so much more at our online Marketplace and Price Comparison site!',
#                       'BID' => '0.03'
#                     },
#                     {
#                       'HTTPLINK' => 'http://www.VivaSearch.com/',
#                       'URL' => 'http://meta.7search.com/click/click.aspx?x=q8DGRawHm9Q9X2jIVSGLvA%3d%3d_pIrf1R9ZQM%2fdy48Yj%2bFy%2bjTZm5pgQP0blDip17TpxjWiTEVKIn5onKkhpkqS6prJ3uopaLw7BFOucBv3A5jYVjZ18qHu%2fai3uTPVURu6R9wFO47FQk6oSwT8daBG5y4qjxEGhU260vuaYP%2bOu%2fGJhY4e3zyD4Jzicteu9wRo5ChNtt1spVLgSvsL8COHE9VoJ11UUebkyxch0BUydlhWdYyFj3CyYsb%2fCxSGnZG%2feMxzL8yQvtw%2fyoH9vhOscOe4iusQM81iueEn0sd5wenyDA%3d%3d',
#                       'NAME' => 'Looking for Car',
#                       'INDEX' => '7',
#                       'DESCRIPTION' => 'Get all of the information you need on Car.',
#                       'BID' => '0.02'
#                     },
#                     {
#                       'HTTPLINK' => 'http://www.Compare.US',
#                       'URL' => 'http://meta.7search.com/click/click.aspx?x=q8DGRawHm9Q9X2jIVSGLvA%3d%3d_pIrf1R9ZQM%2fdy48Yj%2bFy%2bmSiWCyH4Ld64tJS6SVH0XfQ3qtNY7h8egSv4eWzSc%2fYR2HN9bpKnLl092j0xng%2fE8ux7qwIyKyiDY7g3wcDYMlZzQafmqz8CSRa1hnz503e4N7BtyZNOUO2xn7ymQezQ5t7ypRCInyB4W%2b0hxNfkjNFmtuWuRg1h4UxAU8JYepbbLwNl%2fCTU68uD2VWxF%2fJLULP4X%2bpozgkoGiA67AHlSuVAkSKDP5%2bAwvFXh7p%2bDqAixC2qY6DULKlY1ZwEPT%2f7A%3d%3d',
#                       'NAME' => 'Review & Compare Relevant Web Sites',
#                       'INDEX' => '8',
#                       'DESCRIPTION' => 'Find a list of top brand web sites for you to compare and view. All listed on one page for convenience.',
#                       'BID' => '0.02'
#                     }
#                   ]
#         };



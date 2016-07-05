#!/usr/bin/perl

#       Ufinde Search version 1.0
#       
#       Coppyright (C) 2013 Ufinde Search
#       Designed and Built by David Skrenta 
#       All Contents of File and Related Files Protected by Ufinde

use strict;
use URI::Fetch;
use Encode;
use XML::Simple;

my %escapes;
setup_escapes();

print "Content-type: text/html\n\n";

my $query = parse_query();

print_header($query);

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

#7search ad stuff

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
my $r           = 3;       # number of results requested; max is 25
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


my $xml_page = URI::Fetch->fetch( $request );
my $xml_text = $xml_page->content();
my $xml = XMLin( $xml_text );

my $count = 0;

if ( defined $xml && defined $xml->{'SITE'} )
{
	my @ads;

	if ( ref $xml->{SITE} eq 'ARRAY' )
	{
		push @ads, @{ $xml->{'SITE'} };
	}
	
	else
	{
		push @ads, $xml->{SITE};
	}

     	foreach my $ad ( @ads )
        {
		my $adhtml = qq{
			<div class="well">
			<a href="$ad->{'URL'}">
			<span style="color:#195189;"><h4>$ad->{'NAME'}</h4></span>
			</a>
			<p>$ad->{'DESCRIPTION'}<p>
			<span style="color:green">$ad->{'HTTPLINK'}</span>
			<small><p>Sponsored Link - $query</small>
			<p><small><b>Donation Value: </b><span style="color:red">$ad->{'BID'}</span></small></p>
			</div>
		};
		#print $adhtml;

		if ($count == 0)	
		{
			my $adhtmlv2 = qq{
				<iframe src="$ad->{'URL'}"></iframe>
			};
			print $adhtmlv2;
		}
	
		else
		{
			#Nothing
		}

		$count ++;
       	}
}
			
else
{
	#No Ads Present - Display Nothing
}		
			
print_footer();

#SUBS

sub print_header
{
	my ( $query ) = @_;

	$query =~ s/[<>\&]//g;

print <<EOF

<!DOCTYPE html>

<!--
Harvix reserves all of our rights, including but not limited to any and all copyrights, 
trademarks, patents, trade secrets, and any other proprietary right that we may have 
in our web site, its content, and the goods and services that may be provided. The 
use of our rights and property requires our prior written consent. We are not 
providing you with any implied or express licenses or rights by making services 
available to you and you will have no rights to make any commercial uses of our 
web site or service without our prior written consent.

Any violator will be prosecuted to the full extent of law and may face civil and criminal
charges and large monetary fines. 
-->

<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="">
    <meta name="author" content="">
    <link rel="shortcut icon" href="">

    <title>Harvix.org - $query</title>

    <!--Ufinde CSS-->
    <link href="http://harvix.com/search/ufinde/css/bootstrap.min.css" rel="stylesheet">
    <link href="http://harvix.com/search/ufinde/css/dashboard.css" rel="stylesheet">

    <!--Ufinde Onpage CSS-->
    <style>
    #scrollable {
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
	width:400px;
	height:200px;
     float:left;      
  }

.itemfacts{
        width:300px;
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
  height:250px;
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

.well-spec{min-height:20px;padding:19px;margin-bottom:20px;background-color:white;border:1px solid #e3e3e3;border-radius:4px;-webkit-box-shadow:inset 0 1px 1px rgba(0,0,0,.05);box-shadow:inset 0 1px 1px rgba(0,0,0,.05)}

#count{
     float:right;      
}

#upper{
text-transform:uppercase;
}

a:link {color:black; text-decoration: none;}      /* unvisited link */
a:visited {color:black; text-decoration: none;}  /* visited link */
a:hover {color:black; text-decoration: none;}  /* mouse over link */
a:active {color:black; text-decoration: none;}  /* selected link */
  </style>

  </head>

  <body>
  
    <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
      <div class="container-fluid">
        <div class="navbar-header">
          <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
            <span class="sr-only">Toggle navigation</span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
          <a class="navbar-brand" href="http://harvix.org/search">Harvix.org</a>
        </div>
        <div class="navbar-collapse collapse">
          <form class="navbar-form">
            <input type="text" class="form-control" action="http://harvix.com/search/ufinde/org-searchv2.cgi" onsubmit="submitted('h'); return false" name="q"  class="search-query" value="$query">
	    <button type="submit" class="btn"><strong>Search</strong></button>
          </form>
        </div>
      </div>
    </div>

    <div class="container-fluid">
      <div class="row">
        <div class="col-sm-3 col-md-2 sidebar">
          <ul class="nav nav-sidebar">
            <li class="active"><a href="http://harvix.com/search/ufinde/search2.cgi?q=$query">Web</a></li>
          </ul>
        </div>
	<div class="col-sm-9 col-sm-offset-3 col-md-10 col-md-offset-2 main">
<!-- START SEARCH PAGE -->

EOF
;
}

sub print_footer
{
print <<EOX

<!-- END SEARCH PAGE -->
        </div>
      </div>
    </div>
  </body>
</html>

EOX
;
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
        my $query = $ENV{QUERY_STRING} || shift || "Casino";

        $query =~ s/q=//;
        $query = urldecode($query);
        #$query =~ s/\+/ /g;
        $query =~ s/[\[\]\(\)\.\?]/ /g;
        $query =~ s/^\s*//;
        $query =~ s/\s*$//;
        $query =~ s/\s+/ /g;

        return $query;
}


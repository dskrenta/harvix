#!/usr/bin/perl

#       Funzilla Search version 1.0
#       
#       Coppyright (C) 2015
#       All Contents of File and Related Files Protected by Funzilla

use strict;
use JSON;
use URI::Fetch;
use Encode;
use Number::Spell;
use XML::Simple;
use Data::Dumper;

my $catsort = {
	'WIKI'			=> 100,
	'ORIG'			=> 90,
	'IMAGE'			=> 80,
};


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

my $json_page = URI::Fetch->fetch("http://blekko.com/api/p1?q=$query&auth=c31c6fd0");
my $json_text = $json_page->content();
my $json = decode_json( $json_text );


if ( ! defined $json )
{
    print "no results\n";
    exit(0);
}

if ( ! defined $json->{tags} )
{
    print "no results\n";
    exit(0);
}


#print_header($query);

my $dropdowncount = 0;

# foreach my $tag ( @{ $json->{tags} } )

foreach my $tag ( sort { $catsort->{ $b->{name} } <=> $catsort->{ $a->{name} } } @{ $json->{tags} } )
{
    	my $category = $tag->{name};
    	my $results = $tag->{results};

	#Spell Number
        my $numberspell = spell_number($dropdowncount);

	#TAGS + CATEGORIES 

	if($category eq "NAV")
	{
		#Display Nothing
	}	

	elsif($category eq "RETAIL")
	{
		#Display Nothing
	}

	elsif($category eq "WIKI")
	{
		my $wiki_count = 1;

       		foreach my $result ( @{ $results } )
        	{
			if ($wiki_count == 1)
			{
				#Declare Variables
                		my $title = $result->{'t'};
                		my $url = $result->{'u'};
                		my $rurl = $result->{'du'};
                		my $snippet = $result->{'ws'};
				my $img = $result->{'wi'};
		
				#Shorten Snippet
                		$snippet =~ s/<\/?(b|strong)>//g;
                		if ( length($snippet) > 500)
                		{
					$snippet = substr($snippet, 0, 500);
					$snippet =~ s/\s[^\s]*$//;
                       			$snippet .= '';
                		}		

				#Print Alongside HTML
				my $wikihtml = qq{
					<!--Main Wiki Box-->
					<div class="well">
					<table cellspacing="10">
					<tr><td>
					<h3>$title</h3>
					<p>$snippet</p>
					<small>$url</small>
					</td><td>
					<img src="$img" class="img-rounded" alt="" width="200px" onerror="this.style.display='none'"/>
					</td></tr>
					</table>
					</div>
				};
				print $wikihtml;
			}

			else
			{
				#Display Nothing 
			}
			
			$wiki_count ++;
		}
	}
		
	elsif($category eq "ORIG")
        {
		my $count = 1;
		foreach my $result ( @{ $results } )
        	{
			#Declare Variables
                        my $title = $result->{'t'};
                       	my $url = $result->{'u'};
                        my $rurl = $result->{'du'};
                        my $snippet = $result->{'s'};
                        $snippet =~ s/<\/?(b|strong)>//g;
                        my $img_id = $result->{'i'};
                        my $img_data = $json->{img_map}->{$img_id};

                        #Shorten Snippet
                        if ( length($snippet) > 500 )
                        {
                        	$snippet = substr($snippet, 0, 500);
                               	$snippet =~ s/\s[^\s]*$//;
                            	$snippet .= ' ...';
                      	}

			if ($count == 1)
			{
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

                                	#foreach my $ad ( @{ $xml->{'SITE'} } )
                                	foreach my $ad ( @ads )
                                	{
						my $adhtml = qq{
							<div class="well">
								<div class="row">
									<div class="col-md-6">
										<a href="$ad->{'URL'}">
										<span style="color:#195189;"><h4>$ad->{'NAME'}</h4></span>
										</a>
										<p>$ad->{'DESCRIPTION'}<p>
										<span style="color:green">$ad->{'HTTPLINK'}</span>
										<small><p>Sponsored Link - $query</small>
										<!--<p><small><b>Donation Value: </b><span style="color:red">$ad->{'BID'}</span></small></p>-->
									</div>
									<div class="col-md-6">
										<p>Link Preview:</p>
										<iframe frameborder="0" src="http://harvix.com"></iframe>
									</div>
								</div>
							</div>
						};
						print $adhtml;
                                	}
                        	}
			
				else
				{
					#No Ads Present - Display Nothing
				}		
			}			

			else 
			{
				if ( $img_data ne '' )
                        	{
                        		my $ifhtml = qq{
                                        	<div class="well">
						<table cellpadding="10">
                                        	<tr><td>
						<a href="$url" target="_blank">
                                        	<span style="color:#195189;">
						<h3>$title</h3>
						</span>
                                        	<p>$snippet</p>
                                        	<span style="color:green">
						<small>$rurl</small>
						</span>
                                        	</a>
						</td><td>
                                        	<img src="$img_data" class="img-rounded" alt="" height="200px"></img>
                                        	</td></tr>
                                        	</table>
                               			</div>
					};
                                	print $ifhtml;
                   		}

                    		else
                        	{
                     			my $elsehtml = qq{
                                       		<div class="well">
                                        	<a href="$url" target="_blank">
                                        	<span style="color:#195189;">
						<h3>$title</h3>
						</span>
                                       		<p>$snippet</p>
                                        	<span style="color:green">
						<small>$rurl</small>
						</span>
                                        	</a>
                                	        </div>
                           		};
                                	print $elsehtml;
				}
			}
			$count ++;	
        	}
        }

	elsif($category eq "IMAGE")
	{
		#Print Before Alongside HTML		
		my $before = qq{
			<div class="well">
			<div id="scrollable">
			<div id="items">	
		};
		print $before;

                foreach my $result ( @{ $results } )
                {
                        #Declare Variable
                        my $url = $result->{'u'};

			#Print Alongside HTML
			my $imagehtml = qq{
				<div class="item">
				<a href="$url" target="_blank">
				<img src="$url" height="280px" alt="" onerror="this.style.display='none'"></img>
				</a>
				</div>
			};
			print $imagehtml;	
                }
		
		#Print After Alongside HTML
		my $after = qq{
			</div>
			</div>		
			</div>
		};
		print $after;
        }
	
        else
        {
		#Print Before Category HTML
		my $beforecathtml = qq{
			<h2 class="sub-header"><div id="upper">$category</div></h2>
			<div class="well-spec">
			<div id="scrollable">
			<div id="items">
		};
		print $beforecathtml;
		
        	foreach my $result ( @{ $results } )
        	{
                	#Define Variables
			my $title = $result->{'t'};
                	my $url = $result->{'u'};
               		my $rurl = $result->{'du'};
               		my $snippet = $result->{'s'};
                	$snippet =~ s/<\/?(b|strong)>//g;
			my $img_id = $result->{'i'};
                        my $img_data = $json->{img_map}->{$img_id};              
  
			#Shorten Snippet
			if ( length($snippet) > 150 )
                	{
                        	$snippet = substr($snippet, 0, 150);
                        	$snippet =~ s/\s[^\s]*$//;
                        	$snippet .= ' ...';
                	}

			#Alongside Category HTML
			my $alongsidecat = qq{
				<div class="item2">
			        <div class="hero-unit-spec">
				<a href="$url" target="_blank">
                               	<span style="color:#195189;">
                            	<h4>$title</h4>
                             	</span>
                           	<p>$snippet</p>
                           	<span style="color:green">
                           	<small>$rurl</small>
                              	</span>
                              	</a>
				</div>
				</div>
			};
			print $alongsidecat;
		}

		#Print After Category HTML
		my $aftercathtml = qq{
			</div>
			</div>
			</div>
		};
		print $aftercathtml;
	}      
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

    <title>Funzilla Search - $query</title>

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
          <a class="navbar-brand" href="http://harvix.org/search">Funzilla Search</a>
        </div>
        <div class="navbar-collapse collapse">
          <form class="navbar-form">
            <input type="text" class="form-control" action="http://harvix.com/search/ufinde/funzillaSearch.cgi" onsubmit="submitted('h'); return false" name="q"  class="search-query" value="$query">
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


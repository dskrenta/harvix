#!/usr/bin/perl

#       Harvix Search version 2.0
#       
#       Coppyright (C) 2013 Harvix Search
#       Designed and Built by David Skrenta CEO, the Harvix Team 
#       All Contents of File and Related Files Protected by Harvix

use strict;
use JSON;
use URI::Fetch;
use Encode;
use Number::Spell;
use CGI;

my $catsort = {
	'WIKI'			=> 100,
	'ORIG'			=> 90,
	'IMAGE'			=> 80,
};


my %escapes;
setup_escapes();

my $query = parse_query();

print "Content-type: text/html\n\n";

print_header($query);

my $ad_html = qq{
	<iframe hidden src="http://harvix.com/search/sub/index.php?terms=$query"></iframe>
};
print $ad_html;

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
					<div class="row-fluid">
					<!--Main Wiki Box-->
					<div class="span8 well orange click" id="blogone">
					<h3>$title</h3>
					<p>$snippet</p>
					<small>$url</small>
					</div>
					<!--Wiki Image Box-->
					<div class="span4">
					<a href="$img"><div class="container-img" style="background:url('$img'); background-size:cover;"></div></a>
					</div>
					</div> <!--/row-fluid-->
					<!--Wiki Expand-->
					<div class="blog-post-item one">
					<div class="arrow-up left"></div>
					<p>
					<iframe src="$url" height="500px" width="100%" frameborder="0"></iframe>
					</p>
					</div>
				};
				print $wikihtml;
			}

			else
			{
			}
			
			$wiki_count ++;
		}
	}
		
	elsif($category eq "ORIG")
        {
        	#Display Facts and Wolfram Aplha Boxes
		my $factswolfhtml = qq{
                	<div class="row-fluid">
                        <!--Facts Box-->
                        <div class="span4 well blue click" id="blogtwo">
                        <h1 class="text-left">Facts</h1>
                        <p class="text-left">$query</p>
                        </div>
			<!--Wolfram Alpha Box-->
			<div class="span8 no-padding">
			<div style=\"background: #ffffff url(http://www.domaine-saint-pierre.fr/skin/frontend/default/default/images/home/loading.gif) no-repeat 50% 5%;\">
			<iframe src="http://harvix.com/wolf.cgi?$query" allowTransparency="true"  width="632px" height="300px" frameborder="0"></iframe>
			</div>
			</div>
			</div> <!--/row-fluid-->
			<!--Facts Expand-->
			<div class="blog-post-item two">
			<div class="arrow-up leftsmall"></div>
			<p>
			<iframe src="http://harvix.com/facts4.cgi?$query" width="100%" height="328px" class="restricted" overflow-y="hidden" frameborder="0"></iframe>
			</p>
			</div>
		};
		print $factswolfhtml;

		my $count = 0;
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
			
			if ($count < 6)
			{
				if ( $img_data ne '' )
                                {
                                        my $ifhtml = qq{
                                                <div class="row-fluid">
                                                <div class="span12 tealblue well">
                                                <div class="row-fluid">
                                                <div class="span8">
                                                <a href="$url" target="_blank">
                                                <h3>$title</h3>
                                                <p>$snippet</p>
                                                <small>$rurl</small>
                                                </a>
                                                </div> <!--1-->
                                                <div class="span4">
                                                <a href="$img_data"><img src="$img_data" width="250px" alt="" /></a>
                                                </div> <!--2-->
                                                </div> <!--/row-fluid--> <!--3-->
                                                </div> <!--4-->
                                                </div> <!--/row-fluid--> <!--5-->
                                        };
                                        print $ifhtml;
                                }

                                else
                                {
                                        my $elsehtml = qq{
                                                <div class="row-fluid">
                                                <div class="span12 tealblue well">
                                                <a href="$url" target="_blank">
                                                <h3>$title</h3>
                                                <p>$snippet</p>
                                                <small>$rurl</small>
                                                </a>
                                                </div>
                                                </div> <!--/row-fluid-->
                                        };
                                        print $elsehtml;
                                }
			}
		
			else
			{
				if ($count == 7)
				{
					my $expandhtml = qq{
                        			<div class="row-fluid">
                        			<div class="span4 well blue">
						<a href="http://harvix.com/search/web.cgi?q=$query" target="_blank">
						<h1>Top Results</h1>
                        			<p>$query</p>
						</a>
                        			</div>
						<div class="span8 tealblue well">
                                                <a href="$url" target="_blank">
                                                <h3>$title</h3>
                                                <p>$snippet</p>
                                                <small>$rurl</small>
                                                </a>
                                                </div>
						</dib> <!--/row-fluid-->
                			};
                			print $expandhtml;
				}
			}
			
			$count ++;
        	}
        }

	elsif($category eq "IMAGE")
	{
		#Print Before Alongside HTML		
		my $before = qq{
			<div class="row-fluid">
			<div  class="span8 well no-padding">
                	<div class="flexslider" id="slider">
                    	<ul class="slides">
		};
		print $before;

                foreach my $result ( @{ $results } )
                {
                        #Declare Variable
                        my $url = $result->{'u'};

			#Print Alongside HTML
			my $imagehtml = qq{
				<li>
				<img src="$url" alt=""></img>
				</li>
			};
			print $imagehtml;	
                }
		
		#Print After Alongside HTML
		my $after = qq{
			</ul>
			</div>
			</div>
			<div class="span4 well blue">
                        <a href="http://harvix.com/search/images.cgi?q=$query" target="_blank">
			<h1>Images</h1>
                        <p>$query</p>
			</a>
                        </div>
			</div> <!--/row-fluid-->
		};
		print $after;
        }
	
        else
        {
		#Display Category Drop Down Box
		my $drophtml = qq{
			<div class="row-fluid">
			<div class="span4 well blue click" id="blog$numberspell">
                        <h1><div class="lowercase">$category</div></h1>
			<p>$query</p>
			</div>	
		};
		print $drophtml;		

		my $rescount = 1;
		my $print_close = 0;

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

			if ($rescount == 1)
			{
				#Display Results
				my $cathtml = qq{
                                	<div class="span8 tealblue well">
                                	<a href="$url" target="_blank">
					<h3>$title</h3>
                              		<p>$snippet</p>
                               		<small>$rurl</small>
					</a>
					</div>
					</div> <!--/row-fluid-->
				};
				print $cathtml;
			}

			else
			{
				if ( $rescount == 2 )
				{
					my $dropdownhtml = qq{
						<div class="blog-post-item $numberspell">
						<div class="arrow-up leftsmall"></div>
					};
					print $dropdownhtml;
					$print_close = 1;
				}
				
				if ( $img_data ne '' )
                                {
                                        my $ifelshtml = qq{
                                                <div class="row-fluid">
                                                <div class="span12 tealblue well">
                                                <div class="row-fluid">
                                                <div class="span8">
                                                <a href="$url" target="_blank">
                                                <h3>$title</h3>
                                                <p>$snippet</p>
                                                <small>$rurl</small>
                                                </a>
                                                </div>
                                                <div class="span4">
                                                <a href="$img_data"><img src="$img_data" width="250px" alt="" /></a>
                                                </div>
                                                </div> <!--/row-fluid-->
                                                </div>
                                                </div> <!--/row-fluid-->
                                        };
                                        print $ifelshtml;
                                }

                                else
                                {
                                        my $whenelsehtml = qq{
                                                <div class="row-fluid">
                                                <div class="span12 tealblue well">
                                                <a href="$url" target="_blank">
                                                <h3>$title</h3>
                                                <p>$snippet</p>
                                                <small>$rurl</small>
                                                </a>
                                                </div>
                                                </div> <!--/row-fluid-->
                                        };
                                        print $whenelsehtml;
                                }
			}

			$rescount ++;
       		}

		if ( $print_close )
		{
                	print "</div>\n";
		}
	}      

	$dropdowncount ++;  
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
    <title>$query - Harvix</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="$query">
    <meta name="author" content="Harvix Search DEV">

    <!-- Harvix Search Page Styles -->
    <link href="http://harvix.com/search/css/bootstrap.css" rel="stylesheet">
    <link href="http://harvix.com/search/css/bootstrap-responsive.css" rel="stylesheet">	
    <link href="http://harvix.com/search/css/flexslider.css" rel="stylesheet">
    <link href="http://harvix.com/search/css/style.css" rel="stylesheet">

    <style type="text/css">      
body {padding-top: 60px; padding-bottom: 40px;}
.container-img {width: 300px; height: 300px; background-size: contain; background-repeat: no-repeat; background-position: 50% 50%;}
.lowercase {text-transform:lowercase;}
#upper {text-transform:uppercase;}
.restricted{overflow-y: hidden}

#nav-bar-top {
  width: 100%;
  height:50px;
  position: absolute;
  margin-top:-60px;
  background: rgba(55,55,55,0.75);
  margin-left: -50px;
  z-index: 999;
}
#nav-bar-top form {
  width: 539px;
  margin-left: 160px;
}
  #searchBox {
    outline: none;
    width: 460px;
margin-top: 5px;
border-width: 2px medium 2px 2px;
border-style: solid none solid solid;
border-color: rgb(213, 213, 213) -moz-use-text-color rgb(213, 213, 213) rgb(213, 213, 213);
-moz-border-top-colors: none;
-moz-border-right-colors: none;
-moz-border-bottom-colors: none;
-moz-border-left-colors: none;
border-image: none;
background: none repeat scroll 0% 0% white;
height: 25px;
border-radius: 2px 0px 0px 2px;
padding: 5px 10px;
border: 2px solid rgb(213, 213, 213);
margin-left: 0;
position: absolute;
  }
  #searchSubmit {
    overflow: visible;
position: absolute;
float: right;
outline:none;
cursor: pointer;
height: 39px;
width: 52px;
font: bold 15px/40px 'lucida sans','trebuchet MS','Tahoma';
color: rgb(255, 255, 255);
margin-top: 5px;
margin-left: 480px;
background: url("http://harvix.com/search.png") no-repeat scroll center center rgb(236, 240, 241);
border: 2px solid rgb(213, 213, 213);
border-radius: 0px 2px 2px 0px;
  }
  #nav-bar-top h1 {
    font-family: Lato,sans-serif;
font-size: 30px;
font-weight: 300;
color: rgb(238, 55, 41);
position: absolute;
margin-left: 30px;
margin-top: 10px;
  }

    </style>

    <!-- Harvix Fav and Touch Icons / Mobile Icons -->
  

	<link rel="apple-touch-icon-precomposed" sizes="144x144" href="http://www.harvix.com/images/harvixshort2.jpg">
    <link rel="apple-touch-icon-precomposed" sizes="114x114" href="http://www.harvix.com/images/harvixshort2.jpg">
      <link rel="apple-touch-icon-precomposed" sizes="72x72" href="http://www.harvix.com/images/harvixshort2.jpg">
                    <link rel="apple-touch-icon-precomposed" href="http://www.harvix.com/images/harvixshort2.jpg">
                                   <link rel="shortcut icon" href="http://www.harvix.com/images/harvixshort2.jpg">

<style>

a:link {color:white; text-decoration: none;}      /* unvisited link */
a:visited {color:white; text-decoration: none;}  /* visited link */
a:hover {color:white; text-decoration: none;}  /* mouse over link */
a:active {color:white; text-decoration: none;}  /* selected link */

</style>

<!-- Harvix Google Analytics JavaScript -->

<script type="text/javascript">

  var _gaq = _gaq || [];
  _gaq.push(['_setAccount', 'UA-30447587-1']);
  _gaq.push(['_trackPageview']);

  (function() {
    var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
    ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
    var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
  })();

</script>



<script type="text/javascript">

  var _gaq = _gaq || [];
  _gaq.push(['_setAccount', 'UA-30658262-1']);
  _gaq.push(['_trackPageview']);

  (function() {
    var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
    ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
    var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
  })();

</script>


</head>

  <body>

<div id='nav-bar-top'>
  <a href="http://harvix.com"><h1><b>Harvix</b></h1></a>
  <form id="searchForm" class="form-wrapper cf" onsubmit="submitted('h'); return false" action="http://harvix.com/search/stest.cgi" name="searchForm">
    <input id="searchBox" class="ac_input" value="$query" type="text" onwebkitspeechchange="this.form.submit();" speech="" x-webkit-speech="" required="" name="q" spellcheck="false" autocomplete="off" autofocus="autofocus"></input>
    <button type="submit" id='searchSubmit'></button>
    </form>
  </div>

    <div class="container-narrow">



      <!-- START SEARCH PAGE -->


EOF
;
}

sub print_footer
{
print <<EOX

      <!-- END SEARCH PAGE -->

    </div><!-- /.container -->

<!--Javascript-->
        <script src="http://harvix.com/search/js/jquery.js"></script>
        <script src="http://harvix.com/search/js/flexslider.js"></script>
        <script src="http://harvix.com/search/js/fitvids.js"></script>
        <script src="http://harvix.com/search/js/smoothscroll.js"></script>
        <script src="http://harvix.com/search/js/backstretch.js" type="text/javascript"></script>
        <script src="http://harvix.com/search/js/bootstrap.js"></script>
        <script src="http://harvix.com/search/js/script.js" type="text/javascript"></script>
	<script>menu(); backstretch(); slider(); contentslider(); panels(); blogposts();</script>

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


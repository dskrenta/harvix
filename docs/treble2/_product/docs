#!/usr/bin/perl

# this code written by David Skrenta CEO of Harvix Search May 2013 (C) comments vary throughout the file
# call specilized perl modules

use strict;
use JSON;
use URI::Fetch;
use Encode;

my %escapes;
setup_escapes();

print "Content-type: text/html\n\n";


my $query = parse_query();

print_header($query);

my @resultsnew;


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

# CALL IZIK API

my $json_page = URI::Fetch->fetch("http://blekko.com/api/p1?q=$query&auth=c31c6fd0&add_slashtags=homework-help");
my $json_text = $json_page->content();
my $json = decode_json( $json_text );

# print Dumper($json), "\n";

if ( ! defined $json )
{
    print "no results\n";
    exit(0);
}

if ( ! defined $json->{tags} )
{
    print "no tags\n";
    exit(0);
}


# tags go into categories 


foreach my $tag ( @{ $json->{tags} } )
{
    my $category = $tag->{name};
    my $results = $tag->{results};

# print categories 

	if($category ne "WIKI")
        {
        	                                my $wikihtml = qq{

                                 <!-- TREBLE STYLESHEETS -->
    <!-- <link rel="stylesheet/less" href="assets/style/bootstrap.less" media="all" /> -->
    <link rel="stylesheet" href="assets/style/bootstrap2.css" type="text/css" />
    
    <!-- GOOGLE WEB FONTS -->
    <link href='http://fonts.googleapis.com/css?family=Open+Sans:300italic,400italic,600italic,700italic,800italic,400,700,600,300,800' rel='stylesheet' type='text/css'>
</head>
<body>
    <!-- NAVIGATION -->
    <nav class="fixed-top" id="navigation">
        <div class="container">
            <div class="row-fluid">
                <div class="span12 center">
                    <!-- LOGO -->
                    <a class="brand pull-left" href="./">
                        <img src="assets/images/logo.png" alt="Treble">
                    </a>
                    <!-- END LOGO -->

                    <!-- MOBILE MENU BUTTON -->
                    <div class="mobile-menu" data-toggle="collapse" data-target=".nav-collapse">
                        <span class="icon-bar"></span>
                        <span class="icon-bar"></span>
                        <span class="icon-bar"></span>
                    </div>
                    <!-- END MOBILE MENU BUTTON -->

                    <!-- MAIN MENU -->
                    <ul id="main-menu" class="nav-collapse collapse">
                        <li><a href="#page-welcome">Home</a></li>
                        <li><a href="#page-work">Work</a></li>
                        <li><a href="#page-features">Features</a></li>
                        <li><a href="#page-about">About</a></li>
                        <li><a href="#page-blog">Blog</a></li>
                        <li><a href="#page-contact">Contact</a></li>
                    </ul>
                    <!-- END MAIN MENU -->

                    <!-- SOCIAL ICONS -->
                    <div class="social-icons hover-big pull-right">
                        <a href="#" class="sicon-facebook"><i>Facebook</i></a>
                        <a href="#" class="sicon-twitter"><i>Twitter</i></a>
                        <a href="#" class="sicon-linkedin"><i>LinkedIn</i></a>
                        <a href="#" class="sicon-youtube"><i>Youtube</i></a>
                        <a href="#" class="sicon-pinterest"><i>Pinterest</i></a>
                    </div>
                    <!-- END SOCIAL ICONS -->
                </div>
            </div>
        </div>
    </nav>
    <!-- END NAVIGATION -->

                                };
                                print $wikihtml;
	}

	elsif($category eq "ORIG")
	{
	#my $num = scalar @{ $results };
    	#print "<div id=\"count\"><span class=\"label\"><h5>$num results:</h5></span></div> <div id=\"upper\"><span class=\"label label-important\"><h5>Top Results:</h5></span></div><hr></hr>";
	}

	elsif($category eq "WIKI")
        {

	}

	elsif($category eq "NAV")
	{

	}
	
	elsif($category eq "STOCK")
        {
	}

        elsif($category eq "FANDANGO")
        {
	#print "<div id=\"upper\"><span class=\"label label-important\"><h5>Movies:</h5></span></div><hr></hr>";
        }

	elsif($category eq "IMAGE")
	{
	}

	elsif($category eq "date")
	{
	#my $num = scalar @{ $results };
        #print "<div id=\"count\"><span class=\"label\"><h5>$num results:</h5></span></div> <div id=\"upper\"><span class=\"label label-info\"><h5>Latest:</h5></span></div><hr></hr>";
	}
	
	elsif($category eq "PEOPLE")
        {
        #my $num = scalar @{ $results };
        #print "<div id=\"count\"><span class=\"label\"><h5>$num results:</h5></span></div> <div id=\"upper\"><span class=\"label label-info\"><h5>social:</h5></span></div><hr></hr>";
        }

	elsif($category eq "RETAIL")
	{

	}

	else
	{
	#my $num = scalar @{ $results };
        #print "<div id=\"count\"><span class=\"label\"><h5>$num results:</h5></span></div> <div id=\"upper\"><span class=\"label label-info\"><h5>$category:</h5></span></div><hr></hr>";
	}

#	if($category eq "IMAGE")	
#	{
		#print"<div id=\"frame1\"></div>";
		#print"<p>";
		#print"<div id=\"frame2\"></div>";
#	}

# print results inside categories 

	if($category eq "NAV")
	{

	}	

	elsif($category eq "RETAIL")
	{

	}

	elsif($category eq "WIKI")
	{
		my $wiki_count = 1;

        	foreach my $result ( @{ $results } )
        	{
                	if($wiki_count == "1")
			{
				my $title = $result->{'t'};
				my $url = $result->{'u'};
				my $rurl = $result->{'du'};
				my $snippet = $result->{'ws'};
				my $img = $result->{'wi'};
	

				print"
				
				 <style>
    				#page-welcome{width:100%;height:100%;position:relative;overflow:hidden;text-align:center;background:#292929 url($img) 50% 0 repeat fixed;-webkit-background-size:cover;-moz-background-size:cover;-o-background-size:cover;background-size:cover}</style>

				<style>#page-twitter{position:relative;background:url(../images/pages/twitter/tw_bck.jpg) 50% 0 no-repeat fixed;padding-top:90px;padding-bottom:130px}</style>
			
				";

				my $html = qq{

				 <!-- TREBLE STYLESHEETS -->
    <!-- <link rel="stylesheet/less" href="assets/style/bootstrap.less" media="all" /> -->
    <link rel="stylesheet" href="assets/style/bootstrap2.css" type="text/css" />
    
    <!-- GOOGLE WEB FONTS -->
    <link href='http://fonts.googleapis.com/css?family=Open+Sans:300italic,400italic,600italic,700italic,800italic,400,700,600,300,800' rel='stylesheet' type='text/css'>
</head>
<body>
    <!-- NAVIGATION -->
    <nav class="fixed-top" id="navigation">
        <div class="container">
            <div class="row-fluid">
                <div class="span12 center">
                    <!-- LOGO -->
                    <a class="brand pull-left" href="./">
                        <img src="assets/images/logo.png" alt="Treble">
                    </a>
                    <!-- END LOGO -->

                    <!-- MOBILE MENU BUTTON -->
                    <div class="mobile-menu" data-toggle="collapse" data-target=".nav-collapse">
                        <span class="icon-bar"></span>
                        <span class="icon-bar"></span>
                        <span class="icon-bar"></span>
                    </div>
                    <!-- END MOBILE MENU BUTTON -->
                    
                    <!-- MAIN MENU -->
                    <ul id="main-menu" class="nav-collapse collapse">
                        <li><a href="#page-welcome">Home</a></li>
                        <li><a href="#page-work">Work</a></li>
                        <li><a href="#page-features">Features</a></li>
                        <li><a href="#page-about">About</a></li>
                        <li><a href="#page-blog">Blog</a></li>
                        <li><a href="#page-contact">Contact</a></li>
                    </ul>
                    <!-- END MAIN MENU -->
                    
                    <!-- SOCIAL ICONS -->
                    <div class="social-icons hover-big pull-right">
                        <a href="#" class="sicon-facebook"><i>Facebook</i></a>
                        <a href="#" class="sicon-twitter"><i>Twitter</i></a>
                        <a href="#" class="sicon-linkedin"><i>LinkedIn</i></a>
                        <a href="#" class="sicon-youtube"><i>Youtube</i></a>
                        <a href="#" class="sicon-pinterest"><i>Pinterest</i></a>
                    </div>
                    <!-- END SOCIAL ICONS -->
                </div>
            </div>
        </div>
    </nav>
    <!-- END NAVIGATION -->

				};
				print $html;	
			

	
				print"		
		
				<!-- PAGE | WELCOME -->
			 	<div class=\"pages white paralax\" id=\"page-welcome\">
				<div class=\"overlay\"></div>
				<!-- Centralized content -->
				<div class=\"centralized\">
		    		<div class=\"container\">
				<div class=\"row-fluid\">
			    	<div class=\"span12 center\">
				<!-- Animated logo -->
				<div class=\"logo\">
				<div class=\"scrollNormal\">
			 	<a href=\"#page-work\">	
				<img src=\"http://www.harvix.com/images/harvixshort2.jpg\" width=\"140\" height=\"140\" alt=\"Treble\">
				</a>
				</div>
				<div class=\"scrollDown\">
				<a href=\"#page-work\">
				<img src=\"assets/images/pages/welcome/logo2_welcome.png\" width=\"140\" height=\"140\" alt=\"Treble\">
				</a>
				</div> 
				</div>
				<div class=\"line-divider\" id=\"welcome-messages\">
				<ul class=\"slides\">
				<li>
				<h2>$title</h2>
				</li>
				</ul>
				</div>
				<p>$snippet<br></br>$rurl</p>
				</div>
               			</div>
            			</div>
        			</div>
    				</div>

				";

			}

			else 
			{

			}
		
			$wiki_count ++;
		}

	}


	elsif($category eq "STOCK")
	{
	}

	elsif($category eq "FANDANGO")
	{
#		print"<div class=\"panel panel-danger\"><div class=\"panel-heading\"><h3 class=\"panel-title\">MOVIES</h3></div><div class=\"panel-body\">";	
#	
#		foreach my $result ( @{ $results } )
#                {
#			my $fandango = $result->{'fandango'};
#			my $movie = $fandango->{'movie'};
#			my $snippet = $movie->{'snippet'};
#			my $poster = $movie->{'poster'};
#			my $title = $movie->{'title'};
#			my $rating = $movie->{'rating'};
#			my $release_date = $movie->{'release_date'};
#			my $runtime = $movie->{'runtime'};
#			my $trailer_url = $movie->{'trailer_url'};
#			my $fan_url = $movie->{'url'};
#			print"<div class=\"hero-unit-wiki\">";
#			print"<table cellpadding=\"10\"><tr><td>";
#                        print"<a href=\"#myModalwiki\" data-toggle=\"modal\"><img src=\"$poster\"/ class=\"img-rounded\"></a></td><td>";
#                        print"<a href=\"#myModalwiki\" data-toggle=\"modal\"><h3><span style=\"black\">$title</span></h3></a>";
#                        print"Rating: $rating<br>";
#			print"Released: $release_date<br>";
#			print"Runtime: $runtime minutes<br>";
#			print"$snippet<br>";
#			print"<a href=\"$trailer_url\"><span style=\"color:#195189;\">Watch Trailer</span></a> &middot; <a href=\"$fan_url\"><span style=\"color:#195189;\">Get Tickets & Showtimes</span></a>";
#                        print"<p></td></tr></table>";
#			print"</div>";
#		}
#		print"</div></div>";
	}	

	
	elsif($category eq "ORIG")
	{

	my $searchhtml = qq{

    <!-- PAGE | BLOG -->
    <div class="pages" id="page-blog">
        <div class="container">
            <!-- Header -->
            <header>
                <h4 class="line-divider">Top Results</h4>
                
		<!-- Sub menu -->
                <nav class="submenu">
                    <ul id="myTab" class="nav nav-tabs">
                        <li>
                            <a href="#web" class="active" data-toggle="tab">Web Results</a>
                        </li>
                        <li>
                             <a href="#facts" data-toggle="tab">Facts</a>
                        </li>
			<li>
                             <a href="#information" data-toggle="tab">Information</a>
                        </li>
                    </ul>
                </nav>
            </header>
            <!-- End Header -->
	           
		<div id="myTabContent" class="tab-content">
                <div class="tab-pane fade in active" id="web">
            
	    <!-- Article -->
            <article>
                <!-- Blog articles -->
                <ul class="thumbnails">


	};

	print $searchhtml;	


	foreach my $result ( @{ $results } )
        {
	         my $title = $result->{'t'};
                 my $url = $result->{'u'};
                 my $rurl = $result->{'du'};
                 my $snippet = $result->{'s'};
                 $snippet =~ s/<\/?(b|strong)>//g;
                 if ( length($snippet) > 150 )
                 {
                 	$snippet = substr($snippet, 0, 150);
                        $snippet =~ s/\s[^\s]*$//;
                        $snippet .= ' ...';
                 }

			print"<li class=\"span4\">";
                        print"<h5>$title</h5>";
                        print"<p class=\"smallFontBy08\">$snippet</p>";
			print"<div class=\"read-more\"><a href=\"$url\">Read More...</a></div>";
                        print"</li>";
	}

	print"
	</div>
	<div class=\"tab-pane\" id=\"facts\" data-src=\"http://harvix.com\">
	<iframe></iframe>
	</div>
	</div>
	";

	my $searchend = qq{

                </ul>
            </article>
            <!-- End Article -->
        </div>
    </div>
    <!-- END PAGE | BLOG -->

	};

	print $searchend;

	}


	elsif($category eq "IMAGE")
	{

		my $imagehead = qq{
    <!-- PAGE | WORK -->
    <div class="pages" id="page-work">
        <div class="container">
            <!-- Header -->
            <header>
                <h4 class="line-divider">Images</h4>
            </header>
            <!-- End Header -->
            <article>
		<ul class="thumbnails plugin-filter-elements portfolio-items">
		};

		print $imagehead;

	        foreach my $result ( @{ $results } )
                {
                      	print"<li class=\"span4 mix illustration branding\">";
			my $url = $result->{'u'};
                        print"<img src=\"$url\" height=\"295px\"/>";
			print"</li>";
                }
		
		print"</ul></article>";
	}

	else
	{

	my $searchelse = qq{

	<!-- PAGE | BLOG -->
        <div class="pages" id="page-blog">
        <div class="container">
        <!-- Header -->
        <header>
        <h4 class="line-divider">$category</h4>
  	</header>
        <!-- End Header --> 
        <!-- Article -->
        <article>
        <!-- Blog articles -->
        <ul class="thumbnails">
	
	};

	print $searchelse;
	
	foreach my $result ( @{ $results } )
    	{
        
		 my $title = $result->{'t'};
                 my $url = $result->{'u'};
                 my $rurl = $result->{'du'};
                 my $snippet = $result->{'s'};
                 $snippet =~ s/<\/?(b|strong)>//g;
                 if ( length($snippet) > 150 )
                 {
                        $snippet = substr($snippet, 0, 150);
                        $snippet =~ s/\s[^\s]*$//;
                        $snippet .= ' ...';
                 }

                        print"<li class=\"span4\">";
                        print"<h5>$title</h5>";
                        print"<p class=\"smallFontBy08\">$snippet</p>";
                        print"<div class=\"read-more\"><a href=\"$url\">Read More...</a></div>";
                        print"</li>";
	
	}

	print"</ul></article></div></div>";	
	
	}

}

# print footer HTML


print_footer();


# define subroutines 

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
    <!-- META DATA -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=0, minimum-scale=1.0, maximum-scale=1.0">
    <meta name="apple-mobile-web-app-capable" content="yes">
    <meta name="apple-mobile-web-app-status-bar-style" content="black">
    
    <meta name="description" content="Treble theme">
    <title>Treble</title>

    <link rel="apple-touch-icon-precomposed" sizes="144x144" href="assets/images/ico/apple-touch-icon-144-precomposed.png">
    <link rel="apple-touch-icon-precomposed" sizes="114x114" href="assets/images/ico/apple-touch-icon-114-precomposed.png">
      <link rel="apple-touch-icon-precomposed" sizes="72x72" href="assets/images/ico/apple-touch-icon-72-precomposed.png">
                    <link rel="apple-touch-icon-precomposed" href="assets/images/ico/apple-touch-icon-57-precomposed.png">
                                   <link rel="shortcut icon" href="assets/images/ico/favicon.png">


EOF
;
}

sub print_footer
{
print <<EOF

    <!-- LOAD JS FILES -->

    <script>
    $('#myTabs').bind('show', function(e) {  
    paneID = $(e.target).attr('href');
    src = $(paneID).attr('data-src');
    // if the iframe hasn't already been loaded once
    if($(paneID+" iframe").attr("src")=="")
    {
        $(paneID+" iframe").attr("src",src);
    }
    });
    </script>

    
    <!-- Jquery -->
    <script src="assets/js/jquery-1.10.2.min.js" type="text/javascript"></script>
    
    <!-- Less and Twitter Bootstrap -->
    <!-- <script src="assets/js/less-1.3.3.min.js" type="text/javascript"></script> -->
    <script src="assets/js/bootstrap.min.js" type="text/javascript"></script>
    
    <!-- Plugins -->
    <script src="assets/js/plugins/jquery.mixitup.min.js" type="text/javascript"></script>
    <script src="assets/js/plugins/jquery.parallax-1.1.3.js" type="text/javascript"></script>
    <script src="assets/js/plugins/jquery.tweet.min.js" type="text/javascript"></script>
    <script src="assets/js/plugins/jquery.bxslider.min.js" type="text/javascript"></script>
    <script src="assets/js/plugins/jquery.responsivevideos.js" type="text/javascript"></script>
    <script src="assets/js/plugins/jquery.centralized.js" type="text/javascript"></script>
    <script src="assets/js/plugins/jquery.hashloader.js" type="text/javascript"></script>
    <script src="assets/js/plugins/jquery.fixedonlater.js" type="text/javascript"></script>
    <script src="assets/js/plugins/jquery.nav.js" type="text/javascript"></script>
    <script src="assets/js/plugins/jquery.scrollTo.js" type="text/javascript"></script>
        
    
    <!-- Treble scripts and plugin initialisation -->
    <script src="assets/js/application.js" type="text/javascript"></script>
    
    <!-- HTML5 shim, for IE6-8 support of HTML5 elements -->
    <!--[if lt IE 9]>
      <script src="assets/js/html5shiv.js"></script>
    <![endif]-->
    
</body>
</html>


EOF
;
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


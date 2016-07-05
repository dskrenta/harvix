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
					<div class="media box-generic">
					<img class="media-object pull-left thumb" height="200px" src="$img" alt="$title" />
					<div class="media-body">
					<h4 class="media-heading">$title</h4>
					<p>$snippet</p>
					</div>
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
        	#Display Facts and Wolfram Aplha Boxes
		my $factswolfhtml = qq{
			<div style=\"background: #ffffff url(http://www.domaine-saint-pierre.fr/skin/frontend/default/default/images/home/loading.gif) no-repeat 50% 5%;\">
			<iframe src="http://harvix.com/wolf.cgi?$query" allowTransparency="true"  width="632px" height="300px" frameborder="0"></iframe>
		};
		#print $factswolfhtml;

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
			
			if ($count == 0)
			{
				if ( $img_data ne '' )
                                {
                                        my $ifhtml = qq{
						<!--Timeline Start-->
                                        	<div class="widget widget-inverse">
						<div class="widget-body padding-none">		
						<div class="relativeWrap overflow-hidden">
						<div class="row row-merge layout-timeline layout-timeline-mirror">
						<div class="col-md-6"></div>
						<div class="col-md-6">
						<div class="innerAll">
						<ul class="timeline">
						<!--Web Result Start-->
						<li class="active">
						<div class="separator bottom">
						<span class="date box-generic">Now</span>
						<span class="type glyphicons suitcase">Website <i></i></span>
						</div>
						<div class="widget widget-heading-simple widget-body-white margin-none">
						<div class="widget-body">
							<h3>$title</h1>
							<p></p>
							<p>$snippet</p>
							<p><span style="color:green">$rurl</span></p>
						</div>
						</div>
						</li>
						<!--Web Result End-->
						<!--Fact Start-->
						<li class="active">
						<span class="type glyphicons comments">Fact <i></i></span>
						<div class="widget widget-heading-simple widget-body-white margin-none">
						<div class="widget-body">
							<p><i class="fa fa-quote-right fa-4x pull-right fa-muted"></i> Jobs was among the first to see the commercial potential of Xerox PARC's mouse-driven graphical user interface, which led to the creation of the Apple Lisa and, a year later, the Macintosh.</p>
							<p><span style="color:green">Url</span></p>
						</div>
						</div>
						</li>
						<!--Fact End-->
					};
                                        print $ifhtml;
                                }

                                else
                                {
					#No Image
                                        my $elsehtml = qq{
                                        };
                                        #print $elsehtml;
                                }
			}
			$count++
        	}
        }

	elsif($category eq "IMAGE")
	{
		#Print Before Alongside HTML		
		my $before = qq{
		};
		#print $before;

		my $img_count = 0;

                foreach my $result ( @{ $results } )
                {
                        #Declare Variable
                        my $url = $result->{'u'};

			if ($img_count == 0)
			{
				#Print Alongside HTML
				my $imagehtml = qq{
					<li class="active">
					<span class="type glyphicons comments">Image <i></i></span>
					<div class="widget widget-heading-simple widget-body-white margin-none">
					<div class="widget-body">
						<img src="$url" alt="$query"></img>
					</div>
					</div>
					</li>
				};
				print $imagehtml;
			}

			else
			{
				#No Extra Images
			}

			$img_count ++;	
                }
		
		#Print After Alongside HTML
		my $after = qq{
		};
		#print $after;
        }
	
        else
        {
		#Display Category Drop Down Box
		my $drophtml = qq{
		};
		print $drophtml;		

		my $rescount = 1;

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
				};
				#print $cathtml;
			}

			else
			{
				#Display Nothing
			}

			$rescount ++;
       		}
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

<!--[if lt IE 7]> <html class="ie lt-ie9 lt-ie8 lt-ie7"> <![endif]-->
<!--[if IE 7]>    <html class="ie lt-ie9 lt-ie8"> <![endif]-->
<!--[if IE 8]>    <html class="ie lt-ie9"> <![endif]-->
<!--[if gt IE 8]> <html> <![endif]-->
<!--[if !IE]><!--><html><!-- <![endif]-->
<head>
	<title>Harvix Plus</title>
	
	<!-- Meta -->
	<meta charset="UTF-8" />
	<meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=0, minimum-scale=1.0, maximum-scale=1.0">
	<meta name="apple-mobile-web-app-capable" content="yes">
	<meta name="apple-mobile-web-app-status-bar-style" content="black">
	<meta http-equiv="X-UA-Compatible" content="IE=9; IE=8; IE=7; IE=EDGE" />
		
	<!--[if lt IE 9]><link rel="stylesheet" href="http://preview.mosaicpro.biz/shared/components/library/bootstrap/css/bootstrap.min.css" /><![endif]-->
	<link rel="stylesheet" href="http://harvix.com/search/new/css/main.css" />
	
	<!-- HTML5 shim and Respond.js IE8 support of HTML5 elements and media queries -->
    <!--[if lt IE 9]>
      <script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>
      <script src="https://oss.maxcdn.com/libs/respond.js/1.3.0/respond.min.js"></script>
    <![endif]-->

	<script src="http://cdn.mosaicpro.biz/shared/components/library/jquery/jquery.min.js?v=v1.2.4-rc1&sv=v0.0.1.1"></script>
<script src="http://cdn.mosaicpro.biz/shared/components/library/jquery/jquery-migrate.min.js?v=v1.2.4-rc1&sv=v0.0.1.1"></script>
<script src="http://cdn.mosaicpro.biz/shared/components/library/modernizr/modernizr.js?v=v1.2.4-rc1&sv=v0.0.1.1"></script>
<script src="http://cdn.mosaicpro.biz/shared/components/plugins/less-js/less.min.js?v=v1.2.4-rc1&sv=v0.0.1.1"></script>
<script src="http://cdn.mosaicpro.biz/shared/components/modules/admin/charts/flot/assets/lib/excanvas.js?v=v1.2.4-rc1&sv=v0.0.1.1"></script>
<script src="http://cdn.mosaicpro.biz/shared/components/plugins/browser/ie/ie.prototype.polyfill.js?v=v1.2.4-rc1&sv=v0.0.1.1"></script>	
</head>
<body class="">

		<div class="navbar navbar-fixed-top navbar-primary main" role="navigation">
    
    <div class="navbar-header pull-left">
        <div class="navbar-brand">
            <div class="pull-left">
                <a href="" class="toggle-button toggle-sidebar btn-navbar"><i class="fa fa-bars"></i></a>
            </div>
            <a href="index.html?lang=en&amp;skin=black-and-white&amp;v=v1.2.4-rc1" class="appbrand innerL">Harvix+</a>
        </div>
    </div>
  
    <ul class="nav navbar-nav navbar-left">
        <li class=" hidden-xs">
            <form class="navbar-form navbar-left " role="search">
                <div class="input-group">
                    <input type="text" class="form-control" placeholder="Search"/>
                    <div class="input-group-btn">
                        <button type="submit" class="btn btn-inverse"><i class="fa fa-search"></i></button>
                    </div>
                </div>
            </form>
        </li>
    </ul>
    <ul class="nav navbar-nav navbar-right hidden-xs">
        <li class="dropdown notification hidden-sm hidden-md">
            <a href="#" class="dropdown-toggle menu-icon" data-toggle="dropdown"><i class="fa fa-fw fa-exclamation-circle"></i></a>
            <ul class="dropdown-menu">
                <li><a href="#">Help</a></li>
                <li><a href="#">About</a></li>
                <li><a href="#">Privacy & Terms</a></li>
                <li><a href="#">Settings</a></li>
            </ul>
        </li>
    </ul>
</div>
	
	<div id="menu" class="hidden-print hidden-xs">
	<div class="sidebar sidebar-inverse">
		<div class="sidebarMenuWrapper">
			<ul class="list-unstyled">
				<li class="active"><a href=""><i class=""></i><span>Everything</span></a></li>
				<li><a href=""><i class=""></i><span>Web</span></a></li>
				<li><a href=""><i class=""></i><span>Images</span></a></li>
				<li><a href=""><i class=""></i><span>Facts</span></a></li>
				<li><a href=""><i class=""></i><span>Information</span></a></li>
				<li><a href=""><i class=""></i><span>Videos</span></a></li>
				<li><a href=""><i class=""></i><span>Categories</span></a></li>
			</ul>
		</div>
	</div>
</div>




	<div id="content"><div class="heading-buttons bg-white border-bottom innerAll">
	<h1 class="content-heading padding-none pull-left">$query</h1>
	<div class="clearfix"></div>
</div>

<div class="innerAll spacing-x2">

<!-- START DYNAMIC CGI -->

EOF
;
}

sub print_footer
{
print <<EOX

<!-- END DYNAMIC CGI -->

</div>
		<!-- // Content END -->
		
		<div class="clearfix"></div>
		<!-- // Sidebar menu & content wrapper END -->
		
		<!-- Footer -->
		<div id="footer" class="hidden-print">
			
			<!--  Copyright Line -->
			<div class="copy">&copy; 2014 Harvix Search</div>
			<!--  End Copyright Line -->
	
		</div>
		<!-- // Footer END -->
		
	</div>
	<!-- // Main Container Fluid END -->
	
	<script src="http://cdn.mosaicpro.biz/shared/components/library/bootstrap/js/bootstrap.min.js?v=v1.2.4-rc1&sv=v0.0.1.1"></script>
<script src="http://cdn.mosaicpro.biz/shared/components/plugins/nicescroll/jquery.nicescroll.min.js?v=v1.2.4-rc1&sv=v0.0.1.1"></script>
<script src="http://cdn.mosaicpro.biz/shared/components/plugins/breakpoints/breakpoints.js?v=v1.2.4-rc1&sv=v0.0.1.1"></script>
<script src="../assets/components/core/js/animations.init.js?v=v1.2.4-rc1"></script>
<script src="http://cdn.mosaicpro.biz/shared/components/common/gallery/blueimp-gallery/assets/lib/js/blueimp-gallery.min.js?v=v1.2.4-rc1&sv=v0.0.1.1"></script>
<script src="http://cdn.mosaicpro.biz/shared/components/common/gallery/blueimp-gallery/assets/lib/js/jquery.blueimp-gallery.min.js?v=v1.2.4-rc1&sv=v0.0.1.1"></script>
<script src="http://cdn.mosaicpro.biz/shared/components/plugins/holder/holder.js?v=v1.2.4-rc1&sv=v0.0.1.1"></script>
<script src="../assets/components/core/js/sidebar.main.init.js?v=v1.2.4-rc1"></script>
<script src="../assets/components/core/js/sidebar.collapse.init.js?v=v1.2.4-rc1"></script>
<script src="http://cdn.mosaicpro.biz/shared/components/helpers/themer/assets/plugins/cookie/jquery.cookie.js?v=v1.2.4-rc1&sv=v0.0.1.1"></script>
<script src="../assets/components/core/js/core.init.js?v=v1.2.4-rc1"></script>	
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


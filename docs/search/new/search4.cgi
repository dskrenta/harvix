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

# foreach my $tag ( @{ $json->{tags} } )

my $elsecount = 1;

foreach my $tag ( sort { $catsort->{ $b->{name} } <=> $catsort->{ $a->{name} } } @{ $json->{tags} } )
{
    	my $category = $tag->{name};
    	my $results = $tag->{results};

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
				my $newwikihtml = qq{
					<!--Start WIKI Timline Section-->
					<li>
         		 		<div class="timeline-badge"><i class="glyphicon glyphicon-info-sign"></i></div>
          				<div class="timeline-panel">
            				<div class="timeline-heading">
              				<h4 class="timeline-title">$title</h4>
            				</div>
            				<div class="timeline-body">
              				<p>$snippet</p>
            				<p><small class="text-muted"><i class="glyphicon glyphicon-ok"></i> $url</small></p>
                                        <!--Like Dislike Flag-->
                                        <p>
                                        <div class="btn-group">
                                        <button type="button" class="btn btn-default"><i class="glyphicon glyphicon-pencil"></i></button>
                                        <button type="button" class="btn btn-default"><i class="glyphicon glyphicon-fullscreen"></i></button>
                                        <button type="button" class="btn btn-default"><i class="glyphicon glyphicon-thumbs-up"></i></button>
                                        <button type="button" class="btn btn-default"><i class="glyphicon glyphicon-thumbs-down"></i></button>
                                        <button type="button" class="btn btn-default"><i class="glyphicon glyphicon-flag"></i></button>
                                        </div>
                                        </p>
                                        <!--End Like Dislike Flag-->
					</div>
          				</div>
        				</li>
					<!--End WIKI Timeline Section-->
				};
				print $newwikihtml;
			}

			else
			{
			}
			
			$wiki_count ++;
		}
	}
		
	elsif($category eq "ORIG")
        {
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
				my $testhtml = qq{	
					<!--Start Web Result-->
					<li class="timeline-inverted">
          				<div class="timeline-badge warning"><i class="glyphicon glyphicon-info-sign"></i></div>
          				<div class="timeline-panel">
            				<div class="timeline-heading">
              				<h4 class="timeline-title">$title</h4>
            				</div>
            				<div class="timeline-body">
            				<p>$snippet</p>
					<p><small class="text-muted"><i class="glyphicon glyphicon-ok"></i> $url</small></p>
					<!--Like Dislike Flag-->
					<p>
					<div class="btn-group">
					<button type="button" class="btn btn-default"><i class="glyphicon glyphicon-pencil"></i></button>
					<button type="button" class="btn btn-default"><i class="glyphicon glyphicon-fullscreen"></i></button>
  					<button type="button" class="btn btn-default"><i class="glyphicon glyphicon-thumbs-up"></i></button>
  					<button type="button" class="btn btn-default"><i class="glyphicon glyphicon-thumbs-down"></i></button>
  					<button type="button" class="btn btn-default"><i class="glyphicon glyphicon-flag"></i></button>
					<button type="button" class="btn btn-primary"><i class="glyphicon glyphicon-fullscreen"></i> WEB</button>
					</div>
					</p>
					<!--End Like Dislike Flag-->
					</div>
          				</div>
        				</li>
					<!--End Web Result-->
					<!--Start Wolf-->
					<li>
                                        <div class="timeline-badge warning"></div>
                                        <div class="timeline-panel">
                                        <div class="timeline-body">
                                        <p><div style=\"background: #ffffff url(http://www.domaine-saint-pierre.fr/skin/frontend/default/default/images/home/loading.gif) no-repeat 50% 5%;\">
                      			<iframe src="http://harvix.com/wolf.cgi?$query" allowTransparency="true"  width="100%" height="300px" frameborder="0"></iframe></p>
                                        </div>
                                        </div>
                                        </li>
					<!--End Wolf-->
					<!--Start Facts-->
					<li class="timeline-inverted">
                                        <div class="timeline-badge warning"></div>
                                        <div class="timeline-panel">
                                        <div class="timeline-heading">
                                        <h4 class="timeline-title">Facts - Update</h4>
                                        </div>
                                        <div class="timeline-body">
                                        <p><iframe src="http://harvix.com/facts4.cgi?$query" width="100%" height="328px" class="restricted" overflow-y="hidden" frameborder="0"></iframe></p>
                                        </div>
                                        </div>
                                        </li>
					<!--End Facts-->
				};
				print $testhtml;
			}
			
			else
			{
				if ($count <= 3)
				{
					
				}
				
				else
				{
					#MODAL
				}
			}
			$count ++
        	}
		my $ORIGhtml = qq{
			<!--Start Wolf-->
                        <li>
                        <div class="timeline-badge warning"></div>
                        <div class="timeline-panel">
                        <div class="timeline-body">
                        <p><div style=\"background: #ffffff url(http://www.domaine-saint-pierre.fr/skin/frontend/default/default/images/home/loading.gif) no-repeat 50% 5%;\">
                        <iframe src="http://harvix.com/wolf.cgi?$query" allowTransparency="true"  width="100%" height="300px" frameborder="0"></iframe></p>
                        </div>
                        </div>
                        </li>
                      	<!--End Wolf-->
                        <!--Start Facts-->
                        <li class="timeline-inverted">
                       	<div class="timeline-badge warning"></div>
                        <div class="timeline-panel">
                        <div class="timeline-heading">
                        <h4 class="timeline-title">Facts - Update</h4>
                        </div>
                        <div class="timeline-body">
                        <p><iframe src="http://harvix.com/facts4.cgi?$query" width="100%" height="328px" class="restricted" overflow-y="hidden" frameborder="0"></iframe></p>
                        </div>
                        </div>
                        </li>
                      	<!--End Facts-->
		};
		print $ORIGhtml;
        }

	elsif($category eq "IMAGE")
	{
                foreach my $result ( @{ $results } )
                {
                        #Declare Variable
                        my $url = $result->{'u'};

			#Print Alongside IMG HTML
			my $imagehtml = qq{
				<li>
          			<div class="timeline-badge danger"></div>
          			<div class="timeline-panel">
            			<div class="timeline-heading">
              			<h4 class="timeline-title">Mussum ipsum cacilds</h4>
            			</div>
            			<div class="timeline-body">
				<img src="$url" width="200px"  alt=""></img>
            			</div>
          			</div>
       				</li>
			};
			#print $imagehtml;	
                }
        }
	
        else
        {
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
				#Print One Result Box
				if ($elsecount%2)
				{
					my $printone = qq{
						<li>
                                        	<div class="timeline-badge danger"><i class="glyphicon glyphicon-credit-card"></i></div>
                                        	<div class="timeline-panel">
                                        	<div class="timeline-heading">
                                        	<h4 class="timeline-title">$title</h4>
                                        	</div>
                                        	<div class="timeline-body">
                                        	<p>$snippet</p>
                                        	<p><small class="text-muted"><i class="glyphicon glyphicon-ok"></i> $url</small></p>
                                        	<!--Like Dislike Flag-->
                                        	<p>
                                        	<div class="btn-group">
                                        	<button type="button" class="btn btn-default"><i class="glyphicon glyphicon-pencil"></i></button>
                                        	<button type="button" class="btn btn-default"><i class="glyphicon glyphicon-fullscreen"></i></button>
                                        	<button type="button" class="btn btn-default"><i class="glyphicon glyphicon-thumbs-up"></i></button>
                                        	<button type="button" class="btn btn-default"><i class="glyphicon glyphicon-thumbs-down"></i></button>
                                        	<button type="button" class="btn btn-default"><i class="glyphicon glyphicon-flag"></i></button>
                                        	<button type="button" class="btn btn-primary"><i class="glyphicon glyphicon-fullscreen"></i> $category</button>
                                        	</div>
                                        	</p>
                                        	<!--End Like Dislike Flag-->
						</div>
                                        	</div>
                                        	</li>
					};
					print $printone;
				}
				
				else
				{
					my $printtwo = qq{
						<li class="timeline-inverted">
                                        	<div class="timeline-badge warning"></div>
                                        	<div class="timeline-panel">
                                        	<div class="timeline-heading">
                                        	<h4 class="timeline-title">$title</h4>
                                        	</div>
                                        	<div class="timeline-body">
                                       	 	<p>$snippet</p>
                                        	<p><small class="text-muted"><i class="glyphicon glyphicon-ok"></i> $url</small></p>
                                                <!--Like Dislike Flag-->
                                                <p>
                                                <div class="btn-group">
                                                <button type="button" class="btn btn-default"><i class="glyphicon glyphicon-pencil"></i></button>
                                                <button type="button" class="btn btn-default"><i class="glyphicon glyphicon-fullscreen"></i></button>
                                                <button type="button" class="btn btn-default"><i class="glyphicon glyphicon-thumbs-up"></i></button>
                                                <button type="button" class="btn btn-default"><i class="glyphicon glyphicon-thumbs-down"></i></button>
                                                <button type="button" class="btn btn-default"><i class="glyphicon glyphicon-flag"></i></button>
                                                <button type="button" class="btn btn-primary"><i class="glyphicon glyphicon-fullscreen"></i> $category</button>
                                                </div>
                                                </p>
                                                <!--End Like Dislike Flag-->
						</div>
                                        	</div>
                                        	</li>
					};
					print $printtwo;
				}
			}

			if ($rescount%2) 
			{
    				#Odd
				my $oddhtml = qq{
					<li>
          				<div class="timeline-badge danger"><i class="glyphicon glyphicon-credit-card"></i></div>
          				<div class="timeline-panel">
            				<div class="timeline-heading">
              				<h4 class="timeline-title">$title</h4>
            				</div>
            				<div class="timeline-body">
            				<p>$snippet</p>
					<p><span style="color:red">$category</span></p>
					</div>
          				</div>
       					</li>
				};
				#print $oddhtml;
			}
		
			else 
			{
    				#Even
				my $evenhtml = qq{
					<li class="timeline-inverted">
          				<div class="timeline-badge warning"></div>
          				<div class="timeline-panel">
            				<div class="timeline-heading">
              				<h4 class="timeline-title">$title</h4>
            				</div>
            				<div class="timeline-body">
					<p>$snippet</p>
					<p><span style="color:red">$category</span></p>
					</div>
          				</div>
        				</li>
				};
				#print $evenhtml;
			}	
			$rescount ++;
       		}
		$elsecount ++;
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
    <title>Harvix | $query</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Harvix Search Results for: $query">
    <meta name="author" content="Harvix Search">

    <!-- Harvix Search Page Styles -->
    <link href="http://harvix.com/search/css2/bootstrap.css" rel="stylesheet">
    <link href="http://harvix.com/search/css2/timeline.css" rel="stylesheet">

    <!-- Harvix Fav and Touch Icons / Mobile Icons -->
    <link rel="apple-touch-icon-precomposed" sizes="144x144" href="http://www.harvix.com/images/harvixshort2.jpg">
    <link rel="apple-touch-icon-precomposed" sizes="114x114" href="http://www.harvix.com/images/harvixshort2.jpg">
    <link rel="apple-touch-icon-precomposed" sizes="72x72" href="http://www.harvix.com/images/harvixshort2.jpg">
    <link rel="apple-touch-icon-precomposed" href="http://www.harvix.com/images/harvixshort2.jpg">
    <link rel="shortcut icon" href="http://www.harvix.com/images/harvixshort2.jpg">


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

<div class="container">
    <div class="page-header">
        <h1 id="timeline">$query</h1>
    </div>

<ul class="timeline">

<!-- START DYNAMIC CGI -->


EOF
;
}

sub print_footer
{
print <<EOX

<!-- END DYNAMIC CGI -->

</ul>

</div>

<!--Javascript
        <script src="http://harvix.com/search/js/jquery.js"></script>
        <script src="http://harvix.com/search/js/flexslider.js"></script>
        <script src="http://harvix.com/search/js/fitvids.js"></script>
        <script src="http://harvix.com/search/js/smoothscroll.js"></script>
        <script src="http://harvix.com/search/js/backstretch.js" type="text/javascript"></script>
        <script src="http://harvix.com/search/js/bootstrap.js"></script>
        <script src="http://harvix.com/search/js/script.js" type="text/javascript"></script>
	<script>menu(); backstretch(); slider(); contentslider(); panels(); blogposts();</script>
-->
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


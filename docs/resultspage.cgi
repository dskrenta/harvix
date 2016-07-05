#!/usr/bin/perl

# this code written by David Skrenta CEO of Harvix Search May 2013 (C) comments vary throughout the file
# update by Lorenzo F. Antunes CTO of Harvix Search Jul 2013

# call specilized perl modules

use strict;
use JSON;
use URI::Fetch;
use Data::Dumper;
use WebService::Blekko;
use URI::Fetch;
use Encode;

my %escapes;
setup_escapes();

print "Content-type: text/html\n\n";

my $query = parse_query();
#print "Query: $query \n";

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

=head2 utf8_off($string)

Unconditionally marks a string as not UTF-8. If the string isn't
valid UTF-8, chaos is in your immediate future.

=cut

# CALL IZIK API
#http://www.stands4.com/services/v2/quotes.php?uid=2942&tokenid=XlMcm3XQlTYJNhMU&searchtype=AUTHOR&query=Albert+Einstein

my $json_page = URI::Fetch->fetch("http://blekko.com/api/p1?q=$query&auth=c31c6fd0&add_slashtags=homework-help");
my $json_text = $json_page->content();
my $json = decode_json( $json_text );

# print Dumper($json), "\n";

if ( ! defined $json ) {
    print "no results\n";
    exit(0);
}

if ( ! defined $json->{tags} ) {
    print "no tags\n";
    exit(0);
}

# tags go into categories 
foreach my $tag ( @{ $json->{tags} } ) {
    my $category = $tag->{name};
    my $results = $tag->{results};

	# print categories 
	if ( $category eq "WIKI" ) {
		my $wiki_count = 1;

    	foreach my $result ( @{ $results } ) {
        	if($wiki_count == "1") {
				print"<div class=\"hero-unit-wiki\">";
				print" <ul id=\"myTab\" class=\"nav nav-tabs\">
             			<li class=\"active\"><a href=\"#instant\" data-toggle=\"tab\">Instant Information</a></li>
						<li><a href=\"#expand\" data-toggle=\"tab\">Expand</a></li>
              			<li><a href=\"#notes\" data-toggle=\"tab\">Notes</a></li>
	    			</ul>";
				print"<div id=\"myTabContent\" class=\"tab-content\">
			  			<div class=\"tab-pane fade in active\" id=\"instant\">";

				my $title = $result->{'t'};
        		my $url = $result->{'u'};
        		my $rurl = $result->{'du'};
        		my $snippet = $result->{'ws'};
				my $img = $result->{'wi'};

				print"<table cellpadding=\"10\"><tr><td>";
				print"<a href=\"#\" data-toggle=\"modal\"><img src=\"$img\"/ class=\"img-rounded\"></a></td><td>";
        		print"<h3><span style=\"black\">$title</span></h3>";
				print"$snippet";
        		print"<p><span style=\"color:green\">$rurl</span>";
				print"</td>";
				print"<td><iframe src=\"http://harvix.com/wolf.cgi?$query\" width=\"500px\" height=\"300px\" frameborder=\"0\"></iframe></td>";
                print"</tr></table>";
				print"</div>";
				print"<div class=\"tab-pane fade\" id=\"expand\">";
                print"<iframe src=\"$url\" width=\"100%\" height=\"600px\" frameborder=\"0\"></iframe>";
                print"</div>";
				print"<div class=\"tab-pane fade\" id=\"notes\">";
				print"<iframe src=\"https://draftin.com/draft/users/sign_in\" width=\"100%\" height=\"600px\" frameborder=\"0\"></iframe>";
				print"</div>";
				print"</div></div>";
			}

			else{}
		
			$wiki_count ++;
		}
	} 
	else {
		if( ( $category ne "NAV" ) && ( $category ne "STOCK" ) && ( $category ne "RETAIL" ) ) {
			if($category eq "ORIG") {
				my $num = scalar @{ $results };
		    	print "<div id=\"count\"><span class=\"label\"><h5>$num results:</h5></span></div> <div id=\"upper\"><span class=\"label label-important\"><h5>Top Results:</h5></span></div><hr></hr>";

				print"<div id=\"scrollable\"><div id=\"items\">";
				print"<div class=\"item3\">";
				print"<table><tr><td>Ads - $query</td></tr><tr><td>";
				print"<script type=\"text/javascript\"><!--
					google_ad_client = \"ca-pub-8703503710400894\";
					/* Harvix */
					google_ad_slot = \"1521670567\";
					google_ad_width = 300;
					google_ad_height = 250;
					//-->
					</script>
					<script type=\"text/javascript\"
					src=\"http://pagead2.googlesyndication.com/pagead/show_ads.js\">
					</script></td></tr></table>";	
			
				print"</div>";
			
				foreach my $result ( @{ $results } ) {
		            print"<div class=\"item2\">";
		            print"<div class=\"hero-unit-spec\">";
		            my $title = $result->{'t'};
		            my $url = $result->{'u'};
		            my $rurl = $result->{'du'};
		            my $snippet = $result->{'s'};
		            $snippet =~ s/<\/?(b|strong)>//g;
		            if ( length($snippet) > 150 ) {
		                $snippet = substr($snippet, 0, 150);
		                $snippet =~ s/\s[^\s]*$//;
		                $snippet .= ' ...';
		            }
		            print"<a href=\"$url\"><span style=\"color:#195189;\"><h4>$title</h4></span></a>";
		            print"$snippet";
		            print"<p><span style=\"color:green\">$rurl</span>";
		            print"</div></div>";
		            #print"<hr></hr><p>";
		            #print Dumper($result);
		        }

		        print"</div></div>";

		    	print "<p>\n";

				print "<div id=\"upper\"><span class=\"label label-info\"><h5>Facts:</h5></span></div><hr></hr>";
			
				my $countnew = 0;

				foreach my $resnew ( @resultsnew ) {
			        if ($countnew == 0) {
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

						print"<div id=\"scrollable\"><div id=\"items\">";

						my $btw = 1;

						foreach my $s ( @sentences ) {
							next if $s !~ /(\sis\s|\swas\s|\swrote\s|\she\s)/;
							next if length($s) > 200;
							next if length($s) < 50;
							next if $s =~ /(Wikipedia)/;

							print"<div class=\"itemfacts\">";
			                print"<div class=\"hero-unit-spec\">";
							print "<b>$btw.</b> $s <p> <span class=\"label\">Wikipedia</span><p>";
						    $btw++;

							print"</div></div>";
						}

						print"</div></div>";
						print "<p>\n";

						if ( ! @sentences ) {
							print"$pokemon";
							print "No Facts!" ;
						}

		   			}

					$countnew ++;

				}	    	
			}

		    elsif($category eq "FANDANGO") {
				print "<div id=\"upper\"><span class=\"label label-important\"><h5>Movies:</h5></span></div><hr></hr>";

				foreach my $result ( @{ $results } ) {
				
					my $fandango = $result->{'fandango'};
					my $movie = $fandango->{'movie'};
					my $snippet = $movie->{'snippet'};
					my $poster = $movie->{'poster'};
					my $title = $movie->{'title'};
					my $rating = $movie->{'rating'};
					my $release_date = $movie->{'release_date'};
					my $runtime = $movie->{'runtime'};
					my $trailer_url = $movie->{'trailer_url'};
					my $fan_url = $movie->{'url'};
					print"<div class=\"hero-unit-wiki\">";
					print"<table cellpadding=\"10\"><tr><td>";
		            print"<a href=\"#myModalwiki\" data-toggle=\"modal\"><img src=\"$poster\"/ class=\"img-rounded\"></a></td><td>";
		            print"<a href=\"#myModalwiki\" data-toggle=\"modal\"><h3><span style=\"black\">$title</span></h3></a>";
		            print"Rating: $rating<br>";
					print"Released: $release_date<br>";
					print"Runtime: $runtime minutes<br>";
					print"$snippet<br>";
					print"<a href=\"$trailer_url\"><span style=\"color:#195189;\">Watch Trailer</span></a> &middot; <a href=\"$fan_url\"><span style=\"color:#195189;\">Get Tickets & Showtimes</span></a>";
		            print"<p></td></tr></table>";
					print"</div>";
				}
		    }

			elsif($category eq "IMAGE") {
				my $num = scalar @{ $results };
				print "<div id=\"count\"><span class=\"label\"><h5>$num images:</h5></span></div> <div id=\"upper\"><span class=\"label label-important\"><h5>Images:</h5></span></div><hr></hr>";

				print"<div id=\"scrollable-img\"><div id=\"items\">";

				foreach my $result ( @{ $results } ) {
					print"<div class=\"item\">";
					my $url = $result->{'u'};        
		    		print"<a href=\"$url\"><img src=\"$url\" onerror=\"this.style.display=\'none\'\" height=\"280px\"/></a>";
					print"</div>";
				}
				print"</div></div>";
				print "<p>\n";
			}

			elsif($category eq "date") {
				my $num = scalar @{ $results };
		        print "<div id=\"count\"><span class=\"label\"><h5>$num results:</h5></span></div> <div id=\"upper\"><span class=\"label label-info\"><h5>Latest:</h5></span></div><hr></hr>";
				print"<div id=\"scrollable\"><div id=\"items\">";    

				foreach my $result ( @{ $results } ) {
				print"<div class=\"item2\">";
			    print"<div class=\"hero-unit-spec\">";
				my $title = $result->{'t'};
			    my $url = $result->{'u'};
				my $rurl = $result->{'du'};
			    my $snippet = $result->{'s'};
			    $snippet =~ s/<\/?(b|strong)>//g;
				if ( length($snippet) > 150 ) {
			    	$snippet = substr($snippet, 0, 150);
			    	$snippet =~ s/\s[^\s]*$//;
			    	$snippet .= ' ...';
				}
				print"<a href=\"$url\"><span style=\"color:#195189;\"><h4>$title</h4></span></a>";
				print"$snippet";
			    print"<p><span style=\"color:green\">$rurl</span>";
			    print"</div></div>";
				#print"<hr></hr><p>";
			    #print Dumper($result);
			    }

				print"</div></div>";

				print "<p>\n";	
			}
			
			elsif($category eq "PEOPLE") {
		        my $num = scalar @{ $results };
		        print "<div id=\"count\"><span class=\"label\"><h5>$num results:</h5></span></div> <div id=\"upper\"><span class=\"label label-info\"><h5>social:</h5></span></div><hr></hr>";

				print"<div id=\"scrollable\"><div id=\"items\">";

		        foreach my $result ( @{ $results } ) {
		            print"<div class=\"item2\">";	
		            print"<div class=\"hero-unit-spec\">";
		            my $title = $result->{'t'};
		            my $url = $result->{'u'};
					my $snippet = $result->{'s'};
		            $snippet =~ s/<\/?(b|strong)>//g;
		            if ( length($snippet) > 150 ) {
		                $snippet = substr($snippet, 0, 150);
		                $snippet =~ s/\s[^\s]*$//;
		                $snippet .= ' ...';
		            }
		            print"<a href=\"$url\"><span style=\"color:#195189;\"><h4>$title</h4></span></a>";
		            print"$snippet";
		            print"<p><span style=\"color:green\">$url</span>";
		            print"</div></div>";
		            #print"<hr></hr><p>";
		            #print Dumper($result);
		        }

		        print"</div></div>";
		    	print "<p>\n";	        

		    	#quotes for people
				my $quotesquery = $query;
				$quotesquery =~ s/\s/+/g;

				my $quotes = URI::Fetch->fetch("http://www.stands4.com/services/v2/quotes.php?uid=2942&tokenid=XlMcm3XQlTYJNhMU&searchtype=AUTHOR&query=$quotesquery");
				my $content = $quotes->content;
				$content =~ s/\<results\>//g;
				$content =~ s/\<\/results\>//g;
				$content =~ s/\<result\>\<quote\>//g;
				$content =~ s/\<\/quote\><\author\>//g;
				$content =~ s/\<\/author\><\result\>//g;


				my @array = split(/$query/, $content);
				my @goodarray;
				
				my $conttemp = 1;
				my $contx = 0;

				foreach my $x (@array) {
					if ($conttemp == 1) {
						push(@goodarray, $x);
					} 
					else {
						my $elementok = 1;
						foreach my $y (@goodarray) {
							if ($contx < scalar(@goodarray)) {
								if ($x eq( $y)) {
									$elementok = 0;
									last;
								}
								$contx ++;
							} 
							else {
								last;
							}
							
						}
						if ($elementok == 1) {
							push(@goodarray, $x);
						}
					}	
					$conttemp ++;
				}

				$num = scalar(@goodarray);

				print "<div id=\"count\"><span class=\"label\"><h5>$num results:</h5></span></div> <div id=\"upper\"><span class=\"label label-info\"><h5>Quotes:</h5></span></div><hr></hr>";

				print"<div id=\"scrollable\"><div id=\"items\">";

				foreach my $result ( @goodarray ) {
		            print "<div style='display: block'>";	
		            #print "<div class=\"hero-unit-spec\">";
		           	print "<p>$result</p>";
		           	#print"</div></div>";
		           	print"</div>";
		        }

		        print"</div></div>";
		    	print "<p>\n";	 
		    }

			else {
				my $num = scalar @{ $results };
			    print "<div id=\"count\"><span class=\"label\"><h5>$num results:</h5></span></div> <div id=\"upper\"><span class=\"label label-info\"><h5>$category:</h5></span></div><hr></hr>";

				print"<div id=\"scrollable\"><div id=\"items\">";    

				foreach my $result ( @{ $results } ) {
				print"<div class=\"item2\">";
			    print"<div class=\"hero-unit-spec\">";
				my $title = $result->{'t'};
			    my $url = $result->{'u'};
				my $rurl = $result->{'du'};
			    my $snippet = $result->{'s'};
			    $snippet =~ s/<\/?(b|strong)>//g;
				if ( length($snippet) > 150 ) {
			    	$snippet = substr($snippet, 0, 150);
			    	$snippet =~ s/\s[^\s]*$//;
			    	$snippet .= ' ...';
				}
				print"<a href=\"$url\"><span style=\"color:#195189;\"><h4>$title</h4></span></a>";
				print"$snippet";
			    print"<p><span style=\"color:green\">$rurl</span>";
			    print"</div></div>";
				#print"<hr></hr><p>";
			    #print Dumper($result);
			    }

				print"</div></div>";

				print "<p>\n";	
			}
		}
	}	
}

# print footer HTML
print_footer();

# define subroutines 

sub setup_escapes {
	for (0..255)
	{
	    $escapes{chr($_)} = sprintf("%%%02X", $_);
	}
	$escapes{' '} = '+';
}

sub utf8_on {
    my($str) = @_;

    if($str) {
        String::Charset::utf8_clean( $str );

        Encode::_utf8_on($str);

        if(!Encode::is_utf8($str, 1)) {
            Encode::_utf8_off($str);
        }
    }
    return $str;
}

sub utf8_off {
    my( $str ) = @_;

    if($str) {
        Encode::_utf8_off($str);
    }

    return $str;
}

sub urlencode {
    my $url = shift;

    $url =~ s/([^A-Za-z0-9\-_.!~*\'()])/$escapes{$1}/ge if defined $url;
    return $url;
}

sub urldecode {
    my $url = shift;

    $url =~ tr/+/ / if defined $url;
    $url =~ s/%([0-9A-Fa-f]{2})/chr(hex($1))/eg if defined $url;

    return $url;
}

sub print_header {
	my ( $query ) = @_;

	$query =~ s/[<>\&]//g;

	print <<EOF; 

		<!DOCTYPE html>
		<html lang="en">
		<head>
			<meta charset="utf-8">
			<title>$query - Harvix</title>
			<meta name="viewport" content="width=device-width, initial-scale=1.0">
			<meta name="description" content="">
			<meta name="author" content="">

		    <!-- Le styles -->
	    	<link href="http://harvix.com/bootstrap.css" rel="stylesheet">
	    	<link href="http://localhost/resultpage.css" rel="stylesheet">
			

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
			<div class="navbar navbar-inverse navbar-fixed-top">
				<div class="navbar-inner">
					<div class="container-fluid">
						<a class="brand" href="index.php"><b><span style="color:white">Har<span style="color:red">vix</span></span></b></a>
						<ul class="nav">
							<li>
								<form class="navbar-search pull-left">
								<input type="text" style="width:650px;" action="http://harvix.com/search7.cgi" onsubmit="submitted('h'); return false" name="q"  class="search-query" value="$query">
							</li>
						</ul>	
						<ul class="nav">
							<li>
								<button type="submit" class="btn"><strong>Search</strong></button>
								</form>
							</li>
						</ul>
					</div>
				</div>
			</div>


			<!-- Marketing messaging and featurettes
			================================================== -->
			<!-- Wrap the rest of the page in another container to center all the content. -->

			<div class="container-fluid">



			<!-- START THE FEATURETTES -->
EOF
}

sub print_footer {
	
	print <<EOX;

		<!-- /END THE FEATURETTES -->


		</div><!-- /.container -->

		<!-- Le javascript
	    ================================================== -->
	    <!-- Placed at the end of the document so the pages load faster -->
	    <script src="http://twitter.github.io/bootstrap/2.3.2/assets/js/jquery.js"></script>
	    <script src="http://twitter.github.io/bootstrap/2.3.2/assets/js/bootstrap-transition.js"></script>
	    <script src="http://twitter.github.io/bootstrap/2.3.2/assets/js/bootstrap-modal.js"></script>
	    <script src="http://twitter.github.io/bootstrap/2.3.2/assets/js/bootstrap-dropdown.js"></script>
	    <script src="http://twitter.github.io/bootstrap/2.3.2/assets/js/bootstrap-button.js"></script>
	    <script src="http://twitter.github.io/bootstrap/2.3.2/assets/js/bootstrap-collapse.js"></script>
	    <script src="http://twitter.github.io/bootstrap/2.3.2/assets/js/bootstrap-tab.js"></script>



		</body>
		</html>
EOX
}

#receive the params
sub parse_query {
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

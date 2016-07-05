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

my $instant;
my $topresults;
my $factsquotes;
my $facts;
my $quotestoprint;
my $imagestoprint;

my $catmenustoprint;
$catmenustoprint = $catmenustoprint . '<div id="catmenus"><ul>';

my $stufftoprint;
$stufftoprint = $stufftoprint . '<div id="stuff"><ul>';

my $categoriesflag;
$categoriesflag = 0;

my $nocontent;
$nocontent = 0;

foreach my $tag ( @{ $json->{tags} } ) {
    my $category = uc($tag->{name});
    my $results = $tag->{results};
    #print uc($category) ."\n";

    if ($category eq "WIKI") {
    	$instant = $instant . '<section class="row-fluid" id="instant"><div class="span12">';

    	foreach my $result ( @{ $results } ) {
	    	my $title = $result->{'t'};
			my $url = $result->{'u'};
			my $rurl = $result->{'du'};
			my $snippet = $result->{'ws'};
			my $img = $result->{'wi'};

			$instant = $instant . '<img src="' . $img . '" alt="' . $query . '">';
			$instant = $instant . '<p>' . $snippet . '<a href="' . $url . '">' . $rurl . '</a></p>';
		}

		#$instant += '<p>Title: ' . $title . '</p>';
    	$instant = $instant . '</div></section>';
    	
    } 
    elsif($category eq "ORIG") {
    	$topresults = '<section id="categories">
						<div class="category">
							<div>
								<ul class="result pull-left" id="topresults">
									<h2>TOP RESULTS</h2>	
									<hr>';

    	foreach my $result ( @{ $results } ) {
            #print"<div class=\"item2\">";
            #print"<div class=\"hero-unit-spec\">";
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
            $topresults = $topresults . '<li><a href="' . $url . '" target="_blanck">';
			$topresults = $topresults . '<h3>' . $title . '</h3>';
			$topresults = $topresults . '<p>' . $snippet . '</p>';
			$topresults = $topresults . '<p id="link">' . $rurl . '</p>';
			$topresults = $topresults . '</a><hr></li>';

        }
        $topresults = $topresults . '</ul>';

        $factsquotes = $factsquotes . '<div id="factsquotes">
						<h2 class="active" id="facts">FACTS</h2>
						<h2 class="noactive" id="quotes">QUOTES</h2>
					</div>';

		$facts = $facts . '<ul class="result pull-right" id="facts">
						<li>
							<hr>
						</li>';

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

				my $btw = 1;

				foreach my $s ( @sentences ) {
					next if $s !~ /(\sis\s|\swas\s|\swrote\s|\she\s)/;
					next if length($s) > 200;
					next if length($s) < 50;
					next if $s =~ /(Wikipedia)/;

					#print"<div class=\"itemfacts\">";
	                #print"<div class=\"hero-unit-spec\">";
					#print "<b>$btw.</b> $s <p> <span class=\"label\">Wikipedia</span><p>";

					$facts = $facts . '<li><p>' . $btw .'. ' . $s . '</p>';
					$facts = $facts . '<p id="link">Wikipedia</p><hr></li>';

					#print"</div></div>";

				    $btw++;
				}

				#print"</div></div>";
				#print "<p>\n";

				if ( ! @sentences ) {
					print"$pokemon";
					print "No Facts!" ;
				}

   			}

			$countnew ++;

		}	

		$facts = $facts . '</ul>';
    }
    elsif($category eq "IMAGE"){
    	$imagestoprint = $imagestoprint . '<div id="media">
				<div id="imagesvideos">
					<h2 class="active" id="images">IMAGES</h2>
					<!--<h2 class="noactive" id="videos">VIDEOS</h2>-->
				</div>
				<ul>';

		foreach my $result ( @{ $results } ) {
			my $url = $result->{'u'};

			$imagestoprint = $imagestoprint . '<li><img src="' . $url . '" alt="' . $query . '"></li>';
		}
				
		$imagestoprint = $imagestoprint . '</ul></div>';
    }
    else{
    	if($category eq ''){
    		$nocontent = 1;
    	}
		if(($category ne "NAV" ) && ( $category ne "STOCK" ) && ( $category ne "RETAIL")){
	    	if($category eq "DATE"){
				$catmenustoprint = $catmenustoprint . '<li><span>LATEST</span></li>';    	

				if($categoriesflag == 0){

					$stufftoprint = $stufftoprint . '<li class="active" id="LATEST">
								<h2>LATEST</h2>
								<hr>
								<ul class="pull-left">';
					$categoriesflag = 1;
				}
				else{
					$stufftoprint = $stufftoprint . '<li class="noactive" id="LATEST">
								<h2>LATEST</h2>
								<hr>
								<ul class="pull-left">';
					$categoriesflag = 1;
				}
			}
			else{
				$catmenustoprint = $catmenustoprint . '<li><span>' . $category . '</span></li>';    	
			

				if($categoriesflag == 0){

					$stufftoprint = $stufftoprint . '<li class="active" id="' . $category . '">
								<h2>' . $category . '</h2>
								<hr>
								<ul class="pull-left">';
					$categoriesflag = 1;
				}
				else{
					$stufftoprint = $stufftoprint . '<li class="noactive" id="' . $category . '">
								<h2>' . $category . '</h2>
								<hr>
								<ul class="pull-left">';
					$categoriesflag = 1;
				}
			}
			
			my $numli = scalar( @{ $results });
			#print "NUM LI: " . $numli;
			my $numchange;
			my $cont = 0;

			#num of lis to change to change pull;
			if ($numli%2 == 0) {
				$numchange = $numli/2;
			} else {
				$numchange = (($numli-1)/2)+1;
			}

			foreach my $result ( @{ $results } ) {
				if($cont == $numchange){
					$stufftoprint = $stufftoprint . '</ul><ul class="pull-right">';
					$cont ++;
				}
				if ($cont < $numchange) {
					$cont ++;
				}

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
	            $stufftoprint = $stufftoprint . '<li><a href="' . $url . '" target="_blanck">';
				$stufftoprint = $stufftoprint . '<h3>' . $title . '</h3>';
				$stufftoprint = $stufftoprint . '<p>' . $snippet . '</p>';
				$stufftoprint = $stufftoprint . '<p id="link">' . $rurl . '</p>';
				$stufftoprint = $stufftoprint . '</a><hr></li>';


	        }

	        $stufftoprint = $stufftoprint . '</ul></li>';
		}

    	
    }
}

#if people or not for quotes
my $peopleornot = 0;
foreach my $tag ( @{ $json->{tags} } ) {
    my $category = uc($tag->{name});
    if ($category eq "PEOPLE") {
    	$peopleornot = 1;
	}
}	

#Quotes
$quotestoprint = $quotestoprint . '<ul class="result pull-right" id="quotes">
						<li id="title">
							<hr>
						</li>';

if ($peopleornot == 1) {
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
			if ($elementok = 1) {
				push(@goodarray, $x);
			}
		}	
		$conttemp ++;
	}

	my $num = scalar(@goodarray);

	pop(@goodarray);
	foreach my $result ( @goodarray ) {
       	$quotestoprint = $quotestoprint . '<li><p>&#8220;</p><blockquote>' . ucfirst($result) . '</blockquote><cite>- ' . $query . '</cite><p id="both"></p></li>';
    }

	$quotestoprint = $quotestoprint . '</ul><p></p></div></div>';
} 
else {
	#quotes for things
	my $quotesquery = $query;
	$quotesquery =~ s/\s/+/g;

	my $quotes = URI::Fetch->fetch("http://www.stands4.com/services/v2/quotes.php?uid=2942&tokenid=XlMcm3XQlTYJNhMU&searchtype=SEARCH&query=$quotesquery");
	my $content = $quotes->content;
	#$content =~ s/\<results\>//g;
	#$content =~ s/\<\/results\>//g;
	#$content =~ s/\<result\>\<quote\>//g;
	#$content =~ s/\<\/quote\><\author\>//g;
	#$content =~ s/\<\/author\><\result\>//g;	


	#my @array = split(/$query/, $content);
	my @array = split(/<result\>/, $content);
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
			if ($elementok = 1) {
				push(@goodarray, $x);
			}
		}	
		$conttemp ++;
	}

	my $num = scalar(@goodarray);

	pop(@goodarray);

	my $temp = 0;
	foreach my $result ( @goodarray ) {
		if ($temp == 0) {
			$temp = 1;
			next;
		}
		#$result =~ s/\s//;
		my @thisauthor = split("<author>",$result);
		#$result =~ s/@thisauthor[1]//g;
   		#$quotestoprint = $quotestoprint . '<li><p>&#8220;</p><blockquote>' . ucfirst($result) . '</blockquote><cite>- ' . @thisauthor[1] . '</cite><p id="both"></p></li>';
   		$quotestoprint = $quotestoprint . '<li><p>&#8220;</p><blockquote>' . ucfirst( @thisauthor[0]) . '</blockquote><cite>- ' . @thisauthor[1] . '</cite><p id="both"></p></li>';
    }

	$quotestoprint = $quotestoprint . '</ul><p></p></div></div>';
}

print $instant;
print $topresults;
print $factsquotes;
print $facts;
print $quotestoprint;
print $imagestoprint;

if ($nocontent == 0) {
	
	$catmenustoprint = $catmenustoprint . '</ul></div>';
	print $catmenustoprint;

	$stufftoprint = $stufftoprint . '</ul><p style="clear: both"></p></div>';
	print $stufftoprint;
	print '</section>';
}

print '</article>';
print_footer();




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

			<link rel="stylesheet" href="http://harvix.com/bootstrap.css">
			<link rel="stylesheet" href="http://localhost/sketchresultpage/style.css">

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


		</head>
		<body>
			<header>
				<nav>
					<p>
						Har<span>vix</span>
						<input type="text" autocomplete="off" spellcheck="false" placeholder="What would you like to learn about?" x-webkit-speech onwebkitspeechchange="this..submit();" value="$query">
						<button id="submit">Search</button>
					</p>
				</nav>		
			</header>
			<article>
EOF
}

sub print_footer {
	
	print <<EOX;
			<script src="http://getbootstrap.com/2.3.2/assets/js/jquery.js"></script>
		    <script src="http://getbootstrap.com/2.3.2/assets/js/bootstrap-transition.js"></script>
		    <script src="http://getbootstrap.com/2.3.2/assets/js/bootstrap-modal.js"></script>
		    <script src="http://getbootstrap.com/2.3.2/assets/js/bootstrap-dropdown.js"></script>
		    <script src="http://getbootstrap.com/2.UA-30447587-1.2/assets/js/bootstrap-button.js"></script>
		    <script src="http://getbootstrap.com/2.3.2/assets/js/bootstrap-collapse.js"></script>
		    <script src="http://getbootstrap.com/2.3.2/assets/js/bootstrap-tab.js"></script>
		    <script src="http://localhost/sketchresultpage/main.js"></script>


		</body>
	</html>
EOX
}	

sub parse_query {
    my $query = $ENV{QUERY_STRING} || shift || 1;


    $query =~ s/q=//;
    $query = urldecode($query);
    #$query =~ s/\+/ /g;
    $query =~ s/[\[\]\(\)\.\?]/ /g;
    $query =~ s/^\s*//;
    $query =~ s/\s*$//;

    $query =~ s/([\w']+)/\u\L$1/g; # uppercase each letter

    $query =~ s/\s+/ /g;

    return $query;
}

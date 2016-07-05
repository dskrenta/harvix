#!/usr/bin/perl

use strict;

use Data::Dumper;
#use WebService::Blekko;
use URI::Fetch;
use Encode;
use WebService::Yahoo::BOSS;

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

#####YAHOO API#####

my $ckey = "dj0yJmk9UHowSk13Yzd2bG1DJmQ9WVdrOU0wOXVXRlJzTkhNbWNHbzlNQS0tJnM9Y29uc3VtZXJzZWNyZXQmeD05MA--";
my $csecret = "de55df25ba316c3683395ed0fdacc69565475958";

my $Boss = WebService::Yahoo::BOSS->new( ckey => $ckey, csecret => $csecret );

my $response = $Boss->Web(q => $query, count => 10);

#####END YAHOO API#####

#my $querynew = $query;
#print STDERR "querynew=$querynew\n";

#my $blekkonew = WebService::Blekko->new( auth => 'c31c6fd0', );

#my $resnew = $blekkonew->query( $querynew );

print_header($query);

#my @resultsnew;

#while ( my $rnew = $resnew->next ) {
#        push @resultsnew, {
#                        title => $rnew->title,
#                        snippet => $rnew->snippet,
#                        url => $rnew->url,
#                };
#}

#START OF SEARCH 	

my $countnew = 0;

my $btw = 1;

print"<div id=\"scrollable\"><div id=\"items\">";

#foreach my $result ( @{ $response->results } )
#{
#        if($count == 0 && index($result->{url}, 'wikipedia.org') != -1)
#        {
#                print_wiki($result);
#        }
#        elsif($count == 3)
#        {
#                print_result($result);
#                print_facts();
#                print_wa();
#        }
#        else
#        {
#                print_result($result);
#        }
#
#        $count ++;
#}

#foreach my $resnew ( @resultsnew )
#{
	#if ($countnew <= 10)
	#{

	foreach my $result ( @{ $response->results } )
	{
		my $pokemon = $result->{url};
		
        	my $url = $result->{url};
		my $title = $result->{title};
		my $snippet = $result->{abstract};
	
		#print STDERR "pokemon='$pokemon'\n";

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

		foreach my $s ( @sentences )
		{
     			next if $s !~ /(\sis\s|\swas\s|\swrote\s|\she\s|\sshe\s|\showever\s|\sdevelop\s|\slasted\s|\sas\s|\sa\s|\swhen\s|\sbegan\s|\sconventional\s|\series\s)/;
     			next if length($s) > 200;
     			next if length($s) < 50;
     			next if $s =~ /(\sWikipedia\s|\sI\s|\s"\s|\sthis\s|\sRating\s|\sWhat\s|\sEveryone\s|\sHmm\s|\sboring\s|\syou\s|\sThis\s|\sour\s|\sApple Store\s|\sPalo Alto Networks\s|\sSurveyMonkey\s|Paused|\^|your|FREE|I|my|she's|Leave a comment|Please|please|sorry|Sorry|Sign Up|you|Got a|This website will not display properly unless JavaScript is running.|SunGardASVoice|Comment?)/;
     			#next if $pokemon =~ "http://en.wikipedia.org/wiki/";
     			next if $pokemon =~ "http://makeandtakes.com";

     			print"<div class=\"itemfacts\">";
     			print"<div class=\"hero-unit-spec\">";
     			print"<blockquote>";    
 
     			print "<b>$btw.</b> $s <small><cite title=\"Source Title\">$pokemon</cite></small>";

    			# print"<form action=\"flag.php\" method=\"post\" target=\"_blank\"> <input type=\"hidden\" name=\"url\" value=\"$pokemon\"> <input type=\"hidden\" name=\"sentence\" value=\"$s\"> <input type=\"hidden\" name=\"query\" value=\"$query\"> <button type=\"submit\" class=\"btn btn-small btn btn-info\">Flag Fact</button> </form>";

			my $fact_html =qq{
				<!--Like Dislike Flag-->
                		<p>
                		<div class="btn-group">
                		<a target="_blank" href="http://harvix.com/search/new/notes/notes.html" target="_blank" class="btn btn-default"><i class="glyphicon glyphicon-pencil"></i></a>
                		<a target="_blank" href="$url" target="_blank" class="btn btn-default"><i class="glyphicon glyphicon-fullscreen"></i></a>
                		<a target="_blank" href="http://harvix.com/search/new/cite.cgi?u=$url" target="_blank" class="btn btn-default"><i class="glyphicon glyphicon-pushpin"></i></a>
               			<a target="_blank" href="http://harvix.com/content.php?url=$url&title=$title&snippet=$btw&type=like&query=$query" class="btn btn-default"><i class="glyphicon glyphicon-thumbs-up"></i></a>
                		<a target="_blank" href="http://harvix.com/content.php?url=$url&title=$title&snippet=$btw&type=dislike&query=$query" class="btn btn-default"><i class="glyphicon glyphicon-thumbs-down"></i></a>    
                		<a target="_blank" href="http://harvix.com/content.php?url=$url&title=$title&snippet=$btw&type=flag&query=$query" class="btn btn-default"><i class="glyphicon glyphicon-flag"></i></a>
                		</div>
                		</p>
                		<!--End Like Dislike Flag-->
			};
			print $fact_html;

     			print"</blockquote></div></div>";
     			$btw++;
		}


		if ( ! @sentences )
		{
		}
	#}
	
	#$countnew ++;
}

print"</div></div></div>";

#END OF SEARCH


print_footer();


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



sub print_pod
{
    my ( $pod ) = @_;

    return if !defined $pod->{title};
    return if !defined $pod->{subpods};

print"<h3>";
    print $pod->{title}, ":\n<p>";
print"</h3>";

    foreach my $subpod ( @{ $pod->{subpods} } )
    {
        next if !defined $subpod->{plaintext};
        if ( defined $subpod->{img} )
        {
            print "    ", $subpod->{img}, "<hr></hr>\n<p>";
        }

        #my $s = $subpod->{plaintext};
        #$s =~ s/\n/\n    /gs;
        #print "    ", $s, "\n";
    }
}



sub print_header
{
	my ( $query ) = @_;

	$query =~ s/[<>\&]//g;

print <<EOF



<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>$query | Harvix</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="">
    <meta name="author" content="">

    <!-- Le styles -->
<link href="http://harvix.com/search/css2/bootstrap.css" rel="stylesheet">

    <style type="text/css">
      
a:link {text-decoration:none;}      /* unvisited link */
a:visited {text-decoration:none;}  /* visited link */
a:hover {text-decoration:none;}  /* mouse over link */
a:active {text-decoration:none;}  /* selected link */

	body {
	background-color:white;
      }

	      #scrollable {
       overflow: auto;
       width:100%;
       height:300px; 
    }


   #scrollable-img {
       overflow: auto;
       width:100%;
       height:250px; 
    }


   #items {
     width: 100000000000px; /* itemWidth x itemCount */
    }

  .item{
     float:left;      
  }

  .item2{
        width:400px;
        height:200px;
     float:left;      
  }

 .item3{
        width:350px;
        height:220px;
     float:left;      
  }

.itemfacts{
        width:500px;
        height:250px;
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

#count{
     float:right;      
}

#upper{
text-transform:uppercase;
}


.panel {
  background-color: #ffffff;
  border: 1px solid transparent;
  border-radius: 4px;
  -webkit-box-shadow: 0 1px 1px rgba(0, 0, 0, 0.05);
          box-shadow: 0 1px 1px rgba(0, 0, 0, 0.05);
}

.panel-body {
  padding: 15px;
}

.panel-body:before,
.panel-body:after {
  display: table;
  content: " ";
}

.panel-body:after {
  clear: both;
}

.panel-body:before,
.panel-body:after {
  display: table;
  content: " ";
}

.panel-body:after {
  clear: both;
}

.panel > .list-group {
  margin-bottom: 0;
}

.panel > .list-group .list-group-item {
  border-width: 1px 0;
}

.panel > .list-group .list-group-item:first-child {
  border-top-right-radius: 0;
  border-top-left-radius: 0;
}

.panel > .list-group .list-group-item:last-child {
  border-bottom: 0;
}

.panel-heading + .list-group .list-group-item:first-child {
  border-top-width: 0;
}

.panel > .table {
  margin-bottom: 0;
}

.panel > .panel-body + .table {
  border-top: 1px solid #dddddd;
}

.panel-heading {
  padding: 10px 15px;
  border-bottom: 1px solid transparent;
  border-top-right-radius: 3px;
  border-top-left-radius: 3px;
}

.panel-title {
  margin-top: 0;
  margin-bottom: 0;
  font-size: 16px;
}

.panel-title > a {
  color: inherit;
}

.panel-footer {
  padding: 10px 15px;
  background-color: #f5f5f5;
  border-top: 1px solid #dddddd;
  border-bottom-right-radius: 3px;
  border-bottom-left-radius: 3px;
}

.panel-group .panel {
  margin-bottom: 0;
  overflow: hidden;
  border-radius: 4px;
}

.panel-group .panel + .panel {
  margin-top: 5px;
}

.panel-group .panel-heading {
  border-bottom: 0;
}

.panel-group .panel-heading + .panel-collapse .panel-body {
  border-top: 1px solid #dddddd;
}

.panel-group .panel-footer {
  border-top: 0;
}

.panel-group .panel-footer + .panel-collapse .panel-body {
  border-bottom: 1px solid #dddddd;
}

.panel-default {
  border-color: #dddddd;
}

.panel-default > .panel-heading {
  color: #333333;
  background-color: #f5f5f5;
  border-color: #dddddd;
}

.panel-default > .panel-heading + .panel-collapse .panel-body {
  border-top-color: #dddddd;
}

.panel-default > .panel-footer + .panel-collapse .panel-body {
  border-bottom-color: #dddddd;
}

.panel-primary {
  border-color: #428bca;
}

.panel-primary > .panel-heading {
  color: #ffffff;
  background-color: #428bca;
  border-color: #428bca;
}

.panel-primary > .panel-heading + .panel-collapse .panel-body {
  border-top-color: #428bca;
}

.panel-primary > .panel-footer + .panel-collapse .panel-body {
  border-bottom-color: #428bca;
}

.panel-success {
  border-color: #d6e9c6;
}

.panel-success > .panel-heading {
  color: #468847;
  background-color: #dff0d8;
  border-color: #d6e9c6;
}

.panel-success > .panel-heading + .panel-collapse .panel-body {
  border-top-color: #d6e9c6;
}

.panel-success > .panel-footer + .panel-collapse .panel-body {
  border-bottom-color: #d6e9c6;
}

.panel-warning {
  border-color: #fbeed5;
}

.panel-warning > .panel-heading {
  color: #c09853;
  background-color: #fcf8e3;
  border-color: #fbeed5;
}

.panel-warning > .panel-heading + .panel-collapse .panel-body {
  border-top-color: #fbeed5;
}

.panel-warning > .panel-footer + .panel-collapse .panel-body {
  border-bottom-color: #fbeed5;
}

.panel-danger {
  border-color: #eed3d7;
}

.panel-danger > .panel-heading {
  color: #b94a48;
  background-color: #f2dede;
  border-color: #eed3d7;
}

.panel-danger > .panel-heading + .panel-collapse .panel-body {
  border-top-color: #eed3d7;
}

.panel-danger > .panel-footer + .panel-collapse .panel-body {
  border-bottom-color: #eed3d7;
}

.panel-info {
  border-color: #bce8f1;
}

.panel-info > .panel-heading {
  color: #3a87ad;
  background-color: #d9edf7;
  border-color: #bce8f1;
}

.panel-info > .panel-heading + .panel-collapse .panel-body {
  border-top-color: #bce8f1;
}

.panel-info > .panel-footer + .panel-collapse .panel-body {
  border-bottom-color: #bce8f1;
}
    </style>


   <!-- Fav and touch icons -->
    <link rel="apple-touch-icon-precomposed" sizes="144x144" href="http://www.harvix.com/images/harvixshort2.jpg">
    <link rel="apple-touch-icon-precomposed" sizes="114x114" href="http://www.harvix.com/images/harvixshort2.jpg">
      <link rel="apple-touch-icon-precomposed" sizes="72x72" href="http://www.harvix.com/images/harvixshort2.jpg">
                    <link rel="apple-touch-icon-precomposed" href="http://www.harvix.com/images/harvixshort2.jpg">
                                   <link rel="shortcut icon" href="http://www.harvix.com/images/harvixshort2.jpg">
	</head>

  <body>



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


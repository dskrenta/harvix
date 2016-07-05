#!/usr/bin/perl

#       Harvix Search v. 2.0
#       
#       Coppyright (C) 2013 Harvix Search
#       Designed and Built by David Skrenta CEO, and Bryce DesBrisay CXO 
#       All Contents of File and Related Files Protected by Harvix

use strict;
use JSON;
use URI::Fetch;
use Encode;

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
    print "no tags\n";
    exit(0);
}


#print_header($query);



foreach my $tag ( @{ $json->{tags} } )
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
       		foreach my $result ( @{ $results } )
        	{
			#Declare Variables
                	my $title = $result->{'t'};
                	my $url = $result->{'u'};
                	my $rurl = $result->{'du'};
                	my $snippet = $result->{'ws'};
			my $img = $result->{'wi'};
		
			#Shorten Snippet
                	#$snippet =~ s/<\/?(b|strong)>//g;
                	#if ( length($snippet) > 150 )
                	#{
                       	#	$snippet = substr($snippet, 0, 150);
                       	#	$snippet =~ s/\s[^\s]*$//;
                       	#	$snippet .= ' ...';
                	#}		

			#Print Alongside HTML
			my $wikihtml = qq{
				<div class="row-fluid">
				<!--Main Wiki Box-->
				<div  class="span8 well orange">
				<h3>$title</h3>
				<p>$snippet</p>
				</div>
				<!--Wiki Image Box-->
				<div class="span4">
				<img src="$img" height="300px" width="300px" alt="" />
				</div>
				</div> <!--/row-fluid-->
			};
			print $wikihtml;		
		}
	}

	elsif($category eq "ORIG")
        {
        	#Display Facts and Wolfram Aplha Boxes
		my $factswolfhtml = qq{
                	<div class="row-fluid">
                        <!--Facts Box-->
                        <div class="span4 well blue">
                        <h1 class="text-left">Facts</h1>
                        <p class="text-left">$query</p>
                        </div>
			<!--Wolfram Alpha Box-->
			<div class="span8">
			<div style=\"background: #ffffff url(http://www.domaine-saint-pierre.fr/skin/frontend/default/default/images/home/loading.gif) no-repeat 50% 5%;\">
			<iframe src="http://harvix.com/wolf.cgi?$query" allowTransparency="true"  width="632px" height="300px" frameborder="0"></iframe>
			</div>
			</div>
			</div> <!--/row-fluid-->
		};
		print $factswolfhtml;

		my $count = 0;
		foreach my $result ( @{ $results } )
        	{
			if ($count < 6)
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
	
				#Print Alongside HTML
				my $webhtml = qq{
					<div class="row-fluid">
					<div class="span8 tealblue well">
					<h3>$title</h3>
					<p>$snippet</p>
					</div>
				};
				print $webhtml;
                                $count++;		

				if ( $img_data ne '' )
                		{
					my $ifhtml = qq{
						<div class="span4">
						<img src="$img_data" alt="" width="300px" height="300px" />
						</div>
						</div> <!--/row-fluid-->
					};
					print $ifhtml;
                		}
	
				else
				{
					my $elsehtml = qq{
						</div> <!--/row-fluid-->
					};
					print $elsehtml;
				}
			}
        	}
        }

	elsif($category eq "IMAGE")
	{
		my $count = 1;
                foreach my $result ( @{ $results } )
                {
                        #Declare Variable
                        my $url = $result->{'u'};

			if ($count == 1)
			{
				#Print Alongside HTML
				my $first = qq{
					<div class="row-fluid">
					<div class="span4 no-padding">
					<img src="$url" height="300px" width="300px"  alt="" onerror=\"this.style.display='none' />
					</div>
					</div>
				};
				print $first;
			}

			if ($count%3 == 0)
			{
                        	#Print Alongside HTML
                        	my $second = qq{
                                	</div>
					<div class="span4 no-padding">
					<img src="$url" height="300px" width="300px"  alt="" onerror=\"this.style.display='none' />
                                	</div>
                        	};
				print $second;
			}

			else
			{
				#Print Alongside HTML
				my $third = qq{
					<div class="span4 no-padding">
                                        <img src="$url" height="300px" width="300px"  alt="" onerror=\"this.style.display='none' />
                                        </div>
				};
				print $third;
					
			}

			$count ++;
                }
        }
	
        else
        {

        print"<div class=\"panel panel-primary\"><div class=\"panel-heading\"><h3 class=\"panel-title\"><div id=\"upper\">$category</div></h3></div><div class=\"panel-body\">";

        print"<div id=\"scrollable\"><div id=\"items\">";

        foreach my $result ( @{ $results } )
        {
                print"<div class=\"item2\">";
                print"<div class=\"hero-unit-spec\">";
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
                print"<a href=\"$url\"><span style=\"color:#195189;\"><h4>$title</h4></span></a>";
                print"$snippet";
                print"<p><span style=\"color:green\">$rurl</span>";
                print"</div></div>";
                #print"<hr></hr><p>";
                #print Dumper($result);
        }

        print"</div></div></div></div>";

    print "<p>\n";
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
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>$query - Harvix</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="">
    <meta name="author" content="">

    <!-- Harvix Search Page Styles -->
    <link href="http://harvix.com/search/css/bootstrap.css" rel="stylesheet">
    <link href="http://harvix.com/search/css/bootstrap-responsive.css" rel="stylesheet">	
    <link href="http://harvix.com/search/css/flexslider.css" rel="stylesheet">
    <link href="http://harvix.com/search/css/style.css" rel="stylesheet">

    <style type="text/css">
      body {
	padding-top: 60px;
        padding-bottom: 40px;

      }



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
  height:200px;
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
  margin-bottom: 20px;
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

    <!-- Harvix Fav and Touch Icons / Mobile Icons -->
  

	<link rel="apple-touch-icon-precomposed" sizes="144x144" href="http://www.harvix.com/images/harvixshort2.jpg">
    <link rel="apple-touch-icon-precomposed" sizes="114x114" href="http://www.harvix.com/images/harvixshort2.jpg">
      <link rel="apple-touch-icon-precomposed" sizes="72x72" href="http://www.harvix.com/images/harvixshort2.jpg">
                    <link rel="apple-touch-icon-precomposed" href="http://www.harvix.com/images/harvixshort2.jpg">
                                   <link rel="shortcut icon" href="http://www.harvix.com/images/harvixshort2.jpg">

<style>

a:link {color:#black; text-decoration: none;}      /* unvisited link */
a:visited {color:#black; text-decoration: none;}  /* visited link */
a:hover {color:#black; text-decoration: none;}  /* mouse over link */
a:active {color:#black; text-decoration: none;}  /* selected link */

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

<!--
    <div class="navbar navbar-inverse navbar-fixed-top">
      <div class="navbar-inner">
        <div class="container-fluid">
          <a class="btn btn-navbar" data-toggle="collapse" data-target=".nav-collapse">
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </a>
          <a class="brand" href="index.html"><b><span style="color:white">Har<span style="color:red">vix</span></span></b></a>
          <div class="nav-collapse collapse">
            <ul class="nav">
              <li><form class="navbar-search pull-left">
  <input type="text" style="width:650px;" action="http://harvix.com/msnew3.cgi" onsubmit="submitted('h'); return false" name="q"  class="search-query" value="$query">
</li></ul><ul class="nav"><li>
<button type="submit" class="btn"><strong>Search</strong></button>
</form></li>
</ul>
            </ul>
            </ul>
          </div>
        </div>
      </div>
    </div>

-->

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
        <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.7.1/jquery.min.js"></script>
        <script src="http://a1alfred.com/sharpone/assets/js/jquery.flexslider-min.js"></script>
        <script src="http://a1alfred.com/sharpone/assets/js/jquery.fitvids.js"></script>
        <script src="http://a1alfred.com/sharpone/assets/js/smoothscroll.js"></script>
        <script src="http://a1alfred.com/sharpone/assets/js/jquery.backstretch.min.js" type="text/javascript"></script>
        <script src="http://a1alfred.com/sharpone/assets/js/bootstrap.min.js"></script>
        <script src="http://a1alfred.com/sharpone/assets/js/script.js" type="text/javascript"></script>

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


#!/usr/bin/perl

use strict;

use Data::Dumper;
use WebService::Blekko;
use Encode;

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

my $blekko = WebService::Blekko->new( auth => 'c31c6fd0', );

my $res = $blekko->query( $query );


my $wiki = wiki_query($query);




my @results;

while ( my $r = $res->next ) {
        push @results, {
                        title => $r->title,
                        snippet => $r->snippet,
                        url => $r->url,
                };
}




print_header($query);



	my $search_wiki;
	foreach my $res ( @results )
	{
		if ( $res->{url} =~ m,^http://en.wikipedia.org/wiki/(.*)$, )
		{
			#$t =~ s/\s*-\s*Wikipedia.*$//i;
			#$t =~ s/<[^>]*>//gs;
			#$search_wiki = run_wiki_query($t);
			#last;
		}
	}
	if ( $search_wiki )
	{
	    $wiki = $search_wiki;
	}

#START OF SEARCH 	

if ( $wiki )
        {
            my ( $wiki_best, $wiki_rank, $wiki_fnam, $wiki_title, $wiki_page, $wiki_image, $wiki_url ) = @$wiki;

                utf8_off($wiki_title);
                utf8_off($wiki_page);
                utf8_off($wiki_url);


print"<div class=\"span14\">
          <div class=\"hero-unit-wiki\">";

print"<table cellpadding=\"10\"><tr><td>";
print"<img src=\"$wiki_image\" class=\"img-polaroid\"/>";
print"</td><td>";
print"<h2>$wiki_title</h2>";
print"<p>$wiki_page</p>";
print"<p>$wiki_url</p>";
print"<a href=\"#myModalwiki\" style=\"color:white;\" class=\"btn btn-primary btn-large\" data-toggle=\"modal\">Read More &raquo;</a>";
print" 

  <div id=\"myModalwiki\" class=\"modal hide fade\" tabindex=\"-1\" role=\"dialog\" aria-labelledby=\"myModalLabel\" aria-hidden=\"true\">
  <div class=\"modal-header\">
    <button type=\"button\" class=\"close\" data-dismiss=\"modal\" aria-hidden=\"true\">×</button>
    <h3 id=\"myModalLabel\">$wiki_title</h3>
  </div>
  <div class=\"modal-body\">

<iframe src=\"$wiki_url\" width=\"100%\" height=\"90%\" frameborder=\"0\"></iframe>

  </div>

                  </div>

";

print"<a href=\"#mynotes\" style=\"color:white;\" class=\"btn btn-primary btn-large\" data-toggle=\"modal\">Take Notes &raquo;</a>";
print" 

  <div id=\"mynotes\" class=\"modal hide fade\" tabindex=\"-1\" role=\"dialog\" aria-labelledby=\"myNotesLabel\" aria-hidden=\"true\">
  <div class=\"modal-header\">
    <button type=\"button\" class=\"close\" data-dismiss=\"modal\" aria-hidden=\"true\">×</button>
    <h3 id=\"myNotesLabel\">Notes</h3>
  </div>
  <div class=\"modal-body\">

<iframe src=\"https://draftin.com/draft/users/sign_in\" width=\"100%\" height=\"90%\" frameborder=\"0\"></iframe>

  </div>

                  </div>

";



print"</td></tr></table></div></div>";
}







print"  <div class=\"row-fluid\">
        <div class=\"span6\">
        ";

print"<div class=\"hero-unit\">";

print"   <ul id=\"myTab\" class=\"nav nav-tabs\">
              <li class=\"active\"><a href=\"#web\" data-toggle=\"tab\">Web</a></li>
	 <li><a href=\"#images\" data-toggle=\"tab\">Images</a></li>
	 <li><a href=\"#videos\" data-toggle=\"tab\">Videos</a></li>
        <li><a href=\"#mynotes\" data-toggle=\"modal\">Notes</a></li>    
	</ul>";
print"    <div id=\"myTabContent\" class=\"tab-content\">
              <div class=\"tab-pane fade in active\" id=\"web\">";

print"
<center>
<div style=\"background: #ffffff url(http://www.henley-putnam.edu/Portals/_default/Skins/henley/images/loading.gif) no-repeat 50% 5%;\">
<iframe src=\"http://harvix.com/msweb.cgi?$query\" frameborder=\"0\"  allowTransparency=\"true\" width=\"100%\" height=\"2000px\" scrolling=\"no\"></iframe>
</div>
</center>
";


print"
</div>
";


print"<div class=\"tab-pane fade\" id=\"images\">";

print"
<center>
<div style=\"background: #ffffff url(http://www.henley-putnam.edu/Portals/_default/Skins/henley/images/loading.gif) no-repeat 50% 5%;\">
<iframe src=\"http://harvix.com/images2.cgi?$query\" frameborder=\"0\"  allowTransparency=\"true\" width=\"100%\" height=\"5500px\" scrolling=\"no\"></iframe>
</div>
</center>
";

print"</div>";






print"<div class=\"tab-pane fade\" id=\"videos\">";

print"
<center>
<div style=\"background: #ffffff url(http://www.henley-putnam.edu/Portals/_default/Skins/henley/images/loading.gif) no-repeat 50% 5%;\">
<iframe src=\"http://harvix.com/videos2.cgi?$query\" frameborder=\"0\"  allowTransparency=\"true\" width=\"100%\" height=\"3000px\" scrolling=\"no\"></iframe>
</div>
</center>
";

print"</div>";




print"
</div>
";


    
print"
</div>
</div>
";



print"<div class=\"span6\">";
print"<div class=\"hero-unit\">";
print"   <ul id=\"myTab\" class=\"nav nav-tabs\">
              <li class=\"active\"><a href=\"#facts\" data-toggle=\"tab\">Facts</a></li>
	<li><a href=\"#n\" data-toggle=\"tab\">Information</a></li>
                </ul>
              </li>
            </ul>";
print"    <div id=\"myTabContent\" class=\"tab-content\">
              <div class=\"tab-pane fade in active\" id=\"facts\">";


print"
<center>
<div style=\"background: #ffffff url(http://www.henley-putnam.edu/Portals/_default/Skins/henley/images/loading.gif) no-repeat 50% 5%;\">
<iframe src=\"http://harvix.com/msfacts2.cgi?$query\" frameborder=\"0\"  allowTransparency=\"true\" width=\"100%\" height=\"5000px\" scrolling=\"no\"></iframe>
</div>
</center>
";


print"</div>";

print"<div class=\"tab-pane fade\" id=\"n\">";

print"
<center>
<div style=\"background: #ffffff url(http://www.henley-putnam.edu/Portals/_default/Skins/henley/images/loading.gif) no-repeat 50% 5%;\">
<iframe src=\"http://harvix.com/mswolf.cgi?$query\" frameborder=\"0\"  allowTransparency=\"true\" width=\"100%\" height=\"5000px\" scrolling=\"no\"></iframe>
</div>
</center>
";



print"</div>";

print"</div>";



print"
</div></div><!--/span-->
      </div><!--/row-->";





#END OF SEARCH


print_footer();




sub wiki_query
{
    my ( $query ) = @_;

    my $wiki = run_wiki_query($query);
    my $wiki2;
    if ( $query =~ /^((who|what|where|when|why|how)\s.*)\s[a-z]+$/i )
    {
        my $revised = $1;
        $wiki2 = run_wiki_query($revised);
    }
    if ( $wiki && $wiki2 )
    {
        $wiki = $wiki2 if $wiki2->[0] < $wiki->[0];
    }

    return if ! $wiki;

    return fetch_wikidb( $wiki->[1] );
}

sub fetch_wikidb
{
    my ( $wiki_fnam ) = @_;

    my ( $wiki_rank, $wiki_url, $wiki_title, $wiki_page, $wiki_image );

    open( DB, "</home/david/harvix/wikidb/$wiki_fnam" ) || return;
    my $line = <DB>;
    chomp($line);
    close(DB);
    ( $wiki_rank, $wiki_fnam, $wiki_title, $wiki_page, $wiki_image ) = split( "\t", $line );
    $wiki_url = "http://en.wikipedia.org/wiki/$wiki_fnam";

    return if $wiki_title eq '';

    return [ $wiki->[0], $wiki_rank, $wiki_fnam, $wiki_title, $wiki_page, $wiki_image, $wiki_url ];
}

sub run_wiki_query
{
        my ( $query ) = @_;



        $query =~ s/[\[\]\(\)\.\?,]/ /g;
        $query =~ s/^\s*//;
        $query =~ s/\s*$//;
        $query =~ s/\s+/ /g;

        $query =~ s/^(who|what|where|when|why|how) .*?(is|was|do|did) (the )?//i;

        $query =~ s/^\s*//;
        $query =~ s/\s*$//;

        return if $query eq '';

        my ( $wiki_rank, $wiki_url, $wiki_fnam, $wiki_title, $wiki_page, $wiki_image );

        my @wiki_res;

        open(DB, "</home/david/harvix/wikidb.fast") or warn "can't read wikidb.fast";

        while ( my $line = <DB> )
        {
            chomp($line);

            ( $wiki_fnam, $wiki_title ) = split( "\t", $line );

            if ( !defined $wiki_title || $wiki_title eq '' )
            {
                $wiki_title = urldecode($wiki_fnam);
            }

            $wiki_title =~ s/[_,]/ /g;
            $wiki_title =~ s/\s{2,}/ /g;

            my $fnam_match = $wiki_fnam;
            $fnam_match =~ s/[_,]/ /g;
            $fnam_match =~ s/\s{2,}/ /g;

            my $q2 = $query;
            $q2 =~ s/ /\\b\.\*\\b/g;

            my $text = $wiki_title . ' ' . $fnam_match;

#            next if $text !~ /\b$q2\b/i;

            if ( $wiki_title =~ /^$query$/i || $fnam_match =~ /^$query$/i )
            {
                return [ 1, $wiki_fnam ];
            }
#           elsif ( $wiki_title =~ /\b$query\b/i || $fnam_match =~ /\b$query\b/i )
#           {
#               push @wiki_res, [ 2, $wiki_fnam ];
#           }
#            else
#            {
#                push @wiki_res, [ 3, $wiki_fnam ];
#           }

            ( $wiki_fnam, $wiki_title, $wiki_page, $wiki_image, $wiki_url ) = undef;
        }
        close(DB);

        @wiki_res = sort { $a->[0] <=> $b->[0] or $b->[1] <=> $a->[1] } @wiki_res;

        return if ! scalar @wiki_res;
        return $wiki_res[0];
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
    <link href="bootstrap.css" rel="stylesheet">
    <link href="bootstrap-responsive.css" rel="stylesheet">

    <style type="text/css">
      
a:link {text-decoration:none; color:blue;}      /* unvisited link */
a:visited {text-decoration:none; color:blue;}  /* visited link */
a:hover {text-decoration:none; color:blue;}  /* mouse over link */
a:active {text-decoration:none; color:blue;}  /* selected link */

	body {
        padding-top: 60px;
        padding-bottom: 40px;
	background-color: white;
      }
      .sidebar-nav {
        padding: 9px 0;
      }

	div.hero-unit{overflow:hidden; min-height: 330px;}


    </style>
    <link href="bootstrap-responsive.css" rel="stylesheet">

   <!-- Fav and touch icons -->
    <link rel="apple-touch-icon-precomposed" sizes="144x144" href="http://www.harvix.com/images/harvixshort2.jpg">
    <link rel="apple-touch-icon-precomposed" sizes="114x114" href="http://www.harvix.com/images/harvixshort2.jpg">
      <link rel="apple-touch-icon-precomposed" sizes="72x72" href="http://www.harvix.com/images/harvixshort2.jpg">
                    <link rel="apple-touch-icon-precomposed" href="http://www.harvix.com/images/harvixshort2.jpg">
                                   <link rel="shortcut icon" href="http://www.harvix.com/images/harvixshort2.jpg">
	</head>

  <body>



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
          </div><!--/.nav-collapse -->
        </div>
      </div>
    </div>




  <div id=\"mynotes\" class=\"modal hide fade\" tabindex=\"-1\" role=\"dialog\" aria-labelledby=\"myNotesLabel\" aria-hidden=\"true\">
  <div class=\"modal-header\">
    <button type=\"button\" class=\"close\" data-dismiss=\"modal\" aria-hidden=\"true\">×</button>
    <h3 id=\"myNotesLabel\">Notes</h3>
  </div>
  <div class=\"modal-body\">

<iframe src=\"https://draftin.com/draft/users/sign_in\" width=\"100%\" height=\"90%\" frameborder=\"0\"></iframe>

  </div>

                  </div>





    <div class="container-fluid">


EOF
;
}

sub print_footer
{
print <<EOX






    </div><!--/.fluid-container-->

    <!-- Le javascript
    ================================================== -->
    <!-- Placed at the end of the document so the pages load faster -->
    <script src="http://getbootstrap.com/2.3.2/assets/js/jquery.js"></script>
    <script src="http://getbootstrap.com/2.3.2/assets/js/bootstrap-transition.js"></script>
    <script src="http://getbootstrap.com/2.3.2/assets/js/bootstrap-alert.js"></script>
    <script src="http://getbootstrap.com/2.3.2/assets/js/bootstrap-modal.js"></script>
    <script src="http://getbootstrap.com/2.3.2/assets/js/bootstrap-dropdown.js"></script>
    <script src="http://getbootstrap.com/2.3.2/assets/js/bootstrap-scrollspy.js"></script>
    <script src="http://getbootstrap.com/2.3.2/assets/js/bootstrap-tab.js"></script>
    <script src="http://getbootstrap.com/2.3.2/assets/js/bootstrap-tooltip.js"></script>
    <script src="http://getbootstrap.com/2.3.2/assets/js/bootstrap-popover.js"></script>
    <script src="http://getbootstrap.com/2.3.2/assets/js/bootstrap-button.js"></script>
    <script src="http://getbootstrap.com/2.3.2/assets/js/bootstrap-collapse.js"></script>
    <script src="http://getbootstrap.com/2.3.2/assets/js/bootstrap-carousel.js"></script>
    <script src="http://getbootstrap.com/2.3.2/assets/js/bootstrap-typeahead.js"></script>
    

  </body>
</html>

EOX
;
}


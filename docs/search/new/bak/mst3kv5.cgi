#!/usr/bin/perl

#       Harvix Search Revision
#       
#       Coppyright (C) 2015 Harvix Search
#       Designed and Built by David Skrenta 
#       All Contents of File and Related Files are Protected by Harvix

use strict;
#use JSON;
#use URI::Fetch;
use Encode;
#use Number::Spell;
use WebService::Yahoo::BOSS;
#use Data::Dumper;

use Bing::Search;
use Bing::Search::Source::Web;

my %escapes;
setup_escapes();

my $query = parse_query();

print "Content-type: text/html\n\n";

print_header($query);
print_modal($query);

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

#####YAHOO API#####

#my $ckey = "dj0yJmk9UHowSk13Yzd2bG1DJmQ9WVdrOU0wOXVXRlJzTkhNbWNHbzlNQS0tJnM9Y29uc3VtZXJzZWNyZXQmeD05MA--";
#my $csecret = "de55df25ba316c3683395ed0fdacc69565475958";

#my $Boss = WebService::Yahoo::BOSS->new( ckey => $ckey, csecret => $csecret );

#my $response = $Boss->Web(q => $query, count => 20);



#print $response->totalresults;

#print Dumper($response->results);


#####BING API#####

my $search = Bing::Search->new(
	AppId => 'e1364ac05c3743f8901349f78ae7e21b',
      	Query => $query
);
    
my $source = Bing::Search::Source::Web->new();

$search->add_source( $source );

my $response = $search->search();

#####SEARCH RESULTS#####

print Dumper($response->results);

#my $count = 0;

#foreach my $result ( @{ $response->results } )
#{
#	if($count == 0 && index($result->{url}, 'wikipedia.org') != -1)
#	{
#		print_wiki($result, $query, $count);
#	}
#	elsif($count == 3)
#	{
#		print_result($result, $query, $count);
#		print_facts();
#		print_wa();
#	}
#	else
#	{
#		print_result($result, $query, $count);
#	}
#	
#	$count ++;
#}

#####END SEARCH RESULTS#####

print_footer();

#####FUNCTIONS#####

sub print_modal
{
	my ($query) = (@_);

	print qq{
		<!--Modal NOTES Start-->
                <div class="modal fade" id="myNOTESModal" tabindex="-1" role="dialog" aria-labelledby="myNOTESModal" aria-hidden="true">
                <div class="modal-dialog modal-lg">
                <div class="modal-content">
                <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>
                <h4 class="modal-title" id="myModalLabel">Notes - $query</h4>
                </div>
                <div class="modal-body">
                <iframe src="http://harvix.com/search/new/notes/notes.html" height="500px" width="100%" frameborder="0"></iframe>
                </div>
                </div>
                </div>
                </div>
                <!--Modal NOTES End-->
                <!--Modal CITE Start-->
                <div class="modal fade" id="myCITEModal" tabindex="-1" role="dialog" aria-labelledby="myCITEModal" aria-hidden="true">
                <div class="modal-dialog modal-lg">
                <div class="modal-content">
                <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>
                <h4 class="modal-title" id="myModalLabel">Citations</h4>
                </div>
                <div class="modal-body">
                <iframe id="iframeCITE" height="500px" width="100%" frameborder="0"></iframe>
                </div>
                </div>
                </div>
                </div>
                <!--Modal CITE End-->
	};
}

sub print_result
{
	my ($result, $query, $count) = (@_);

	print qq{
		<!--Start Web Result-->
                <li>
                <div class="timeline-badge info"><i class="glyphicon glyphicon-bookmark"></i></div>
                <div class="timeline-panel">
                <div class="media">
                <a class="pull-right" href="">
                <img class="media-object img-rounded" src="" alt="" height="200px" onerror="this.style.display='none'" alt="">
                </a>
                <div class="timeline-heading">                
		<h4 class="timeline-title"><a href="$result->{url}" target="_blank">$result->{title}</a></h4>
                </div>
                <div class="timeline-body">                
		<p>$result->{abstract}</p>
                <p><small class="text-muted"><i class="glyphicon glyphicon-ok"></i> $result->{dispurl}</small></p>  
		<br />
	};

	web_expand($count, $result->{title});
	button_bar($result->{title}, $result->{abstract}, $result->{url}, $query, $count);

	print qq{                              
                </div>
                </div>
                </div>
                </li>
                <!--End Web Result-->
	};
}

sub web_expand
{
	my ($count, $title) = (@_);	

	print qq{
		<!--Modal Web Expand Start-->
                <div class="modal fade" id="myWEBexpandModal$count" tabindex="-1" role="dialog" aria-labelledby="myWEBexpandModal$count" aria-hidden="true">
                <div class="modal-dialog modal-lg">
                <div class="modal-content">
                <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>
                <h4 class="modal-title" id="myModalLabel">$title</h4>
                </div>
                <div class="modal-body">
                <iframe id="WEBexpand$count" height="500px" width="100%" frameborder="0"></iframe>
                </div>
                </div>
                </div>
                </div>
                <!--Modal Web Expand End-->
	};
}

sub print_wiki
{
	my ($result, $query, $count) = (@_);

	print qq{
		<!--Start Web Result-->
                <li>
                <div class="timeline-badge success"><i class="glyphicon glyphicon-info-sign"></i></div>
                <div class="timeline-panel">
                <div class="media">
                <a class="pull-right" href="">
                <img class="media-object img-rounded" src="" alt="" height="200px" onerror="this.style.display='none'" alt="">
                </a>
                <div class="timeline-heading">                
                <h4 class="timeline-title"><a href="$result->{url}" target="_blank">$result->{title}</a></h4>
                </div>
                <div class="timeline-body">                
                <p>$result->{abstract}</p>
                <p><small class="text-muted"><i class="glyphicon glyphicon-ok"></i> $result->{dispurl}</small></p>
		<br />                                
        };

	web_expand($count, $result->{title});
        button_bar($result->{title}, $result->{abstract}, $result->{url}, $query, $count);        
	
	print qq{
		</div>
                </div>
                </div>
                </li>
                <!--End Web Result-->
	};
}

sub print_facts
{
	print qq{
		<!--Start Facts-->
                <li class="timeline-inverted">
                <div class="timeline-badge warning"><i class="glyphicon glyphicon-list"></i></div>
                <div class="timeline-panel">
                <div class="timeline-heading">
                </div>
                <div class="timeline-body">
                <p><iframe src="http://harvix.com/facts_searchv2.cgi?$query" width="100%" height="310px" class="restricted" overflow-y="hidden" frameborder="0"></iframe></p>
                </div>
                </div>
                </li>
                <!--End Facts-->
	};
}

sub print_wa
{
	print qq{
		<!--Start Wolf-->
                <li>
                <div class="timeline-badge danger"><i class="glyphicon glyphicon-tasks"></i></div>
                <div class="timeline-panel">
                <div class="timeline-body">
                <p><div style=\"background: #ffffff url(http://www.domaine-saint-pierre.fr/skin/frontend/default/default/images/home/loading.gif) no-repeat 50% 5%;\">
                <iframe src="http://harvix.com/wolf.cgi?$query" allowTransparency="true"  width="100%" height="300px" frameborder="0"></iframe></p>
                </div>
                </div>
                </li>
                <!--End Wolf-->
	};
}

sub button_bar
{
	my ($title, $snippet, $url, $query, $count) = (@_);
	$snippet =~ s|<.+?>||g;
	print qq{
		<!--Like Dislike Flag-->
               	<p>
                <div class="btn-group">
                <button type="button" class="btn btn-default" data-toggle="modal" data-target="#myNOTESModal"><i class="glyphicon glyphicon-pencil"></i></button>
                <button type="button" class="btn btn-default" data-toggle="modal" data-target="#myWEBexpandModal$count" onClick='document.getElementById("WEBexpand$count").src="$url";'><i class="glyphicon glyphicon-fullscreen"></i></button>
                <button type="button" class="btn btn-default" data-toggle="modal" onClick='document.getElementById("iframeCITE").src="http://harvix.com/search/new/cite.cgi?u=$url";' data-target="#myCITEModal"><i class="glyphicon glyphicon-pushpin"></i></button>
                <a href="http://harvix.com/content.php?url=$url&title=$title&snippet=$snippet&type=like&query=$query" class="btn btn-default"><i class="glyphicon glyphicon-thumbs-up"></i></a>
                <a href="http://harvix.com/content.php?url=$url&title=$title&snippet=$snippet&type=dislike&query=$query" class="btn btn-default"><i class="glyphicon glyphicon-thumbs-down"></i></a>    
                <a href="http://harvix.com/content.php?url=$url&title=$title&snippet=$snippet&type=flag&query=$query" class="btn btn-default"><i class="glyphicon glyphicon-flag"></i></a>
                </div>
                </p>
                <!--End Like Dislike Flag-->
	};
}

sub open_form
{
	my ($type, $title, $snippet, $url) = (@_);
	my $form_open_html = qq{
		<form action="http://harvix.com/content.php" method="post">
		<input type="hidden" name="page_url" value="http://harvix.com/search/new/dev5.cgi?q=$query"\>
		<input type="hidden" name="type" value="$type"\>
		<input type="hidden" name="title" value="$title"\>
		<input type="hidden" name="snippet" value="$snippet"\>
		<input type="hidden" name="url" value="$url"\>
		<input type="hidden" name="query" value="$query"\>
	};
	print $form_open_html;

}

sub close_form
{
	my $form_close_html = qq{
		</form>
	};
	print $form_close_html;
}

sub print
{
	my ($html_for_print) = (@_);
	my $html_print = qq{$html_for_print};
	print $html_print;
}

#sub show_modal
#{
#	my ($num, $title) = (@_);
#	my $print_modal = qq{
#		<!--Modal Else Expand Start-->
#     		<div class="modal fade" id="modalexpand$modalcount" tabindex="-1" role="dialog" aria-labelledby="modalexpand$modalcount" aria-hidden="true">
#                <div class="modal-dialog modal-lg">
#              	<div class="modal-content">
#             	<div class="modal-header">
#          	<button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>
#              	<h4 class="modal-title" id="myModalLabel">$title</h4>
#                </div>
#              	<div class="modal-body">
#              	<iframe id="frame$modalcount" height="500px" width="100%" frameborder="0"></iframe>
#            	</div>
#               	</div>
#              	</div>
#             	</div>
#             	<!--Modal Else Expand End-->
#	};
#	print $print_modal;
#}


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
    <link href="http://harvix.com/search/css2/timeline4.css" rel="stylesheet">
    <link href="http://harvix.com/search/css2/top-nav2.css" rel="stylesheet">

    <!-- Harvix Fav and Touch Icons / Mobile Icons -->
    <link rel="apple-touch-icon-precomposed" sizes="144x144" href="http://www.harvix.com/images/harvixshort2.jpg">
    <link rel="apple-touch-icon-precomposed" sizes="114x114" href="http://www.harvix.com/images/harvixshort2.jpg">
    <link rel="apple-touch-icon-precomposed" sizes="72x72" href="http://www.harvix.com/images/harvixshort2.jpg">
    <link rel="apple-touch-icon-precomposed" href="http://www.harvix.com/images/harvixshort2.jpg">
    <link rel="shortcut icon" href="http://www.harvix.com/images/harvixshort2.jpg">
 
    <!--Onpage Style-->
    <style>
a:link {text-decoration:none; color:#333;}      /* unvisited link */
a:visited {text-decoration:none; color:#333;}  /* visited link */
a:hover {text-decoration:none; color:#333;}  /* mouse over link */
a:active {text-decoration:none; color:#333;}  /* selected link */

      
    .glyphicon {
       top:2px;
    }
      
    #scrollable {
       overflow: overlay;
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

  <body style="background-image: url('http://1.bp.blogspot.com/-kSjPlU-wY9E/UK9PymRJV6I/AAAAAAAADh0/tCrD_Bn7UqI/s1600/body.png')">

<div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
      <div class="container-fluid">
        <div class="navbar-header">
          <a class="navbar-brand" href="http://harvix.com">Harvix</a>
        </div>
        <div class="navbar-collapse collapse">
          <form class="navbar-form">
            <input type="text" class="form-control" action="http://harvix.com/search/new/bak/mst3kv3.cgi" onsubmit="submitted('h'); return false" name="q"  class="search-query" value="$query">
	    <button type="submit" class="btn"><strong>Search</strong></button>
          </form>
        </div>
      </div>
    </div>

<div class="container">

<div class="page-header">
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

<!--Javascript-->
<script src="http://harvix.com/search/new/js/bootstrap.js"></script>
<script src="http://harvix.com/search/new/js/jquery.js"></script>
<script src="http://harvix.com/search/new/js/modal.js"></script>

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


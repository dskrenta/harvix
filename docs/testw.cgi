#!/usr/bin/perl

use strict;

use warnings;

use Data::Dumper;
use WebService::Blekko;
use Encode;
use Net::WolframAlpha;

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




print"
<div id=\"fb-root\"></div>
<script>(function(d, s, id) {
  var js, fjs = d.getElementsByTagName(s)[0];
  if (d.getElementById(id)) return;
  js = d.createElement(s); js.id = id;
  js.src = \"//connect.facebook.net/en_US/all.js#xfbml=1\";
  fjs.parentNode.insertBefore(js, fjs);
}(document, 'script', \'facebook-jssdk\'));</script>
\n";


# Instantiate WA object with your appid.
my $wa = Net::WolframAlpha->new (
    appid => 'XXX',
);

my $query = parse_query();

my $wiki = wiki_query($query);

my $blekko = WebService::Blekko->new( auth => 'c31c6fd0', );


my $res = $blekko->query( $query );

#if ( $res->error ) ...

print_header($query);

my @results;

while ( my $r = $res->next ) {
	push @results, {
			title => $r->title,
			snippet => $r->snippet,
			url => $r->url,
		};
}

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

	
	print"<table cellspacing=\"8\" cellpadding=\"5\" width=\"100%\"><tr><td>";

print"<div class=\"t\"><b>Web Results:</b></div><p>\n";

foreach my $res ( @results )
{
        print"<div class=\"t\">";
        print "<a href=", '"', $res->{url}, '">', $res->{title}, "</a><br>\n";

        my $snippet = $res->{snippet};
        if ( length($snippet) > 100 )
        {
                $snippet = substr($snippet, 0, 500);
                $snippet =~ s/\s[^\s]*$//;
                $snippet .= ' ...';
        }
        print $snippet, "<br>\n";

        print "<span style=\"color:green;\">";
        print $res->{url}, "<br> </span> </div> <div class=\"fb-like\" data-href=\"$res->{url}\" data-send=\"false\" data-layout=\"button_count\" data-width=\"1\" data-show-faces=\"true\"></div> <a href=\"https://twitter.com/share\" class=\"twitter-share-button\" data-url=\"$res->{url}\">Tweet</a>\n";
        print "</div><p>\n";
        }
	print"</td><td valign=top>";


if ( $wiki )
        {
            my ( $wiki_best, $wiki_rank, $wiki_fnam, $wiki_title, $wiki_page, $wiki_image, $wiki_url ) = @$wiki;

                utf8_off($wiki_title);
                utf8_off($wiki_page);
                utf8_off($wiki_url);


		print"<div class=\"t\"><b>Instant Information:</b></div><p>\n";		

                if ( $search_wiki )
                {
                        print"<div class=\"hi5\">";
                }
                else
                {
                        print"<div class=\"hi5\">";
                }
                print "<div class=\"t\">";
                print "<a href=", '"', $wiki_url, '"><b>', $wiki_title, "</b></a><br>\n";
                print "<p>";
                print"<table cellspacing=\"5\" cellpadding=\"5\"><tr><td>";
                print "<a href=\"$wiki_image\"><img src=\"$wiki_image\"></a> <p>\n" if $wiki_image ne '';
                print"</td>";
                print"<td>";
                print $wiki_page, "<br><a href=\"$wiki_url\"><b>read more ...</b></a>\n";
                print "<p>";
                print "<span style=\"color:green;\">";
                print $wiki_url, "<br>\n";
                print"<div class=\"fb-like\" data-href=\"$wiki_url\" data-send=\"false\" data-layout=\"button_count\" data-width=\"100\" data-show-faces=\"true\"></div> <a href=\"https://twitter.com/share\" class=\"twitter-share-button\" data-url=\"$wiki_url\">Tweet</a>\n";
                print "</td></tr></table>";
                print "</span>";
                print "</div></div><p><p>\n";
        }







if ($query->success) {

    print "Datatypes: ", $query->datatypes, "\n" if $query->datatypes;
    print "Timing: ", $query->timing, "\n" if $query->timing;
    print "Parsetiming: ", $query->parsetiming, "\n" if $query->parsetiming;
    print "Timedout: ", $query->timedout, "\n" if $query->timedout;

    # Associated with format='html'.
    print "CSS: ", $query->css, "\n" if $query->css;
    print "Scripts: ", $query->scripts, "\n" if $query->scripts;
    
    print "\n\n\nNumpods: ", $query->numpods, "\n";
    foreach my $pod (@{$query->pods}) {
	if (!$pod->error) {

	    print "\n\nPod title: ", $pod->title, "\n";
	    print "Scanner: ", $pod->scanner, "\n";
	    print "Position: ", $pod->position, "\n";
	    
	    # Associated with format='html'.
	    print "Markup: ", $pod->markup, "\n" if $pod->markup;
	    
	    # Associated with async='true'.
	    print "Async: ", $pod->async, "\n" if $pod->async;
	    
	    print "Numsubpods: ", $pod->numsubpods, "\n" if $pod->numsubpods;
	    foreach my $subpod (@{$pod->subpods}) {
		print "  Subpod\n";
		print '    plaintext: ', $subpod->plaintext, "\n" if $subpod->plaintext;
		print '    title: ', $subpod->title, "\n" if $subpod->title;
		print '    minput: ', $subpod->minput, "\n" if $subpod->minput;
		print '    moutput: ', $subpod->moutput, "\n" if $subpod->moutput;
		print '    mathml: ', $subpod->mathml, "\n" if $subpod->mathml;
		print '    img: ', $subpod->img, "\n" if $subpod->img;
	    }
	    
	    if ($pod->states->count) {
		print "  States\n";
		foreach my $state (@{$pod->states->state}) {
		    print "    name: ", $state->name, "\n";
		}
		
		foreach my $statelist (@{$pod->states->statelist}) {
		    print "    statelist: ", $statelist->value, "\n";
		    foreach my $state (@{$statelist->state}) {
		    print "      name: ", $state->name, "\n";
		    }
		}
	    }
	    
	    # Associated with format='sound'.
	    if ($pod->sounds->count) {
		print "  Sounds\n";
		foreach my $sound (@{$pod->sounds->sound}) {
		    print "    Sound: ", $sound->url, "\n";
		    print "      type: ", $sound->type, "\n";
		}
	    }
	    
	    if ($pod->infos->count) {
		print "  Infos\n";
		foreach my $info (@{$pod->infos->info}) {
		    print "    Info\n";
		    print "      text: ", $info->text, "\n" if $info->text;
		    
		    foreach my $link (@{$info->link}) {
			print "      link: ", $link->url, "\n";
			print "        title: ", $link->title, "\n" if $link->title;
			print "        text: ", $link->text, "\n" if $link->text;
		    }
		    
		    if ($info->units->count) {
			print "      units img: ", $info->units->img, "\n" if $info->units->img;
			foreach my $unit (@{$info->units->unit}) {
			    print "      unit: ", $unit->short, "\n";
			    print "        long: ", $unit->long, "\n";
			}
		    }
		}
	    }
	    
	} else {
	    print "Error ", $pod->error->code, ": ", $pod->error->msg, "\n";
	}
    }

	
    if ($query->assumptions->count) {
	print "\n\nAssumptions\n";
	foreach my $assumption (@{$query->assumptions->assumption}) {
	    print "\n  type: ", $assumption->type, "\n";
	    print "  word: ", $assumption->word, "\n" if $assumption->word;
	    foreach my $value (@{$assumption->value}) {
		print '    ', $value->name, ', ', $value->desc, ' (', $value->input, ') ', "\n";
		print '     valid: ', $value->valid, "\n" if defined $value->valid;
	    }
	}
    }
    
    if ($query->sources->count) {
	print "\n\nSources\n";
	foreach my $source (@{$query->sources->source}) {
	    print "  url: ", $source->url, "\n";
	    print "  text: ", $source->text, "\n" if $source->text;
	}
    }
	
    if ($query->warnings->count) {
	print "\nWarnings\n";
	print "  delimiters: ", $query->warnings->delimiters, "\n" if $query->warnings->delimiters;
	
	foreach my $spellcheck (@{$query->warnings->spellcheck}) {
	    print "  Spellcheck word: ", $spellcheck->word, "\n";
	    print "    suggestion: ", $spellcheck->suggestion, "\n" if $spellcheck->suggestion;
	    print "    text: ", $spellcheck->text, "\n" if $spellcheck->text;
	}
	
    }
    

# No success, but no error either.
} elsif (!$query->error) {
    print "No results.\n";

    if ($query->didyoumeans->count) {
	foreach my $didyoumean (@{$query->didyoumeans->didyoumean}) {
	    print "  Did you mean: ", $didyoumean->text, "\n"
	}
    }


# Error contacting WA.
} elsif ($wa->error) {
    print "Net::WolframAlpha error: ", $wa->errmsg , "\n" if $wa->errmsg;


# Error returned by WA.    
} elsif ($query->error) {
    print "WA error ", $query->error->code, ": ", $query->error->msg, "\n";

}








print"</td></tr></table>";

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

            if ( $wiki_title eq '' )
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
#	    elsif ( $wiki_title =~ /\b$query\b/i || $fnam_match =~ /\b$query\b/i )
#	    {
#		push @wiki_res, [ 2, $wiki_fnam ];
#	    }
#            else
#            {
#                push @wiki_res, [ 3, $wiki_fnam ];
#	    }

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
	$query =~ s/\+/ /g;

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
<html>
<head>
<title>Harvix Search - $query</title>
<link rel="shortcut icon" href="http://www.tinychan.org/img/1328039793912825.png" type="image/x-icon" />
<style type="text/css"> 
a:link {color:#1a54e1; text-decoration:none;}  
a:visited {color:#1a54e1; text-decoration:none;}
a:hover {color:red;}
body { font-size: 13px; font-family:  Helvetica, sans-serif; font-size: normal; line-height: normal; margin: 0; padding: 0; } 
div.header{font-size:130px;}

div.hi{width:100%; padding:8px; border:1px solid:black; margin:0px; background-color:black;}
div.hi2{font-size:20px;}

div.1footer{color:gray;}
div.bar{float:right;}
div.footer{clear:both;text-align:center;}
div.large{font-size:20px;}
div.h{font-size:18px;}
div.t{font-size:18px;}
div.o{width:20%; padding:2px; border:1px solid:#ffffff; margin:0px; background-color:#b31c1c;}
div.center{text-align:center;}
div.ex{width:35%; padding:2px; border:1px solid black;  margin:0px; -moz-border-radius: 15px; border-radius: 15px; background-color:#1a54e1;}
div.h{width:40%; padding:2px; border:1px solid black;  margin:0px; background-color:white;} 
body{background-color:white;}
div.po{width:50%; padding:2px; border:1px solid white;  margin:0px; -moz-border-radius: 15px; border-radius: 15px; background-color:white;}
 
 
 
#searchBox{font-size:18px;width:700px;line-height:26px;height:32px;10px;border:1px solid Black;}
#search-submit{height:38px;margin-top:8px;}.red-button:hover{background:#2E2E2E;}





html {
     height:100%
}
body {
     height:100%
}
#container {
     position:relative;
     min-height:100%;
     _height:100%; /* for IE6 as it doesnt understand min-height */
}
#content {
     padding-bottom:100px; /* assuming your footer height is 100px */
}
 
#footer {
     position: relative;
     margin-top:-100px;
     /* move the footer up negatively exactly the same height
         as the footer so that its back in the view and always
         appears to rest at the bottom
         of the page */
}


div.hi4{padding:4px; border:1px solid:gray; margin:0px; background-color:#D8D8D8;}
div.hi3{padding:4px; border:1px solid:gray; margin:0px; background-color:#AAFFAA;}
div.hi5{padding:8px; border:1px solid:gray; margin:0px; background-color:#D8D8D8; -moz-box-shadow: 0 0 1em black; -webkit-box-shadow: 0 0 1em black; box-shadow: 0 0 1em black;}

div.hi6{padding:8px; border:1px solid:gray; margin:0px; background-color:white; -moz-box-shadow: 0 0 1em black; -webkit-box-shadow: 0 0 1em black; box-shadow: 0 0 1em black;}

</style>
</head>





<div id="fb-root"></div>
<script>(function(d, s, id) {
  var js, fjs = d.getElementsByTagName(s)[0];
  if (d.getElementById(id)) return;
  js = d.createElement(s); js.id = id;
  js.src = "//connect.facebook.net/en_US/all.js#xfbml=1";
  fjs.parentNode.insertBefore(js, fjs);
}(document, 'script', 'facebook-jssdk'));</script>



<script>!function(d,s,id){var js,fjs=d.getElementsByTagName(s)[0];if(!d.getElementById(id)){js=d.createElement(s);js.id=id;js.src="//platform.twitter.com/widgets.js";fjs.parentNode.insertBefore(js,fjs);}}(document,"script","twitter-wjs");</script>




<body style="margin:0px;">


<div id="container">
    <div id="content">

<table width="100%" cellpadding="0" cellspacing="0">
<tr><td colspan=5><span class="hh">

</span></td><td></td></tr>
<tr height=""><td></td></tr>

<tr>
<td width=15></td>

<td width=175 valign=top>
<div style="font-size:36pt">
<b><span style="color:black;">Har</span><span style="color:#b31c1c;">vix</span></b>
</div>
<p>
<img src="http://harvix.com/images/Harvixever.jpg">
<p>
<a href="http://harvix.com/test3.cgi?q=$query">Information</a>
<p>
<a href="http://harvix.com/test4.cgi?q=$query">Web</a>
<p>
<a href="http://harvix.com">Images</a>
<p>
<a href="http://harvix.com">Videos</a>
<p>
<div class="fb-like" data-href="http://harvix.com/test.cgi?q=$query" data-send="false" data-layout="button_count" data-width="100" data-show-faces="false"></div>
<p>
<div class="fb-comments" data-href="http://harvix.com/test.cgi?q=$query" data-num-posts="10" data-width="150"></div>
<p>
</td>
<td valign=top>

<table width="100%" cellpadding="0" cellspacing="0">

<tr><td>
<form id="searchform" name="searchForm" action="http://harvix.com/test2.cgi" onsubmit="submitted('s'); return false;">
<input type="text" id="searchBox" autofocus="autofocus" autocomplete="off" spellcheck="false" type="text" name="q" value="$query" />
<button type="submit" class="red-button" href="javascript:void(0);" id="search-submit" >Search</button></form>
<p>
EOF
;

}

sub print_footer
{
print <<EOX

</td>

<td width=100>&nbsp;</td>


<td valign=top align=right width=0>
&nbsp;
<p>



</td>

<td width=15>&nbsp;</td>

</tr>

</table>
</td></tr></table>

<p>
<p>
<p>
<p>
<center>
<p>
&nbsp;
<p>
&nbsp;
<p>
&nbsp;
<p>
&nbsp;

<div id="footer">
<div class="t"><a href="about.html">About</a> &middot; <a href="terms.html">Terms & Conditions</a> &middot; <a href="privacy.html">Privacy</a> &middot; <a href="contact.html">Contact</a> &middot; <a href="manegment.html">Management</a> &middot;  <span style="color:gray;">&copy; - 2012 Harvix.</span> 
</div> 
</div>
</div></center>
</body>

EOX
;
}



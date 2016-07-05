#!/usr/bin/perl

use strict;

use Data::Dumper;
use WebService::Blekko;
use WebService::GData::YouTube;
use WWW::Google::Images;
use Net::WolframAlpha;
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

my $wa = Net::WolframAlpha->new (
    appid => '3EP4EG-Q7UKGAPR4Q',
);


my $query = parse_query();

my $wiki = wiki_query($query);

my $blekko = WebService::Blekko->new( auth => 'c31c6fd0', );


my $wa_query = $wa->query(
    input => $query,
);

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

#START	


print"<div class=\"page-region\"> <div class=\"page-region-content tiles\"> ";



if ( $wiki )
        {
            my ( $wiki_best, $wiki_rank, $wiki_fnam, $wiki_title, $wiki_page, $wiki_image, $wiki_url ) = @$wiki;

                utf8_off($wiki_title);
                utf8_off($wiki_page);
                utf8_off($wiki_url);

	print" <div class=\"tile double quadro-vertical\">";
	print"<div class=\"tile-content\">";
	print" <img src=\"$wiki_image\" width=\"270px\" class=\"place-left\"/>";
	print" <p> ";
	print" <h3 style=\"margin-bottom: 5px;\">$wiki_title</h3> ";
        print"  <p> ";
        print" $wiki_page ";
	print"		</p> ";
        print"                <h5>$wiki_url</h5> ";
	print"</div> </div> ";
	


	}



foreach my $res ( @results )
{

	print"<div class=\"tile triple\">
                    <div class=\"tile-content\">";

	print"<h1><a href=\"$res->{url}\">$res->{title}</a><br></h1>";


        my $snippet = $res->{snippet};
        if ( length($snippet) > 100 )
        {
                $snippet = substr($snippet, 0, 500);
                $snippet =~ s/\s[^\s]*$//;
                $snippet .= ' ...';
        }
        print $snippet, "<br>";

        print"$res->{url}";

	print"</div></div>";


        }



#END


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

            if ( my  $wiki_title eq '' )
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

print"<div class=\"h10\"><u>";
    print $pod->{title}, ":\n<p>";
print"</u>";

    foreach my $subpod ( @{ $pod->{subpods} } )
    {
        next if !defined $subpod->{plaintext};
        if ( defined $subpod->{img} )
        {
            print "    ", $subpod->{img}, "\n<p>";
        }

        #my $s = $subpod->{plaintext};
        #$s =~ s/\n/\n    /gs;
        #print "    ", $s, "\n";
    }
    print "</div>";
}



sub print_header
{
	my ( $query ) = @_;

	$query =~ s/[<>\&]//g;

print <<EOF


<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/html">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="target-densitydpi=device-dpi, width=device-width, initial-scale=1.0, maximum-scale=1">
    <meta name="description" content="Harvix Search">

    <link href="http://metroui.org.ua/css/modern.css" rel="stylesheet">
    <link href="http://metroui.org.ua/css/theme-dark.css" rel="stylesheet">
    <link href="http://metroui.org.ua/css/modern-responsive.css" rel="stylesheet">

    <script src="http://metroui.org.ua/js/assets/jquery-1.8.2.min.js"></script>
    <script src="http://metroui.org.ua/js/assets/github.info.js"></script>
    <script src="http://metroui.org.ua/js/modern/tile-slider.js"></script>
    <script src="http://metroui.org.ua/js/modern/tile-drag.js"></script>

    <title>Harvix Search | $query</title>

    <style>
        body {
            background: #1d1d1d;
        }
    </style>

    <script>
        function Resize(){
            var tiles_area = 0;
            $(".tile-group").each(function(){
                tiles_area += $(this).outerWidth() + 80;

            });

            $(".tiles").css("width", 120 + tiles_area + 20);

            $(".page").css({
                height: $(document).height() - 20,
                width: $(document).width()
            });
        }


        $(function(){

            Resize();

        })


    </script>
</head>
<body class="modern-ui" onresize="Resize()">




EOF
;

}

sub print_footer
{
print <<EOX

</div>
</div>
</div>
<a href='http://hit.ua/?x=19154' target='_blank'>
    <script language="javascript" type="text/javascript"><!--
    Cd=document;Cr="&"+Math.random();Cp="&s=1";
    Cd.cookie="b=b";if(Cd.cookie)Cp+="&c=1";
    Cp+="&t="+(new Date()).getTimezoneOffset();
    if(self!=top)Cp+="&f=1";
    //--></script>
    <script language="javascript1.1" type="text/javascript"><!--
    if(navigator.javaEnabled())Cp+="&j=1";
    //--></script>
    <script language="javascript1.2" type="text/javascript"><!--
    if(typeof(screen)!='undefined')Cp+="&w="+screen.width+"&h="+
            screen.height+"&d="+(screen.colorDepth?screen.colorDepth:screen.pixelDepth);
    //--></script>
    <script language="javascript" type="text/javascript"><!--
    Cd.write("<img src='http://c.hit.ua/hit?i=19154&g=0&x=2"+Cp+Cr+
            "&r="+escape(Cd.referrer)+"&u="+escape(window.location.href)+
            "' border='0' wi"+"dth='1' he"+"ight='1'/>");
    //--></script>
    <noscript>
        <img src='http://c.hit.ua/hit?i=19154&amp;g=0&amp;x=2' border='0'/>
    </noscript></a>
<!-- / hit.ua -->

</body>
</html>


EOX
;
}



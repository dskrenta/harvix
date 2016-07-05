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


my $query = parse_query();


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

print"

<div id=\"tabs\">
    <ul>
        <li><a href=\"#tabs-1\">Nunc tincidunt</a></li>
        <li><a href=\"#tabs-2\">Proin dolor</a></li>
        <li><a href=\"#tabs-3\">Aenean lacinia</a></li>
    </ul>
    <div id=\"tabs-1\">
";

#START OF SEARCH
 	


foreach my $res ( @results )
{
       	
	print "<div class=\"large4\"><b><u><a href=", '"', $res->{url}, '">', $res->{title}, "</a></u></b><br></div>\n";

	        print "<span style=\"color:green;\">";
        print $res->{url}, "<br> </span>\n";
	
        my $snippet = $res->{snippet};
        if ( length($snippet) > 100 )
        {
                $snippet = substr($snippet, 0, 500);
                $snippet =~ s/\s[^\s]*$//;
                $snippet .= ' ...';
        }
        print $snippet, "<br>\n";

        print "<p>\n";
        }

	print"Web results powered by blekko<p>\n";


#END OF SEARCH
print"

</div>
    <div id=\"tabs-2\">
        <p>Morbi tincidunt, dui sit amet facilisis feugiat, odio metus gravida ante, ut pharetra massa metus id nunc. Duis scelerisque molestie turpis. Sed fringilla, massa eget luctus malesuada, metus eros molestie lectus, ut tempus eros massa ut dolor. Aenean aliquet fringilla sem. Suspendisse sed ligula in ligula suscipit aliquam. Praesent in eros vestibulum mi adipiscing adipiscing. Morbi facilisis. Curabitur ornare consequat nunc. Aenean vel metus. Ut posuere viverra nulla. Aliquam erat volutpat. Pellentesque convallis. Maecenas feugiat, tellus pellentesque pretium posuere, felis lorem euismod felis, eu ornare leo nisi vel felis. Mauris consectetur tortor et purus.</p>
    </div>
    <div id=\"tabs-3\">
        <p>Mauris eleifend est et turpis. Duis id erat. Suspendisse potenti. Aliquam vulputate, pede vel vehicula accumsan, mi neque rutrum erat, eu congue orci lorem eget lorem. Vestibulum non ante. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Fusce sodales. Quisque eu urna vel enim commodo pellentesque. Praesent eu risus hendrerit ligula tempus pretium. Curabitur lorem enim, pretium nec, feugiat nec, luctus a, lacus.</p>
        <p>Duis cursus. Maecenas ligula eros, blandit nec, pharetra at, semper at, magna. Nullam ac lacus. Nulla facilisi. Praesent viverra justo vitae neque. Praesent blandit adipiscing velit. Suspendisse potenti. Donec mattis, pede vel pharetra blandit, magna ligula faucibus eros, id euismod lacus dolor eget odio. Nam scelerisque. Donec non libero sed nulla mattis commodo. Ut sagittis. Donec nisi lectus, feugiat porttitor, tempor ac, tempor vitae, pede. Aenean vehicula velit eu tellus interdum rutrum. Maecenas commodo. Pellentesque nec elit. Fusce in lacus. Vivamus a libero vitae lectus hendrerit hendrerit.</p>
    </div>
</div>

";


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






sub print_header
{
	my ( $query ) = @_;

	$query =~ s/[<>\&]//g;

print <<EOF
<html>
<head>
<title>Harvix Web Search - $query</title> 
<link rel="shortcut icon" href="http://www.tinychan.org/img/1328039793912825.png" type="image/x-icon" /> 





    <link rel="stylesheet" href="http://code.jquery.com/ui/1.9.1/themes/base/jquery-ui.css" />
    <script src="http://code.jquery.com/jquery-1.8.2.js"></script>
    <script src="http://code.jquery.com/ui/1.9.1/jquery-ui.js"></script>
    <link rel="stylesheet" href="/resources/demos/style.css" />
    <script>
    $(function() {
        $( "#tabs" ).tabs();
    });
    </script>



<style type="text/css"> 
a:link {color:#5858FA; text-decoration:none;}  
a:visited {color:#5858FA; text-decoration:none;}
a:hover {color:red;}
body { font-size: 12px; width:100%; font-family:  Helvetica, sans-serif; font-size: normal; line-height: normal; margin: 0; padding: 0; } 
div.header{font-size:150px;}
div.header1{font-size:20px;}
div.hi{width:98%; padding:8px; border:0px solid:black; margin:0px; background-color:white;}
div.hi2{font-size:20px;}
div.h7{width:100%; position: fixed; padding:4px; border:0px solid:black; margin:0px; background-color:black; -moz-box-shadow: 0 0 1em black; -webkit-box-shadow: 0 0 1em black; box-shadow: 0 0 1em black;}
div.1footer{color:gray;}
div.bar{float:right;}
div.footer{clear:both;text-align:center;}
div.large{font-size:50px; font-family:  Helvetica, sans-serif; font-size: normal; line-height: normal;}
div.large4{font-size:18px;}
div.h{font-size:15px;}
div.t{font-size:15px;}
div.o{width:20%; padding:2px; border:1px solid:#ffffff; margin:0px; background-color:#b31c1c;}
div.center{text-align:center;}
div.ex{width:35%; padding:2px; border:1px solid black;  margin:0px; -moz-border-radius: 15px; border-radius: 15px; background-color:#1a54e1;}
div.h{width:40%; padding:2px; border:1px solid black;  margin:0px; background-color:white;} 
body{background-color:white;}
div.po{width:50%; padding:2px; border:1px solid white;  margin:0px; -moz-border-radius: 15px; border-radius: 15px; background-color:white;}
 div.h8{width:100%; padding:8px; border:0px solid:black; margin:0px; background-color:black;}
div.semilarge{font-size:20px;} 
div.bar2{float:left;}

div.h0{width:; padding:8px; border:0px solid:black; margin:0px; background-color:#F6F6F6; -moz-box-shadow: 0 0 1em black; -webkit-box-shadow: 0 0 1em black; box-shadow: 0 0 1em black;}

div.h10{width:; padding:8px; border:0px solid:black; margin:0px; background-color:white; -moz-box-shadow: 0 0 1em black; -webkit-box-shadow: 0 0 1em black; box-shadow: 0 0 1em black;}

div.h11{width:10%; padding:8px; border:0px solid:black; margin:0px; background-color:white; -moz-box-shadow: 0 0 1em black; -webkit-box-shadow: 0 0 1em black; box-shadow: 0 0 1em black;}

div.side{width:50px; padding:8px; border:0px solid:black; margin:0px; background-color:white;}

div.h12{width:; padding:4px; border:0px solid:black; margin:0px; background-color:white; -moz-box-shadow: 0 0 1em black; -webkit-box-shadow: 0 0 1em black; box-shadow: 0 0 1em black;}

#footer{clear:both;padding:10px 0;text-transform:uppercase;height:12px;font-size:10.5px;overflow:hidden;background:#2c2c2b;background:-moz-linear-gradient(top, #2c2c2b 0%, #262426 49%, #232222 50%, #1e201e 100%);background:-webkit-gradient(linear, left top, left bottom, color-stop(0%,#2c2c2b), color-stop(49%,#262426), color-stop(50%,#232222), color-stop(100%,#1e201e));background:-webkit-linear-gradient(top, #2c2c2b 0%,#262426 49%,#232222 50%,#1e201e 100%);background:-o-linear-gradient(top, #2c2c2b 0%,#262426 49%,#232222 50%,#1e201e 100%);background:-ms-linear-gradient(top, #2c2c2b 0%,#262426 49%,#232222 50%,#1e201e 100%);background:linear-gradient(top, #2c2c2b 0%,#262426 49%,#232222 50%,#1e201e 100%);filter:progid:DXImageTransform.Microsoft.gradient( startColorstr='#2c2c2b', endColorstr='#1e201e',GradientType=0 );}#footer p{margin:0 10px}#footer a{color:#818181;padding-right:15px;}#footer .copyright{float:right;color:#818181;}

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
     margin-top:-50px;
     /* move the footer up negatively exactly the same height
         as the footer so that its back in the view and always
         appears to rest at the bottom
         of the page */
}


#searchBox{width:600px;}
#searchBox{font-size:25px;line-height:30px;height:30px;outline:none;border:1px solid #AAA;}
#searchBox{height:40px;clear:both;}
#search-submit{width:100px;}
#search-submit{height:40px;}
.red-button{height:32px;border:none 0;outline:none 0;font-size:14px;color:#FFF;cursor:pointer;font-weight:bold;background:#ef3625;background:-moz-linear-gradient(top, #ef3625 0%, #d02f20 100%);background:-webkit-gradient(linear, left top, left bottom, color-stop(0%,#ef3625), color-stop(100%,#d02f20));background:-webkit-linear-gradient(top, #ef3625 0%,#d02f20 100%);background:-o-linear-gradient(top, #ef3625 0%,#d02f20 100%);background:-ms-linear-gradient(top, #ef3625 0%,#d02f20 100%);background:linear-gradient(top, #ef3625 0%,#d02f20 100%);filter:progid:DXImageTransform.Microsoft.gradient( startColorstr='#ef3625', endColorstr='#d02f20',GradientType=0 );}
.search-icon{background:url('http://a.blekko-img.com/045/gz/theme21/imgs/serp08.png') no-repeat -212px 0;width:20px;height:20px;display:inline-block;}


</style>
</head> 
<body>
<div id="fb-root"></div>
<script>(function(d, s, id) {
  var js, fjs = d.getElementsByTagName(s)[0];
  if (d.getElementById(id)) return;
  js = d.createElement(s); js.id = id;
  js.src = "//connect.facebook.net/en_US/all.js#xfbml=1";
  fjs.parentNode.insertBefore(js, fjs);
}(document, 'script', 'facebook-jssdk'));</script>

<div class="h7">
<table cellpadding="0">
<tr VALIGN=BOTTOM>
<td>
<div class="large">
<a href="index.html"><b><span style="color:white;">Har</span><span style=color:red;">vix</span></b></a>
</div>
</td>
<td>
<form id="searchForm" name="searchForm" action="http://harvix.com/harvixweb.cgi" onsubmit="submitted('h'); return false">
<input id="searchBox" autofocus="autofocus" autocomplete="off" type="text" spellcheck="false" name="q" value="$query"  />
<button type="submit" class="red-button"  href="javascript:void(0);" id="search-submit" ><span class="search-icon"></span></button>
</form>
</td>
</tr>
</table>
</div>
<p>
&nbsp;
<p>
&nbsp;
<p>
&nbsp;
<p>
</div>
EOF
;

}

sub print_footer
{
print <<EOX


</div>
</div>
<p>
&nbsp;
<div id="footer">
<span class="copyright"> &copy; 2012 harvix, inc.</span>
<p>
<a href="about.html">about</a>&nbsp;
<a href="privacy.html">privacy policy</a>&nbsp;
<a href="terms.html">terms & condtions</a>&nbsp;
</p>
</div>
</body> 
<html> 
EOX
;
}



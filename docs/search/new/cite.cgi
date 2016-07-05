#!/usr/bin/perl

use strict;
use URI::Fetch;
use POSIX qw(strftime);

my %escapes;
setup_escapes();

#Structure: Last name, First name. "Article Title." Website Title. Publisher of Website, Day Month Year article was published. Web. Day Month Year article was accessed. <URL>.

print "Content-type: text/html\n\n";

my $url = parse_url();

my $result_code = URI::Fetch->fetch($url);

my $result_code_html = $result_code->content();

print_header();

my $tab_html = qq{
	<ul id="myTab" class="nav nav-tabs">
      	<li class="active"><a href="#cite" data-toggle="tab">Cite</a></li>
      	<li><a href="#web" data-toggle="tab" onClick='document.getElementById("iframeWEB").src="$url";'>Website</a></li>
    	</ul>
	<div id="myTabContent" class="tab-content">
      	<div class="tab-pane fade in active" id="cite">
};
print $tab_html;

print"<form method=\"post\" action=\"cite.php\"></p>";

print"<div class=\"form-group has-error\"><p><label class=\"control-label\">Author's Name:</label><input type=\"text\" class=\"form-control\" placeholder=\"Last name, First name of Author\" name=\"one\"></p></div>";

if ($result_code_html =~ m|<title>(.*?)</title>|)
{
        my $html_extract_title = $1;
        print "<p><label class=\"control-label\">Article Title:</label><input type=\"text\" class=\"form-control\" placeholder=\"Article Title\" value=\"$html_extract_title\" name=\"two\"></p>";
	print "<p><label class=\"control-label\">Website Title:</label><input type=\"text\" class=\"form-control\" placeholder=\"Website Title\" value=\"$html_extract_title\" name=\"three\"></p>";
}
	
else
{
	print "<div class=\"form-group has-error\"><p><label class=\"control-label\">Article Title:</label><input type=\"text\" class=\"form-control\" placeholder=\"Article Title\" id=\"inputError1\" name=\"two\"></p></div>";
	print "<div class=\"form-group has-error\"><p><label class=\"control-label\">Website Title:</label><input type=\"text\" class=\"form-control\" placeholder=\"Website Title\" id=\"inputError1\" name=\"three\"></p></div>";
}

print "<div class=\"form-group has-error\"><p><label class=\"control-label\">Publisher of Website:</label><input type=\"text\" class=\"form-control\" placeholder=\"Publisher of Website\" name=\"four\"></p></div>";

print "<div class=\"form-group has-error\"><p><label class=\"control-label\">Publication Date:</label><input type=\"text\" class=\"form-control\" placeholder=\"Day, Month, Year article was published\" name=\"five\"></p></div>";

#Current Date
my @months = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December");   

#Month
my $month_num = strftime "%m", localtime;
my $month_array_num = $month_num - 1;
my $display_month = $months[$month_array_num];

#Day
my $day_num = strftime "%d", localtime;
my $display_day = $day_num;

#Year
my $year_num = strftime "%y", localtime;
my $display_year = $year_num; 

print "<p><label class=\"control-label\">Current Date:</label><input type=\"text\" class=\"form-control\" placeholder=\"Current Date\" value=\"$display_month $display_day, 20$display_year\" name=\"six\"></p>";

print "<p><label class=\"control-label\">Website URL:</label><input type=\"text\" class=\"form-control\" placeholder=\"Website URL\" value=\"$url\" name=\"seven\"></p>";

print "<p><button class=\"btn btn-large btn-primary\" type=\"submit\">Cite</button></p>";

print "<p></form></p>";

my $tab_html_two = qq{
	</div>
        <div class="tab-pane fade" id="web">
        <p><div style=\"background: #ffffff url(http://www.domaine-saint-pierre.fr/skin/frontend/default/default/images/home/loading.gif) no-repeat 50% 5%;\">
       	<iframe allowTransparency="true"  width="100%" height="500px" frameborder="0" id="iframeWEB"></iframe></p>
	</div>
        </div>
};
print $tab_html_two;

print_footer();

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

sub setup_escapes
{
        for (0..255)
        {
            $escapes{chr($_)} = sprintf("%%%02X", $_);
        }
        $escapes{' '} = '+';
}

sub parse_url
{
        my $url = $ENV{QUERY_STRING} || shift || "http://en.wikipedia.org/wiki/American_Civil_War";

        $url =~ s/u=//;
        $url = urldecode($url);

        return $url;
}

sub print_header
{
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
    <title>Harvix Cite</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="">
    <meta name="author" content="Harvix Search">

    <!-- Harvix Search Page Styles -->
    <link href="http://harvix.com/search/css2/bootstrap.css" rel="stylesheet">

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


<!-- START DYNAMIC CGI -->

EOF
;
}

sub print_footer
{
print <<EOX

<!-- END DYNAMIC CGI -->

</div>

<!--Javascript-->
<script src="http://harvix.com/search/new/js/bootstrap.js"></script>
<script src="http://harvix.com/search/new/js/jquery.js"></script>
<script src="http://harvix.com/search/new/js/modal.js"></script>
<script src="http://harvix.com/search/new/js/tab.js"></script>

</body>
</html>

EOX
;
}



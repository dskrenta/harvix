#!/usr/bin/perl

#Harvix Search

# call specilized perl modules

use strict;
use JSON;
use URI::Fetch;

my %escapes;
setup_escapes();

print "Content-type: text/html\n\n";



my $query = parse_query();

print_header();

#quotes for people
my $quotesquery = $query;
$quotesquery =~ s/\s/+/g;

my $quotes = URI::Fetch->fetch("http://www.stands4.com/services/v2/quotes.php?uid=2942&tokenid=XlMcm3XQlTYJNhMU&searchtype=AUTHOR&query=$quotesquery");
my $content = $quotes->content;

my @array = split(/<result\>/, $content);
my @goodarray;

my $conttemp = 1;
my $contx = 0;

my $peoplequotes; 

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
my $quotescont = -1;
foreach my $result ( @goodarray ) {
    $quotescont ++;
    if ($temp == 0) {
        $temp = 1;
        next;
    }
    my @thisauthor = split("<author>",$result);
    $peoplequotes = $peoplequotes . '<div class="item2">
                <div class="hero-unit-spec"> <p>
                                        <b>' . $quotescont . '.</b>
                                        ' . ucfirst( @thisauthor[0]) . '
                                        </p>
                                        <p><span style="color:green">' . @thisauthor[1] . '</span></p></div></div>';
}


#quotes for social
my $quotesquery = $query;
$quotesquery =~ s/\s/+/g;

my $quotes = URI::Fetch->fetch("http://www.stands4.com/services/v2/quotes.php?uid=2942&tokenid=XlMcm3XQlTYJNhMU&searchtype=SEARCH&query=$quotesquery");
my $content = $quotes->content;

my @array = split(/<result\>/, $content);
my @goodarray;

my $conttemp = 1;
my $contx = 0;

my $socialquotes; 

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
my $quotescont = -1;
foreach my $result ( @goodarray ) {
    $quotescont ++;
    if ($temp == 0) {
        $temp = 1;
        next;
    }
    my @thisauthor = split("<author>",$result);
    $socialquotes = $socialquotes . '<div class="item2">
                <div class="hero-unit-spec">	<p>
                                        <b>' . $quotescont . '.</b>
                                        ' . ucfirst( @thisauthor[0]) . '
                                        </p>
                                        <p><span style="color:green">' . @thisauthor[1] . '</span></p></div></div>';
}




print"<div class=\"panel panel-danger\"><div class=\"panel-heading\"><h3 class=\"panel-title\">QUOTES</h3></div><div class=\"panel-body\">";

print"<div id=\"scrollable\"><div id=\"items\">";

if($peoplequotes ne ''){
 
    print $peoplequotes;

    if ($socialquotes eq '') {
    } else {
    }
    
}

if ($peoplequotes eq '' && $socialquotes eq '') {
    print '<h2>No Quotes</h2>';
}

print"</div></div>";

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
                <title>$query | Harvix</title>
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <meta name="description" content="">
                <meta name="author" content="">

                <!-- Le styles -->
                <link href="http://harvix.com/bootstrap.css" rel="stylesheet">
                <style type="text/css">
                   body{
                        background-color: white;
                   }


a:link {text-decoration:none; color:blue;}      /* unvisited link */
a:visited {text-decoration:none; color:blue;}  /* visited link */
a:hover {text-decoration:none; color:blue;}  /* mouse over link */
a:active {text-decoration:none; color:blue;}  /* selected link */



   #scrollable {
       overflow: auto;
       width:100%;
       height:260px; 
    }


   #scrollable-img {
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
        height:250px;
     float:left;      
  }

 .item3{
        width:350px;
        height:220px;
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
            </head>
            <body>
EOF
}

sub print_footer {

    print <<EOX;
       

 <!-- Le javascript
    ================================================== -->
    <!-- Placed at the end of the document so the pages load faster -->
    <script src="http://getbootstrap.com/2.3.2/assets/js/jquery.js"></script>
    <script src="http://getbootstrap.com/2.3.2/assets/js/bootstrap-transition.js"></script>
    <script src="http://getbootstrap.com/2.3.2/assets/js/bootstrap-tab.js"></script>


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

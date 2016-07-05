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




print"<div class=\"hero-unit-wiki\">";
print" <ul id=\"myTab\" class=\"nav nav-tabs\">
<li class=\"active\"><a href=\"#instant\" data-toggle=\"tab\">Facts</a></li>
<li><a href=\"#quotes\" data-toggle=\"tab\">Quotes</a></li>
</ul>";
print"<div id=\"myTabContent\" class=\"tab-content\">
<div class=\"tab-pane fade in active\" id=\"instant\">";

print"IHIHHIHHIHIHIHIHI";

print"</div>";
print"<div class=\"tab-pane fade\" id=\"quotes\">";

print "<div id=\"upper\"><span class=\"label label-important\"><h5>People Quotes:</h5></span></div><hr></hr>";

print"<div id=\"scrollable\"><div id=\"items\">";

if($peoplequotes ne ''){
 
    print $peoplequotes;

    if ($socialquotes eq '') {
        #print '</div></div></div>';
    } else {
        #print '</div></div></div>';
    }
    
}

print"</div></div>";

print "<div id=\"upper\"><span class=\"label label-important\"><h5>Social Quotes:</h5></span></div><hr></hr>";

print"<div id=\"scrollable\"><div id=\"items\">";

if($socialquotes ne ''){
    
    print $socialquotes;

    #if ($peoplequotes eq '') {
        print '</div></div></div>';
    #} else {
        print '</div></div></div>';
    #}
}
if ($peoplequotes eq '' && $socialquotes eq '') {
    print '<h2>No Quotes</h2>';
}

print"</div><div>";

print"</div>";
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

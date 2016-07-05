#!/usr/bin/perl

# code written by Lorenzo F. Antunes CTO of Harvix Search Aug 2013

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
    $peoplequotes = $peoplequotes . '<p>
                                        <b>' . $quotescont . '.</b>
                                        ' . ucfirst( @thisauthor[0]) . '
                                        </p>
                                        <p><span style="color:green">' . @thisauthor[1] . '</span></p><hr>';
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
    $socialquotes = $socialquotes . '<p>
                                        <b>' . $quotescont . '.</b>
                                        ' . ucfirst( @thisauthor[0]) . '
                                        </p>
                                        <p><span style="color:green">' . @thisauthor[1] . '</span></p><hr>';
}






if($peoplequotes ne ''){
    print '<div class="row-fluid"> 
    <div class="span12">
    <div class="hero-unit">  <h2>People Quotes: <small>' . $query . '</small></h2><hr>';
    print $peoplequotes;

    if ($socialquotes eq '') {
        print '<p class="hero-unit">Computed by Harvix</p>';
        print '</div></div></div>';
    } else {
        print '</div></div></div>';
    }
    
}
if($socialquotes ne ''){
    print '<div class="row-fluid"> 
    <div class="span12">
    <div class="hero-unit">  <h2>Social Quotes: <small>' . $query . '</small></h2><hr>';
    print $socialquotes;

    #if ($peoplequotes eq '') {
        print '<p class="hero-unit">Computed by Harvix</p>';
        print '</div></div></div>';
    #} else {
        print '</div></div></div>';
    #}
}
if ($peoplequotes eq '' && $socialquotes eq '') {
    print '<h2>No Quotes</h2>';
}

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
                        background-color: #eeeeee;
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

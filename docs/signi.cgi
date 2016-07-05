#!/usr/bin/perl

use strict;
use Data::Dumper;


my %args;

foreach my $arg ( $ENV{QUERY_STRING} =~ /([^\&]+=[^\&]+)/g )
{
	my ( $var, $val ) = split(/=/, $arg );
	$args{$var}=$val;
}

my $user = $args{user};
my $password = $args{password};

$user = lc $user;

if ( $user !~ /^[a-z][a-z0-9]{1,14}$/ )
{
	print_header();
	print "<p>Sorry, Bad Username '$user'</p>\n";
	exit(0);
}


if ( ! -f "/home/david/harvix/users/$user" )
{
	print_header();
	print "<p>Sorry, No Such User.<p>\n";
	exit(0);
}

my $pass;

open(FILE, "</home/david/harvix/users/$user") or warn;
while ( my $line = <FILE> )
{
	chomp($line);

	if ( $line =~ /^password:(.*)$/ )
	{
		$pass = $1;
	}
}
close(FILE);

if ( $password ne $pass )
{
	print_header();
	print "Sorry, Wrong Password.<p>\n";
}
else
{
	print "Location: /?user=$user\r\n\r\n";
}

sub print_header
{

print "Content-type: text/html\n\n";
print <<EOF
<html>
<head>
<title>
Harvix Login
</title>
<link rel="stylesheet" href="/style.css" type="text/css">
<style type="text/css">

a:link {color:#1a54e1; text-decoration:none;}  
a:visited {color:#1a54e1; text-decoration:none;}
a:hover {color:#1a54e1; text-decoration:underline;}
body { font-size: 16px; font-family:  Arial, sans-serif; font-size: normal; line-height: normal; }



div.footer
{
color:#a0a0a0;
}

div.bar
{
float:right;
}

div.ex
{
width:50%;
padding:10px;
border:2px solid gray;
margin:0px;
-moz-border-radius: 15px;
border-radius: 15px;
background-color:;
}

div.ix
{
width:50%;
padding:10px;
border:1px black;
margin:0px;
-moz-border-radius: 15px;
border-radius: 15px;
background-color:red;
}



div.header{font-size:100px;}

</style>
</head>
<body>


<center>
<div class="header">
<span style="color:black;">Har</span><span style="color:#b31c1c;">vix</span>
</div>

<p>



<div class="ex">
Login To Harvix:
<p>
<form action="signi.cgi" method="get">
Username: <input size="40" name="user" value="">
<p>
Password: <input size="40" name="password" type="password"  value="">
<p>
<input type=submit value="sign in">
</form>

<a href="index.html">Cancel Login</a>
</div>
</center>
</body>
</html>

EOF
;


print "<p>\n";

#foreach my $k ( keys %ENV )
#{
#	print "$k: $ENV{$k}<br>\n";
#}

#print "<p>\n";
#print "username was $args{user}<p>\n";
#print "email was $args{email}<p>\n";
#print "password was $args{password}<p>\n";
#print "about was $args{about}<p>\n";
#print "<p>\n";

}


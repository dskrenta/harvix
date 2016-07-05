#!/usr/bin/perl

use strict;
use Data::Dumper;

#my $query;
#if ( $ENV{QUERY_STRING} =~ /\bq=([^\&\?]*)/ )
#{
#	$query = $1;
#}

my %args;


print "Content-type: text/html\n\n";
print <<EOF
<html>
<head>
<title>Harvix Signup</title>
<link rel="stylesheet" href="/style.css" type="text/css">
<style type="text/css">

div.footer
{
color:#a0a0a0;
}

div.bar
{
float:right;
}

</style>
</head>
<body>
<div class="bar">
<a href="index.html">home</a> &middot;  <a href="signi.html">sign in</a> &middot; <a href="signu.html">sign up</a>
</div>

<b>search bar:</b>  <a href="y2search.html">web</a> &middot; <a href="ysearch.html">images</a> &middot; <a href="search.html">jokes</a>
<hr></hr>

<img src="http://harvix.com/harvix-logo.png"/>

</body>
EOF
;


print "<p>\n";

foreach my $arg ( $ENV{QUERY_STRING} =~ /([^\&]+=[^\&]+)/g )
{
	my ( $var, $val ) = split(/=/, $arg );
	#if ( $ENV{QUERY_STRING} =~ /\bq=([^\&\?]*)/ )
	#QUERY_STRING: user=david&password=foo&email=email&about=hi
	$args{$var}=$val;
#	print "$var: $val<br>\n";
}


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


my $user = $args{user};
my $email = $args{email};
my $password = $args{password};
my $about = $args{about};
$email =~ s/%40/\@/g;

$user = lc $user;

if ( $user !~ /^[a-z][a-z0-9]{1,14}$/ )
{
	print "<p>Sorry, bad username. To go back and edit click the back button. <p>\n";
	exit(0);
}

if ( length($password) < 6 )
{
	print "<p>Sorry, bad password. To go back and edit click the back button. <p>\n";
	exit(0);
}


if ( $email !~ /.\@../ )
{
	print "<p>Sorry, bad email. To go back and edit click the back button. <p>\n";
	exit(0);
}

if ( -f "/home/david/harvix/users/$user" )
{
	print "<p>Sorry, user already exists. To go back and edit click the back button. <p>\n";
	exit(0);
}

else
{
print "Congragulations, $user you have just joined harvix.com now you are open to the privegles listed below:\n<p>
<p>
<ol>
<li>use hmail
<br>
<li>use chatvix
<br>
<li>use social search
<br>
<li>use all of harvix products with your new harvix acount.
<br>
<li>try out harvix beta.
</ol>
to login to your harvix acount, goto <a href=\"signi.html\">Sign in</a>
\n<p>";
}

print <<EOF
<div class="footer">
&copy; copyright 2010 &middot; <a href="privacy.html">privacy</a>
</div>

EOF
;

open(FILE, ">/home/david/harvix/users/$user") or warn;
print FILE "user:$user\n";
print FILE "email:$email\n";
print FILE "password:$password\n";
print FILE "about:$about\n";
close(FILE);

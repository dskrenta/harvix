#!/usr/bin/perl

# magic - do not change
print "Content-type: text/html\n\n";
$page = $ENV{QUERY_STRING} || shift || 1;
# end magic


if ( $page eq '1' )
{

	print "<title>*** WAR3.CGI/PERL ***</title>\n";

	
	print " greetings profesor skrenta\n";
	print "<p>\n";

	print "login: ";


	print "<h2>You are in the Maze</h2>\n";

	print "<a href=maze.cgi?2>go east</a>\n";
}


if ( $page eq '2' )
{

	print "<title>Maze Room 2</title>\n";

	print "<h1>You are in Maze Room 2</h1>\n";

	print "<a href=maze.cgi?1>back to room 1</a>\n";
}

#!/usr/bin/perl

#       Harvix Search DEV version 10.0
#       
#       Coppyright (C) 2013 Harvix Search
#       Designed and Built by David Skrenta CEO 
#       All Contents of File and Related Files are Protected by Harvix

use strict;
use JSON;
use URI::Fetch;
use Encode;
use Number::Spell;

my $catsort = {
	'WIKI'			=> 100,
	'ORIG'			=> 90,
	'IMAGE'			=> 80,
};


my %escapes;
setup_escapes();

my $query = parse_query();

print "Content-type: text/html\n\n";

print_header($query);

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

my $json_page = URI::Fetch->fetch("http://blekko.com/api/p1?q=$query&auth=c31c6fd0");
my $json_text = $json_page->content();
my $json = decode_json( $json_text );


if ( ! defined $json )
{
    print "no results\n";
    exit(0);
}

if ( ! defined $json->{tags} )
{
    print "no results\n";
    exit(0);
}

#print_header($query);

# foreach my $tag ( @{ $json->{tags} } )

my $elsecount = 1;

my $modalcount = 0;

foreach my $tag ( sort { $catsort->{ $b->{name} } <=> $catsort->{ $a->{name} } } @{ $json->{tags} } )
{
    	my $category = $tag->{name};
    	my $results = $tag->{results};

	#Spell Number
        my $numberspell = spell_number($modalcount);

	#TAGS + CATEGORIES 

	if($category eq "NAV")
	{
		#Display Nothing
	}	

	elsif($category eq "RETAIL")
	{
		#Display Nothing
	}

	elsif($category eq "WIKI")
	{
		my $wiki_count = 1;

       		foreach my $result ( @{ $results } )
        	{
			if ($wiki_count == 1)
			{
				#Declare Variables
                		my $title = $result->{'t'};
                		my $url = $result->{'u'};
                		my $rurl = $result->{'du'};
                		my $snippet = $result->{'ws'};
				my $img = $result->{'wi'};
		
				#Shorten Snippet
                		$snippet =~ s/<\/?(b|strong)>//g;
                		if ( length($snippet) > 500)
                		{
					$snippet = substr($snippet, 0, 500);
					$snippet =~ s/\s[^\s]*$//;
                       			$snippet .= '';
                		}		

				#Print Alongside HTML
				my $newwikihtml = qq{
					<!--Start WIKI Timline Section-->
					<li>
         		 		<div class="timeline-badge success"><i class="glyphicon glyphicon-info-sign"></i></div>
          				<div class="timeline-panel">
					<div class="media">
					<a class="pull-right" href="$img">
    					<img class="media-object img-rounded" src="$img" alt="" height="200px" onerror="this.style.display='none'" alt="$query Image">
  					</a>
					<div class="timeline-heading">
              				<h4 class="timeline-title"><a href="$url" target="_blank">$title</a></h4>
            				</div>
            				<div class="timeline-body">
              				<p>$snippet</p>
            				<p><small class="text-muted"><i class="glyphicon glyphicon-ok"></i> $rurl</small></p>
                                        <!--Like Dislike Flag-->
                                        <p>
                                        <div class="btn-group">
                                        <button type="button" class="btn btn-default" data-toggle="modal" data-target="#myNOTESModal"><i class="glyphicon glyphicon-pencil"></i></button>
                                        <button type="button" class="btn btn-default" data-toggle="modal" onClick='document.getElementById("iframeWIKI").src="$url";' data-target="#myWIKIModal"><i class="glyphicon glyphicon-fullscreen"></i></button>
                                        <button type="button" class="btn btn-default" data-toggle="modal" onClick='document.getElementById("iframeCITE").src="http://harvix.com/search/new/cite.cgi?u=$url";' data-target="#myCITEModal"><i class="glyphicon glyphicon-pushpin"></i></button>
				};
				print $newwikihtml;
				
				#open_form("Like", $title, $snippet, $url);
				#print('<button type="submit" class="btn btn-default"><i class="glyphicon glyphicon-thumbs-up"></i></button>');
                                #close_form();
				#open_form("Like", $title, $snippet, $url);
				#print('<button type="submit" class="btn btn-default"><i class="glyphicon glyphicon-thumbs-down"></i></button>');
				#close_form();
				#open_form("Like", $title, $snippet, $url);
                                #print('<button type="submit" class="btn btn-default"><i class="glyphicon glyphicon-flag"></i></button>');
                     		#close_form();

				my $redirect = qq{
					<a href="http://harvix.com/content.php?url=$url&title=$title&snippet=$snippet&type=like&query=$query" class="btn btn-default"><i class="glyphicon glyphicon-thumbs-up"></i></a>
					<a href="http://harvix.com/content.php?url=$url&title=$title&snippet=$snippet&type=dislike&query=$query" class="btn btn-default"><i class="glyphicon glyphicon-thumbs-down"></i></a>	
					<a href="http://harvix.com/content.php?url=$url&title=$title&snippet=$snippet&type=flag&query=$query" class="btn btn-default"><i class="glyphicon glyphicon-flag"></i></a>
				};
				print $redirect;
				

				my $print_wiki_2 = qq{
					</div>
                                        </p>
                                        <!--End Like Dislike Flag-->
					</div>
					<!--Modal WIKI Start-->
					<div class="modal fade" id="myWIKIModal" tabindex="-1" role="dialog" aria-labelledby="myWIKIModal" aria-hidden="true">
  					<div class="modal-dialog modal-lg">
    					<div class="modal-content">
 					<div class="modal-header">
        				<button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>
        				<h4 class="modal-title" id="myModalLabel">$title</h4>
      					</div>
      					<div class="modal-body">
      					<iframe id="iframeWIKI" height="500px" width="100%" frameborder="0"></iframe>
					</div>
    					</div>
 					</div>
					</div>
					<!--Modal WIKI End-->
					<!--Modal NOTES Start-->
                                        <div class="modal fade" id="myNOTESModal" tabindex="-1" role="dialog" aria-labelledby="myNOTESModal" aria-hidden="true">
                                        <div class="modal-dialog modal-lg">
                                        <div class="modal-content">
                                        <div class="modal-header">
                                        <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>
                                        <h4 class="modal-title" id="myModalLabel">Notes - $query</h4>
                                        </div>
                                        <div class="modal-body">
                                        <iframe src="http://harvix.com/search/new/notes/notes.html" height="500px" width="100%" frameborder="0"></iframe>
                                        </div>
                                        </div>
                                        </div>
                                        </div>
                                        <!--Modal NOTES End-->
					<!--Modal CITE Start-->
                                        <div class="modal fade" id="myCITEModal" tabindex="-1" role="dialog" aria-labelledby="myCITEModal" aria-hidden="true">
                                        <div class="modal-dialog modal-lg">
                                        <div class="modal-content">
                                        <div class="modal-header">
                                        <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>
                                        <h4 class="modal-title" id="myModalLabel">Citations</h4>
                                        </div>
                                        <div class="modal-body">
                                        <iframe id="iframeCITE" height="500px" width="100%" frameborder="0"></iframe>
					</div>
                                        </div>
                                        </div>
                                        </div>
                                        <!--Modal CITE End-->
					</div>
          				</div>
        				</li>
					<!--End WIKI Timeline Section-->
				};
				print $print_wiki_2;
			}

			else
			{
			}
			
			$wiki_count ++;
		}
	}
		
	elsif($category eq "ORIG")
        {
		my $count = 0;
		foreach my $result ( @{ $results } )
        	{
			#Declare Variables
                        my $title = $result->{'t'};
                       	my $url = $result->{'u'};
                        my $rurl = $result->{'du'};
                        my $snippet = $result->{'s'};
                        $snippet =~ s/<\/?(b|strong)>//g;
                        my $img_id = $result->{'i'};
                        my $img_data = $json->{img_map}->{$img_id};

                        #Shorten Snippet
                        if ( length($snippet) > 500 )
                        {
                        	$snippet = substr($snippet, 0, 500);
                               	$snippet =~ s/\s[^\s]*$//;
                            	$snippet .= ' ...';
                      	}
		
			if ($count <= 2)
			{
				#IMAGE
				if ( $img_data ne '' )
				{
					my $testhtml = qq{	
						<!--Start Web Result-->
						<li>
         					<div class="timeline-badge info"><i class="glyphicon glyphicon-bookmark"></i></div>
          					<div class="timeline-panel">
            					<div class="media">
                                        	<a class="pull-right" href="$img_data">
                                        	<img class="media-object img-rounded" src="$img_data" alt="" height="200px" onerror="this.style.display='none'" alt="$query Image">
                                        	</a>
						<div class="timeline-heading">
              					<h4 class="timeline-title"><a href="$url" target="_blank">$title</a></h4>
            					</div>
            					<div class="timeline-body">
            					<p>$snippet</p>
						<p><small class="text-muted"><i class="glyphicon glyphicon-ok"></i> $rurl</small></p>
						<!--Like Dislike Flag-->
						<p>
						<div class="btn-group">
						<button type="button" class="btn btn-default" data-toggle="modal" data-target="#myNOTESModal"><i class="glyphicon glyphicon-pencil"></i></button>
						<button type="button" class="btn btn-default" data-toggle="modal" data-target="#myWEBexpandModal$count" onClick='document.getElementById("WEBexpand$count").src="$url";'><i class="glyphicon glyphicon-fullscreen"></i></button>
  						<button type="button" class="btn btn-default" data-toggle="modal" onClick='document.getElementById("iframeCITE").src="http://harvix.com/search/new/cite.cgi?u=$url";' data-target="#myCITEModal"><i class="glyphicon glyphicon-pushpin"></i></button>
						<a href="http://harvix.com/content.php?url=$url&title=$title&snippet=$snippet&type=like&query=$query" class="btn btn-default"><i class="glyphicon glyphicon-thumbs-up"></i></a>
                                        	<a href="http://harvix.com/content.php?url=$url&title=$title&snippet=$snippet&type=dislike&query=$query" class="btn btn-default"><i class="glyphicon glyphicon-thumbs-down"></i></a>    
                                        	<a href="http://harvix.com/content.php?url=$url&title=$title&snippet=$snippet&type=flag&query=$query" class="btn btn-default"><i class="glyphicon glyphicon-flag"></i></a>
						<button type="button" class="btn btn-primary" data-toggle="modal" data-target="#myORIGModal"><i class="glyphicon glyphicon-fullscreen"></i> Web</button>
						</div>
						</p>
						<!--End Like Dislike Flag-->
						</div>
						</div>
          					</div>
        					</li>
						<!--End Web Result-->
						<!--Modal Web Expand Start-->
                                        	<div class="modal fade" id="myWEBexpandModal$count" tabindex="-1" role="dialog" aria-labelledby="myWEBexpandModal$count" aria-hidden="true">
                                        	<div class="modal-dialog modal-lg">
                                        	<div class="modal-content">
                                        	<div class="modal-header">
                                        	<button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>
                                        	<h4 class="modal-title" id="myModalLabel">$title</h4>
                                        	</div>
                                        	<div class="modal-body">
                                        	<iframe id="WEBexpand$count" height="500px" width="100%" frameborder="0"></iframe>
                                        	</div>
                                        	</div>
                                        	</div>
                                        	</div>
                                        	<!--Modal Web Expand End-->
					};
					print $testhtml;
				}
			
				#NO IMAGE
				else
				{
					my $testhtml = qq{      
                                                <!--Start Web Result-->
                                                <li>
                                                <div class="timeline-badge info"><i class="glyphicon glyphicon-bookmark"></i></div>
                                                <div class="timeline-panel">
                                                <div class="media">
                                                <a class="pull-right" href="$img_data">
                                                <img class="media-object img-rounded" src="$img_data" alt="" height="200px" onerror="this.style.display='none'" alt="$query Image">
                                                </a>
                                                <div class="timeline-heading">
                                                <h4 class="timeline-title"><a href="$url" target="_blank">$title</a></h4>
                                                </div>
                                                <div class="timeline-body">
                                                <p>$snippet</p>
                                                <p><small class="text-muted"><i class="glyphicon glyphicon-ok"></i> $rurl</small></p>
                                                <!--Like Dislike Flag-->
                                                <p>
                                                <div class="btn-group">
                                                <button type="button" class="btn btn-default" data-toggle="modal" data-target="#myNOTESModal"><i class="glyphicon glyphicon-pencil"></i></button>
                                                <button type="button" class="btn btn-default" data-toggle="modal" data-target="#myWEBexpandModal$count" onClick='document.getElementById("WEBexpand$count").src="$url";'><i class="glyphicon glyphicon-fullscreen"></i></button>
						<button type="button" class="btn btn-default" data-toggle="modal" onClick='document.getElementById("iframeCITE").src="http://harvix.com/search/new/cite.cgi?u=$url";' data-target="#myCITEModal"><i class="glyphicon glyphicon-pushpin"></i></button>
                                                <a href="http://harvix.com/content.php?url=$url&title=$title&snippet=$snippet&type=like&query=$query" class="btn btn-default"><i class="glyphicon glyphicon-thumbs-up"></i></a>
                                        	<a href="http://harvix.com/content.php?url=$url&title=$title&snippet=$snippet&type=dislike&query=$query" class="btn btn-default"><i class="glyphicon glyphicon-thumbs-down"></i></a>    
                                        	<a href="http://harvix.com/content.php?url=$url&title=$title&snippet=$snippet&type=flag&query=$query" class="btn btn-default"><i class="glyphicon glyphicon-flag"></i></a>
						<button type="button" class="btn btn-primary" data-toggle="modal" data-target="#myORIGModal"><i class="glyphicon glyphicon-fullscreen"></i> Web</button>
                                                </div>
                                                </p>
                                                <!--End Like Dislike Flag-->
                                                </div>
                                                </div>
                                                </div>
                                                </li>
                                                <!--End Web Result-->
                                                <!--Modal Web Expand Start-->
                                                <div class="modal fade" id="myWEBexpandModal$count" tabindex="-1" role="dialog" aria-labelledby="myWEBexpandModal$count" aria-hidden="true">
                                                <div class="modal-dialog modal-lg">
                                                <div class="modal-content">
                                                <div class="modal-header">
                                                <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>
                                                <h4 class="modal-title" id="myModalLabel">$title</h4>
                                                </div>
                                                <div class="modal-body">
                                                <iframe id="WEBexpand$count" height="500px" width="100%" frameborder="0"></iframe>
                                                </div>
                                                </div>
                                                </div>
                                                </div>
                                                <!--Modal Web Expand End-->
                                        };
					print $testhtml;
				}
			
			}
				
			else
			{
				if ($count == 3)
				{	
					my $ORIGModalhtml = qq{
						<!--Modal ORIG Start-->
                                       	 	<div class="modal fade" id="myORIGModal" tabindex="-1" role="dialog" aria-labelledby="myORIGModal" aria-hidden="true">
                                       		<div class="modal-dialog modal-lg">
                                        	<div class="modal-content">
                                        	<div class="modal-header">
                                        	<button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>
                                        	<h4 class="modal-title" id="myModalLabel">Web Results - $query</h4>
                                       	 	</div>
                                        	<div class="modal-body">
						<!--Start ORIG Content-->
						<!--Start ORIG Result-->
						<div class="well">
						<div class="media">
  						<a class="pull-left" href="#">
 					   	<img class="media-object" src="" alt="">
  						</a>
  						<div class="media-body">
    						<h4 class="media-heading">$title</h4>
    						<p>$snippet</p>
						<p><small class="text-muted"><i class="glyphicon glyphicon-ok"></i> $rurl</small></p>
                                                <!--Like Dislike Flag-->
                                                <p>
                                                <div class="btn-group">
						<a href="http://harvix.com/search/new/notes/notes.html" target="_blank" class="btn btn-default"><i class="glyphicon glyphicon-pencil"></i></a>
						<a href="$url" target="_blank" class="btn btn-default"><i class="glyphicon glyphicon-fullscreen"></i></a>
                                                <a href="http://harvix.com/search/new/cite.cgi?u=$url" target="_blank" class="btn btn-default"><i class="glyphicon glyphicon-pushpin"></i></a>
						<a href="http://harvix.com/content.php?url=$url&title=$title&snippet=$snippet&type=like&query=$query" class="btn btn-default"><i class="glyphicon glyphicon-thumbs-up"></i></a>
                                        	<a href="http://harvix.com/content.php?url=$url&title=$title&snippet=$snippet&type=dislike&query=$query" class="btn btn-default"><i class="glyphicon glyphicon-thumbs-down"></i></a>    
                                        	<a href="http://harvix.com/content.php?url=$url&title=$title&snippet=$snippet&type=flag&query=$query" class="btn btn-default"><i class="glyphicon glyphicon-flag"></i></a>
						</div>
                                                </p>
                                                <!--End Like Dislike Flag-->
  						</div>
						</div>
						</div>
						<!--End ORIG Result-->
					};
					print $ORIGModalhtml;
				}
				
				else
				{
					my $ORIGModalhtmlv2 = qq{
						<!--Start ORIG Result-->
                                        	<div class="well">
						<div class="media">
                                       		<a class="pull-left" href="#">
                                        	<img class="media-object" src="" alt="">
                                        	</a>
                                        	<div class="media-body">
                                        	<h4 class="media-heading"><a href="$url" target="_blank">$title</a></h4>
                                        	<p>$snippet</p>
						<p><small class="text-muted"><i class="glyphicon glyphicon-ok"></i> $rurl</small></p>
                                                <!--Like Dislike Flag-->
                                                <p>
                                                <div class="btn-group">
						<a href="http://harvix.com/search/new/notes/notes.html" target="_blank" class="btn btn-default"><i class="glyphicon glyphicon-pencil"></i></a>
                                                <a href="$url" target="_blank" class="btn btn-default"><i class="glyphicon glyphicon-fullscreen"></i></a>
                                                <a href="http://harvix.com/search/new/cite.cgi?u=$url" target="_blank" class="btn btn-default"><i class="glyphicon glyphicon-pushpin"></i></a>
                                                <a href="http://harvix.com/content.php?url=$url&title=$title&snippet=$snippet&type=like&query=$query" class="btn btn-default"><i class="glyphicon glyphicon-thumbs-up"></i></a>
                                        	<a href="http://harvix.com/content.php?url=$url&title=$title&snippet=$snippet&type=dislike&query=$query" class="btn btn-default"><i class="glyphicon glyphicon-thumbs-down"></i></a>    
                                        	<a href="http://harvix.com/content.php?url=$url&title=$title&snippet=$snippet&type=flag&query=$query" class="btn btn-default"><i class="glyphicon glyphicon-flag"></i></a>
						</div>
                                                </p>
                                                <!--End Like Dislike Flag-->
                                        	</div>
                                       		</div>
                                       		<!--End ORIG Result-->	
						</div>
					};
					print $ORIGModalhtmlv2;
				}
			}
			$count ++
        	}
		my $ORIGModalhtmlv3 = qq{
			<!--End ORIG Content-->
			</div>
                	</div>
                        </div>
                        </div>
                        <!--Modal ORIG End-->
			<!--Modal NOTES Start-->
                        <div class="modal fade" id="myNOTESModal" tabindex="-1" role="dialog" aria-labelledby="myNOTESModal" aria-hidden="true">
                        <div class="modal-dialog modal-lg">
                      	<div class="modal-content">
                       	<div class="modal-header">
                     	<button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>
                      	<h4 class="modal-title" id="myModalLabel">Notes - $query</h4>
                   	</div>
                     	<div class="modal-body">
                   	<iframe src="http://harvix.com/search/new/notes/notes.html" height="500px" width="100%" frameborder="0"></iframe>
                       	</div>
                      	</div>
                       	</div>
                        </div>
                      	<!--Modal NOTES End-->
                       	<!--Modal CITE Start-->
                       	<div class="modal fade" id="myCITEModal" tabindex="-1" role="dialog" aria-labelledby="myCITEModal" aria-hidden="true">
                       	<div class="modal-dialog modal-lg">
                       	<div class="modal-content">
                      	<div class="modal-header">
                    	<button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>
                      	<h4 class="modal-title" id="myModalLabel">Citations</h4>
                     	</div>
                        <div class="modal-body">
                      	<iframe id="iframeCITE" height="500px" width="100%" frameborder="0"></iframe>
                      	</div>
                        </div>
                        </div>
                        </div>
                        <!--Modal CITE End-->
		};
		print $ORIGModalhtmlv3;
			
		my $ORIGhtml = qq{
			<!--Start Wolf-->
                        <li>
                        <div class="timeline-badge danger"><i class="glyphicon glyphicon-tasks"></i></div>
                        <div class="timeline-panel">
                        <div class="timeline-body">
                        <p><div style=\"background: #ffffff url(http://www.domaine-saint-pierre.fr/skin/frontend/default/default/images/home/loading.gif) no-repeat 50% 5%;\">
                        <iframe src="http://harvix.com/wolf.cgi?$query" allowTransparency="true"  width="100%" height="300px" frameborder="0"></iframe></p>
                        </div>
                        </div>
                        </li>
                      	<!--End Wolf-->
                        <!--Start Facts-->
                        <li class="timeline-inverted">
                       	<div class="timeline-badge warning"><i class="glyphicon glyphicon-list"></i></div>
                        <div class="timeline-panel">
                        <div class="timeline-heading">
                        </div>
                        <div class="timeline-body">
                        <p><iframe src="http://harvix.com/facts_search.cgi?$query" width="100%" height="310px" class="restricted" overflow-y="hidden" frameborder="0"></iframe></p>
                        </div>
                        </div>
                        </li>
                      	<!--End Facts-->
		};
		print $ORIGhtml;
        }

	elsif($category eq "IMAGE")
	{
		#Print Before Alongside HTML            
                my $before = qq{
			<li class="timeline-inverted">
                        <div class="timeline-badge danger"><i class="glyphicon glyphicon-picture"></i></div>
                        <div class="timeline-panel">
                        <div class="timeline-heading">
                        </div>
                        <div class="timeline-body">
                        <p>
                        <div id="scrollable">
                        <div id="items">        
                };
                print $before;

                foreach my $result ( @{ $results } )
                {
                        #Declare Variable
                        my $url = $result->{'u'};
				
			#Print Alongside IMG HTML
			my $imagehtml = qq{
				<div class="item">
				<a href="$url" target="_blank">
				<img src="$url" height="280px" alt="$url" onerror="this.style.display='none'"></img>
				</a>
				</div>
			};
			print $imagehtml;	
                }
		
		#Print After Alongside HTML
                my $after = qq{
                	</div>
			</div>
		        </p>
                        <!--Like Dislike Flag-->
                        <!--
			<p>
                        <div class="btn-group">                                	
			<button type="button" class="btn btn-default" data-toggle="modal" data-target="#myNOTESModal"><i class="glyphicon glyphicon-pencil"></i></button>
                        <button type="button" class="btn btn-default"><i class="glyphicon glyphicon-fullscreen"></i></button>
			<button type="button" class="btn btn-primary" data-toggle="modal" data-target="#myIMGModal"><i class="glyphicon glyphicon-fullscreen"></i> Images</button>
                        </div>
                        </p>
			-->
                       	<!--End Like Dislike Flag-->
                        </div>
                        </div>
                        </li>
                };
                print $after;
        }
	
        else
        {
		my $rescount = 1;

		my $modal_count = 0;

        	foreach my $result ( @{ $results } )
        	{
                	#Define Variables
			my $title = $result->{'t'};
                	my $url = $result->{'u'};
               		my $rurl = $result->{'du'};
               		my $snippet = $result->{'s'};
                	$snippet =~ s/<\/?(b|strong)>//g;
			my $img_id = $result->{'i'};
                        my $img_data = $json->{img_map}->{$img_id};              
  
			#Shorten Snippet
			if ( length($snippet) > 150 )
                	{
                        	$snippet = substr($snippet, 0, 150);
                        	$snippet =~ s/\s[^\s]*$//;
                        	$snippet .= ' ...';
                	}
			
			if ($rescount == 1)
			{
				my $num = $modalcount;
				if ( $img_data ne '' )
				{
					my $printone = qq{
						<li class="timeline-inverted">
                                       		<div class="timeline-badge success"><i class="glyphicon glyphicon-tag"></i></div>
                                       		<div class="timeline-panel">
                                       		<div class="media">
                                                <a class="pull-right" href="$img_data">
                                                <img class="media-object img-rounded" src="$img_data" alt="" height="200px" onerror="this.style.display='none'" alt="$query Image">
                                                </a>
						<div class="timeline-heading">
                                       		<h4 class="timeline-title"><a href="$url" target="_blank">$title</a></h4>
                                       		</div>
                                       		<div class="timeline-body">
                                       		<p>$snippet</p>
                                       		<p><small class="text-muted"><i class="glyphicon glyphicon-ok"></i> $rurl</small></p>
                                       		<!--Like Dislike Flag-->
                                       		<p>
                                       		<div class="btn-group">
                                       		<button type="button" class="btn btn-default" data-toggle="modal" data-target="#myNOTESModal"><i class="glyphicon glyphicon-pencil"></i></button>
                                       		<button type="button" class="btn btn-default" data-toggle="modal" data-target="#modalexpand$num" onClick='document.getElementById("frame$num").src="$url";'><i class="glyphicon glyphicon-fullscreen"></i></button>
                                       		<button type="button" class="btn btn-default" data-toggle="modal" onClick='document.getElementById("iframeCITE").src="http://harvix.com/search/new/cite.cgi?u=$url";' data-target="#myCITEModal"><i class="glyphicon glyphicon-pushpin"></i></button>
                                       		<a href="http://harvix.com/content.php?url=$url&title=$title&snippet=$snippet&type=like&query=$query" class="btn btn-default"><i class="glyphicon glyphicon-thumbs-up"></i></a>
                                        	<a href="http://harvix.com/content.php?url=$url&title=$title&snippet=$snippet&type=dislike&query=$query" class="btn btn-default"><i class="glyphicon glyphicon-thumbs-down"></i></a>    
                                        	<a href="http://harvix.com/content.php?url=$url&title=$title&snippet=$snippet&type=flag&query=$query" class="btn btn-default"><i class="glyphicon glyphicon-flag"></i></a>
						<button type="button" class="btn btn-primary" data-toggle="modal" data-target="#myELSEModalNUM$numberspell"><i class="glyphicon glyphicon-fullscreen"></i> $category</button>

                                       		</div>
                                       		</p>
                                       		<!--End Like Dislike Flag-->
						</div>
						</div>
                                       		</div>
                                       		</li>
					};
					print $printone;
				}
	
				else
				{
					my $printtwo = qq{
                                                <li class="timeline-inverted">
                                                <div class="timeline-badge success"><i class="glyphicon glyphicon-tag"></i></div>
                                                <div class="timeline-panel">
                                                <div class="timeline-heading">
                                                <h4 class="timeline-title"><a href="$url" target="_blank">$title</a></h4>
                                                </div>
                                                <div class="timeline-body">
                                                <p>$snippet</p>
                                                <p><small class="text-muted"><i class="glyphicon glyphicon-ok"></i> $rurl</small></p>
                                                <!--Like Dislike Flag-->
                                                <p>
                                                <div class="btn-group">
                                                <button type="button" class="btn btn-default" data-toggle="modal" data-target="#myNOTESModal"><i class="glyphicon glyphicon-pencil"></i></button>
                                                <button type="button" class="btn btn-default" data-toggle="modal" data-target="#modalexpand$num" onClick='document.getElementById("frame$num").src="$url";'><i class="glyphicon glyphicon-fullscreen"></i></button>
                                                <button type="button" class="btn btn-default" data-toggle="modal" onClick='document.getElementById("iframeCITE").src="http://harvix.com/search/new/cite.cgi?u=$url";' data-target="#myCITEModal"><i class="glyphicon glyphicon-pushpin"></i></button>
                                                <a href="http://harvix.com/content.php?url=$url&title=$title&snippet=$snippet&type=like&query=$query" class="btn btn-default"><i class="glyphicon glyphicon-thumbs-up"></i></a>
                                        	<a href="http://harvix.com/content.php?url=$url&title=$title&snippet=$snippet&type=dislike&query=$query" class="btn btn-default"><i class="glyphicon glyphicon-thumbs-down"></i></a>    
                                        	<a href="http://harvix.com/content.php?url=$url&title=$title&snippet=$snippet&type=flag&query=$query" class="btn btn-default"><i class="glyphicon glyphicon-flag"></i></a>
						<button type="button" class="btn btn-primary" data-toggle="modal" data-target="#myELSEModalNUM$numberspell"><i class="glyphicon glyphicon-fullscreen"></i> $category</button>
                                                </div>
                                                </p>
                                                <!--End Like Dislike Flag-->
                                                </div>
                                                </div>
                                                </li>
                                        };
                                        print $printtwo;
				}
				show_modal($num, $title);
				$modal_count++;
			}
			
			else
			{
				if ($rescount == 2)
				{
					my $ELSEModalhtml = qq{
                                                <!--Modal ELSE Start-->
                                                <div class="modal fade" id="myELSEModalNUM$numberspell" tabindex="-1" role="dialog" aria-labelledby="myELSEModalNUM$numberspell" aria-hidden="true">
                                                <div class="modal-dialog modal-lg">
                                                <div class="modal-content">
                                                <div class="modal-header">
                                                <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>
                                                <h4 class="modal-title" id="myModalLabel">$category results - $query</h4>
                                                </div>
                                                <div class="modal-body">
                                                <!--Start ELSE Content-->
                                                <!--Start ELSE Result-->
                                                <div class="well">
                                                <div class="media">
                                                <a class="pull-left" href="#">
                                                <img class="media-object" src="" alt="">
                                                </a>
                                                <div class="media-body">
                                                <h4 class="media-heading"><a href="$url" target="_blank">$title</a></h4>
                                                <p>$snippet</p>
                                                <p><small class="text-muted"><i class="glyphicon glyphicon-ok"></i> $rurl</small></p>
                                                <!--Like Dislike Flag-->
                                                <p>
                                                <div class="btn-group">
						<a href="http://harvix.com/search/new/notes/notes.html" target="_blank" class="btn btn-default"><i class="glyphicon glyphicon-pencil"></i></a>
                                                <a href="$url" target="_blank" class="btn btn-default"><i class="glyphicon glyphicon-fullscreen"></i></a>
                                                <a href="http://harvix.com/search/new/cite.cgi?u=$url" target="_blank" class="btn btn-default"><i class="glyphicon glyphicon-pushpin"></i></a>
                                                <a href="http://harvix.com/content.php?url=$url&title=$title&snippet=$snippet&type=like&query=$query" class="btn btn-default"><i class="glyphicon glyphicon-thumbs-up"></i></a>
                                        	<a href="http://harvix.com/content.php?url=$url&title=$title&snippet=$snippet&type=dislike&query=$query" class="btn btn-default"><i class="glyphicon glyphicon-thumbs-down"></i></a>    
                                        	<a href="http://harvix.com/content.php?url=$url&title=$title&snippet=$snippet&type=flag&query=$query" class="btn btn-default"><i class="glyphicon glyphicon-flag"></i></a>
						</div>
                                                </p>
                                                <!--End Like Dislike Flag-->
                                                </div>
                                                </div>
                                                </div>
                                                <!--End ELSE Result-->
                                        };
                                        print $ELSEModalhtml;
				}

				else
				{
					my $ELSEModalhtmlv2 = qq{
                                                <!--Start ELSE Result-->
                                                <div class="well">
                                                <div class="media">
                                                <a class="pull-left" href="#">
                                                <img class="media-object" src="" alt="">
                                                </a>
                                                <div class="media-body">
                                                <h4 class="media-heading"><a href="$url" target="_blank">$title</a></h4>
                                                <p>$snippet</p>
                                                <p><small class="text-muted"><i class="glyphicon glyphicon-ok"></i> $rurl</small></p>
                                                <!--Like Dislike Flag-->
                                                <p>
                                                <div class="btn-group">
						<a href="http://harvix.com/search/new/notes/notes.html" target="_blank" class="btn btn-default"><i class="glyphicon glyphicon-pencil"></i></a>
                                                <a href="$url" target="_blank" class="btn btn-default"><i class="glyphicon glyphicon-fullscreen"></i></a>
                                                <a href="http://harvix.com/search/new/cite.cgi?u=$url" target="_blank" class="btn btn-default"><i class="glyphicon glyphicon-pushpin"></i></a>
                                                <a href="http://harvix.com/content.php?url=$url&title=$title&snippet=$snippet&type=like&query=$query" class="btn btn-default"><i class="glyphicon glyphicon-thumbs-up"></i></a>
                                        	<a href="http://harvix.com/content.php?url=$url&title=$title&snippet=$snippet&type=dislike&query=$query" class="btn btn-default"><i class="glyphicon glyphicon-thumbs-down"></i></a>    
                                        	<a href="http://harvix.com/content.php?url=$url&title=$title&snippet=$snippet&type=flag&query=$query" class="btn btn-default"><i class="glyphicon glyphicon-flag"></i></a>
						</div>
                                                </p>
                                                <!--End Like Dislike Flag-->
                                                </div>
                                                </div>
                                                <!--End ELSE Result-->  
                                                </div>
                                        };
                                        print $ELSEModalhtmlv2;	
				}
			}

			$rescount ++;
       		}
		$elsecount ++;
		
		 my $ELSEModalhtmlv3 = qq{
                        <!--End ELSE Content-->
                        </div>
                        </div>
                        </div>
                        </div>
                	<!--Modal ELSE End-->
               	};
                print $ELSEModalhtmlv3;
	}     
	$modalcount ++; 
}

print_footer();

#SUBS

sub open_form
{
	my ($type, $title, $snippet, $url) = (@_);
	my $form_open_html = qq{
		<form action="http://harvix.com/content.php" method="post">
		<input type="hidden" name="page_url" value="http://harvix.com/search/new/dev5.cgi?q=$query"\>
		<input type="hidden" name="type" value="$type"\>
		<input type="hidden" name="title" value="$title"\>
		<input type="hidden" name="snippet" value="$snippet"\>
		<input type="hidden" name="url" value="$url"\>
		<input type="hidden" name="query" value="$query"\>
	};
	print $form_open_html;

}

sub close_form
{
	my $form_close_html = qq{
		</form>
	};
	print $form_close_html;
}

sub print
{
	my ($html_for_print) = (@_);
	my $html_print = qq{$html_for_print};
	print $html_print;
}

sub show_modal
{
	my ($num, $title) = (@_);
	my $print_modal = qq{
		<!--Modal Else Expand Start-->
     		<div class="modal fade" id="modalexpand$modalcount" tabindex="-1" role="dialog" aria-labelledby="modalexpand$modalcount" aria-hidden="true">
                <div class="modal-dialog modal-lg">
              	<div class="modal-content">
             	<div class="modal-header">
          	<button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>
              	<h4 class="modal-title" id="myModalLabel">$title</h4>
                </div>
              	<div class="modal-body">
              	<iframe id="frame$modalcount" height="500px" width="100%" frameborder="0"></iframe>
            	</div>
               	</div>
              	</div>
             	</div>
             	<!--Modal Else Expand End-->
	};
	print $print_modal;
}


sub print_header
{
	my ( $query ) = @_;

	$query =~ s/[<>\&]//g;

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
    <title>Harvix | $query</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Harvix Search Results for: $query">
    <meta name="author" content="Harvix Search">

    <!-- Harvix Search Page Styles -->
    <link href="http://harvix.com/search/css2/bootstrap.css" rel="stylesheet">
    <link href="http://harvix.com/search/css2/timeline4.css" rel="stylesheet">
    <link href="http://harvix.com/search/css2/top-nav2.css" rel="stylesheet">

    <!-- Harvix Fav and Touch Icons / Mobile Icons -->
    <link rel="apple-touch-icon-precomposed" sizes="144x144" href="http://www.harvix.com/images/harvixshort2.jpg">
    <link rel="apple-touch-icon-precomposed" sizes="114x114" href="http://www.harvix.com/images/harvixshort2.jpg">
    <link rel="apple-touch-icon-precomposed" sizes="72x72" href="http://www.harvix.com/images/harvixshort2.jpg">
    <link rel="apple-touch-icon-precomposed" href="http://www.harvix.com/images/harvixshort2.jpg">
    <link rel="shortcut icon" href="http://www.harvix.com/images/harvixshort2.jpg">
 
    <!--Onpage Style-->
    <style>
a:link {text-decoration:none; color:#333;}      /* unvisited link */
a:visited {text-decoration:none; color:#333;}  /* visited link */
a:hover {text-decoration:none; color:#333;}  /* mouse over link */
a:active {text-decoration:none; color:#333;}  /* selected link */

      
    .glyphicon {
       top:2px;
    }
      
    #scrollable {
       overflow: overlay;
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
     height:200px;
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
    </style>
    
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

  <body style="background-image: url('http://1.bp.blogspot.com/-kSjPlU-wY9E/UK9PymRJV6I/AAAAAAAADh0/tCrD_Bn7UqI/s1600/body.png')">

<div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
      <div class="container-fluid">
        <div class="navbar-header">
          <a class="navbar-brand" href="http://harvix.com">Harvix</a>
        </div>
        <div class="navbar-collapse collapse">
          <form class="navbar-form">
            <input type="text" class="form-control" action="http://harvix.com/search/new/mst3kv2.cgi" onsubmit="submitted('h'); return false" name="q"  class="search-query" value="$query">
	    <button type="submit" class="btn"><strong>Search</strong></button>
          </form>
        </div>
      </div>
    </div>

<div class="container">

<div class="page-header">
</div>

<ul class="timeline">

<!-- START DYNAMIC CGI -->

EOF
;
}

sub print_footer
{
print <<EOX

<!-- END DYNAMIC CGI -->

</ul>

</div>

<!--Javascript-->
<script src="http://harvix.com/search/new/js/bootstrap.js"></script>
<script src="http://harvix.com/search/new/js/jquery.js"></script>
<script src="http://harvix.com/search/new/js/modal.js"></script>

</body>
</html>

EOX
;
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


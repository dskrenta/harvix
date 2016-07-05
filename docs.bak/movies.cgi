        #!/usr/bin/perl -w

        use strict;
        use warnings;

        use WWW::Yahoo::Movies;

        my $title = shift || 'troy';

        my $matched = get_movie_info($title, 1);

        for(@$matched) {
                print "\nGet [$_->{title}] ...\n";
                get_movie_info($_->{id});
        }

        sub get_movie_info {
                my $title = shift;
                my $ret_match = shift || 0;
                
                my $ym = new WWW::Yahoo::Movies(id => $title);

                print "Get info about [$title] ...";

                print "\n\tID: ".$ym->id;
                print "\n\tTITLE: ".$ym->title;
                print "\n\tYEAR: ".$ym->year;
                print "\n\tMPAA: ".$ym->mpaa_rating;
                print "\n\tCOVER: ".$ym->cover_file;
                print "\n\tPLOT: ".substr($ym->plot_summary, 0, 90)." ...";
                print "\n\tDATE: ".$ym->release_date;
                print "\n\tDISTR: ".$ym->distributor;
                print "\n\tGENRES: ".join(", ", @{ $ym->genres }) if $ym->genres;

                return $ym->matched if $ret_match;
        }       

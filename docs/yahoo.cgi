#!/usr/bin/perl

use Yahoo::Search;
my @Results = Yahoo::Search->Results(Doc => "Britney latest marriage",
                                     AppId => "YahooDemo",
                                     # The following args are optional.
                                     # (Values shown are package defaults).
                                     Mode         => 'all', # all words
                                     Start        => 0,
                                     Count        => 10,
                                     Type         => 'any', # all types
                                     AllowAdult   => 0, # no porn, please
                                     AllowSimilar => 0, # no dups, please
                                     Language     => undef,
                                    );
warn $@ if $@; # report any errors

for my $Result (@Results)
{
    printf "Result: #%d\n",  $Result->I + 1,
    printf "Url:%s\n",       $Result->Url;
    printf "%s\n",           $Result->ClickUrl;
    printf "Summary: %s\n",  $Result->Summary;
    printf "Title: %s\n",    $Result->Title;
    printf "In Cache: %s\n", $Result->CacheUrl;
    print "\n";
 }

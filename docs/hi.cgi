#!/usr/bin/perl

use strict;

use Net::WolframAlpha;
use Data::Dumper;

my $query = shift(@ARGV);
$query = 'Pi' if $query eq '';


my $wa = Net::WolframAlpha->new (
    appid => '3EP4EG-Q7UKGAPR4Q',
);

my $query = $wa->query(
    input => $query,
);

if ($query->success) {

    foreach my $pod (@{$query->pods}) {
        print_pod($pod);
        #print Dumper($pod);
    }
}


sub print_pod
{
    my ( $pod ) = @_;

    return if !defined $pod->{title};
    return if !defined $pod->{subpods};

    print $pod->{title}, ":\n";

    foreach my $subpod ( @{ $pod->{subpods} } )
    {
        next if !defined $subpod->{plaintext};
        if ( defined $subpod->{img} )
        {
            print "    ", $subpod->{img}, "\n";
        }

        my $s = $subpod->{plaintext};
        $s =~ s/\n/\n    /gs;
        print "    ", $s, "\n";
    }
    print "\n";
}

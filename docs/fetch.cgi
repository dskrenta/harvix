use URI::Fetch;
use Data::Dumper;

    my $res = URI::Fetch->fetch('http://harvix.com/')
        or die URI::Fetch->errstr;

print Dumper($res);

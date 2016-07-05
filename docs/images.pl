use Bing::Search;
use Bing::Search::Result::Image

    my $search = Bing::Search->new();

    $search->AppId('RhGHTGRwo6St1qHhcKQXmNoBnJVpF0bkFYXM0Z0GmUM=');

    $search->Query('rocks');

    $search->add_source( 
      Bing::Search::Result::Image->new
    );

    my $response = $search->search();

    foreach my $result ( @{$response->results} ) { 
      print $result->Title, " -> ", $result->Url, "\n";
    }

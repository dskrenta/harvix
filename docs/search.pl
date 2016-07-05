#!/usr/bin/perl

use WWW::WolframAlpha;

  my $wa = WWW::WolframAlpha->new (
    appid => '3EP4EG-VWH9LJ5658',
  );

  my $query = $wa->query(
    input => 'pokemon',
  );

  if ($query->success) {
    foreach my $pod (@{$query->pods}) {     
      ...
    }
  }

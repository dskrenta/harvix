  #!/usr/bin/perl
  use warnings;
  use strict;

  use Amazon::S3;
  
  use vars qw/$OWNER_ID $OWNER_DISPLAYNAME/;
  
  my $aws_access_key_id     = "Fill me in!";
  my $aws_secret_access_key = "Fill me in too!";
  
  my $s3 = Amazon::S3->new(
      {   aws_access_key_id     => $aws_access_key_id,
          aws_secret_access_key => $aws_secret_access_key,
          retry                 => 1
      }
  );
  
  my $response = $s3->buckets;
  
  # create a bucket
  my $bucket_name = $aws_access_key_id . '-net-amazon-s3-test';
  my $bucket = $s3->add_bucket( { bucket => $bucket_name } )
      or die $s3->err . ": " . $s3->errstr;
  
  # store a key with a content-type and some optional metadata
  my $keyname = 'testing.txt';
  my $value   = 'T';
  $bucket->add_key(
      $keyname, $value,
      {   content_type        => 'text/plain',
          'x-amz-meta-colour' => 'orange',
      }
  );
  
  # list keys in the bucket
  $response = $bucket->list
      or die $s3->err . ": " . $s3->errstr;
  print $response->{bucket}."\n";
  for my $key (@{ $response->{keys} }) {
        print "\t".$key->{key}."\n";  
  }

  # delete key from bucket
  $bucket->delete_key($keyname);
  
  # delete bucket
  $bucket->delete_bucket;

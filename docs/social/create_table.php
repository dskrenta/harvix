<?php
// Create connection
$con=mysqli_connect("localhost","wordpress","dtechblog777","wordpress");

// Check connection
if (mysqli_connect_errno($con))
  {
  echo "Failed to connect to MySQL: " . mysqli_connect_error();
  }

// Create table
$sql="CREATE TABLE harvixtest(
id int(4) NOT NULL auto_increment,
username varchar(65) NOT NULL default '',
password varchar(65) NOT NULL default '',
PRIMARY KEY (`id`)
)
TYPE=MyISAM AUTO_INCREMENT=2 ;
";


// Execute query
if (mysqli_query($con,$sql))
  {
  echo "Table harvixtest created successfully";
  }
else
  {
  echo "Error creating table: " . mysqli_error($con);
  }

?>

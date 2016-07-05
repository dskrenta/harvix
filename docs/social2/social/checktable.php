<?php
$host="localhost"; // Host name 
$username="wordpress"; // Mysql username 
$password="dtechblog777"; // Mysql password 
$db_name="wordpress"; // Database name 
$tbl_name="harvixtest"; // Table name 

// Connect to server and select databse.
mysql_connect("$host", "$username", "$password")or die("cannot connect");
mysql_select_db("$db_name")or die("cannot select DB");

$result = mysqli_query($con,"SELECT * FROM $tbl_name ");

while($row = mysqli_fetch_array($result))
  {
  echo $row['username'] . " " . $row['password'];
  echo "<br>";
  }

mysqli_close($con);
?>

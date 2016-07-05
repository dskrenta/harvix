<?php
$dbhost = 'localhost';
$dbuser = 'wordpress';
$dbpass = 'dtechblog777';
$db_name="wordpress"; // Database name 

$conn = mysql_connect($dbhost, $dbuser, $dbpass);
mysql_select_db("$db_name")or die("cannot select DB");
if(! $conn )
{
  die('Could not connect: ' . mysql_error());
}
$sql = 'SELECT username, fullname, password FROM harvixsocial3';

mysql_select_db('test_db');
$retval = mysql_query( $sql, $conn );
if(! $retval )
{
  die('Could not get data: ' . mysql_error());
}
while($row = mysql_fetch_array($retval, MYSQL_ASSOC))
{
    echo "EMP ID :{$row['username']}  <br> ".
         "EMP NAME : {$row['fullname']} <br> ".
         "EMP SALARY : {$row['password']} <br> ".
         "--------------------------------<br>";
} 
echo "Fetched data successfully\n";
mysql_close($conn);
?>

<?php
$host="localhost"; // Host name 
$username="wordpress"; // Mysql username 
$password="dtechblog777"; // Mysql password 
$db_name="wordpress"; // Database name 
$tbl_name="harvixsocial4"; // Table name 

// Connect to server and select databse.
mysql_connect("$host", "$username", "$password")or die("cannot connect"); 
mysql_select_db("$db_name")or die("cannot select DB");

// username and password sent from form 
$myusername=$_POST['myusername']; 
$mypassword=$_POST['mypassword']; 

// To protect MySQL injection (more detail about MySQL injection)
$myusername = stripslashes($myusername);
$mypassword = stripslashes($mypassword);
$myusername = mysql_real_escape_string($myusername);
$mypassword = mysql_real_escape_string($mypassword);
$sql="SELECT * FROM $tbl_name WHERE username='$myusername' and password='$mypassword'";
$result=mysql_query($sql);

// Mysql_num_row is counting table row
$count=mysql_num_rows($result);

// If result matched $myusername and $mypassword, table row must be 1 row
if($count > 0){

// Register $myusername, $mypassword and redirect to file "login_success.php"
session_register("myusername");
session_register("mypassword"); 
$_SESSION['myusername']=$myusername;
$_SESSION['mypassword']=$mypassword;

$dbhost = 'localhost';
$dbuser = 'wordpress';
$dbpass = 'dtechblog777';
$db_name="wordpress"; // Database name 

$conn = mysql_connect($dbhost, $dbuser, $dbpass);
if(! $conn )
{
  die('Could not connect: ' . mysql_error());
}

$sql = "SELECT username, fullname, password, cphoto, pphoto, aboutme FROM harvixsocial4 WHERE username='$myusername'";

mysql_select_db('harvixsocial3');
$retval = mysql_query( $sql, $conn );
if(! $retval )
{
  die('Could not get data: ' . mysql_error());
}
while($row = mysql_fetch_array($retval, MYSQL_ASSOC))
{
	$_SESSION['myfullname']=$row['fullname'];
	$_SESSION['mycphoto']=$row['cphoto'];
	$_SESSION['mypphoto']=$row['pphoto'];
	$_SESSION['myaboutme']=$row['aboutme'];
} 

header("location:login_success2.php");
}
else {
echo "Wrong Username or Password";
}
?>

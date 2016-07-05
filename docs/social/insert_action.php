<?php
$host="localhost"; // Host name 
$username="wordpress"; // Mysql username 
$password="dtechblog777"; // Mysql password 
$db_name="wordpress"; // Database name 
$tbl_name="harvixtest"; // Table name 

// Connect to server and select database.
mysql_connect("localhost", "wordpress", "dtechblog777", "wordpress")or die("cannot connect");
mysql_select_db("$db_name")or die("cannot select DB");

// Get values from form 
$myusername=$_POST['myusername'];
$mypassword=$_POST['mypassword'];

// Insert data into mysql 
$sql="INSERT INTO $tbl_name (username, password)VALUES('$username', '$password')";
$result=mysql_query($sql);

// if successfully insert data into database, displays message "Successful". 
if($result){

	// Register $myusername, $mypassword and redirect to file "login_success.php"
	session_register("myusername");
	session_register("mypassword");
	$_SESSION['myusername']=$myusername;
	$_SESSION['mypassword']=$mypassword;
	header("location:login_success.php");

}

else {
echo "ERROR";
}
?>

<?php
// close connection 
mysql_close();
?>

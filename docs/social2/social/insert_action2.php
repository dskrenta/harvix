<?php
$host="localhost"; // Host name 
$username="wordpress"; // Mysql username 
$password="dtechblog777"; // Mysql password 
$db_name="wordpress"; // Database name 
$tbl_name="harvixsocial4"; // Table name 

// Connect to server and select database.
mysql_connect("localhost", "wordpress", "dtechblog777", "wordpress")or die("cannot connect");
mysql_select_db("$db_name")or die("cannot select DB");
$con = mysql_connect("localhost", "wordpress", "dtechblog777", "wordpress");

// Get values from form 
$myusername=$_POST['myusername'];
$myfullname=$_POST['myfullname'];
$mypassword=$_POST['mypassword'];
$mycphoto=$_POST['mycphoto'];
$mypphoto=$_POST['mypphoto'];
$myaboutme=$_POST['myaboutme'];

// Insert data into mysql 
$sql="INSERT INTO $tbl_name (username, fullname, password, cphoto, pphoto, aboutme)VALUES('$myusername', '$myfullname', '$mypassword', '$mycphoto', '$mypphoto', '$myaboutme')";
$result=mysql_query($sql);

// Check if Username already exists 
$sql="SELECT * FROM $tbl_name WHERE username='$myusername'";
$result=mysql_query($sql);

$count=mysql_num_rows($result);

if($count > 0){
	header("location:insertsec.php");
}

else{

 // if successfully insert data into database, displays message "Successful". 
        if($result){

                // Register $myusername, $mypassword and redirect to file "login_success.php"
                session_register("myusername");
                session_register("mypassword");
                
		$_SESSION['myusername']=$myusername;
                $_SESSION['myfullname']=$myfullname;
                $_SESSION['mypassword']=$mypassword;
                $_SESSION['mycphoto']=$mycphoto;
                $_SESSION['mypphoto']=$mypphoto;
                $_SESSION['myaboutme']=$myaboutme;
                
		// Create table
		$sql="CREATE TABLE $myusername(
		id int(4) NOT NULL auto_increment,
		title varchar(500) NOT NULL default '',
		content varchar(5000) NOT NULL default '',
		PRIMARY KEY (`id`)
		)
		TYPE=MyISAM AUTO_INCREMENT=2 ;
		";
		
		// Execute query
		if (mysqli_query($con,$sql))
  		{
  			header("location:login_success2.php");	
		}

		else
  		{
  			echo "Error creating table: " . mysqli_error($con); 
		}
                
		}       

                else 
		{
                	 header("location:insertsec2.php");
		}
}

?>

<?php
// close connection 
mysql_close();
?>

<!DOCTYPE html>

<html lang="en">

  <head>

    <meta charset="utf-8">

    <title>Harvix</title>

    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <meta name="description" content="">

    <meta name="author" content="">



    <!-- Le styles -->

    <link href="http://harvix.com/assets/bootstrap.css" rel="stylesheet">

      

        <!-- Fav and touch icons -->

    <link rel="apple-touch-icon-precomposed" sizes="144x144" href="http://www.harvix.com/images/harvixshort2.jpg">

    <link rel="apple-touch-icon-precomposed" sizes="114x114" href="http://www.harvix.com/images/harvixshort2.jpg">

      <link rel="apple-touch-icon-precomposed" sizes="72x72" href="http://www.harvix.com/images/harvixshort2.jpg">

                    <link rel="apple-touch-icon-precomposed" href="http://www.harvix.com/images/harvixshort2.jpg">

                                   <link rel="shortcut icon" href="http://www.harvix.com/images/harvixshort2.jpg">

        </head>



  <body>

<?php

$atitle = $_POST['atitle'] ;

$fname = $_POST['fname'] ;

$lname = $_POST['lname'] ;

$websitet = $_POST['websitet'] ;

$publish = $_POST['publish'] ;

$eday = $_POST['eday'] ;
$emonth = $_POST['emonth'] ;
$eyear = $_POST["eyear"] ;

$aday = $_POST['aday'] ;
$amonth = $_POST['amonth'] ;
$ayear = $_POST["ayear"] ;
 
//if bool is_nan(float $eday,$eyear,$aday,$ayear) {
//    alert("Please enter a valid number")
//    
//    }; 

echo '

Your Citation :


$lname,$fname."$atitle."<i>$websitet</i>$publish,$eday $emonth.$eyear.Web. $aday $amonth.$ayear.





'



?>

</body>

</html>

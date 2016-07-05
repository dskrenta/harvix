<?php
$email = $_POST["email"];
$title = $_POST["title"];
$notes = $_POST["notes"];

$to = $email;
$subject = "$title - Notes";
$message = $notes;
$from = "harvix@harvix.com";
$headers = "From:" . $from;
$headers = "From: " . $from . "\r\n";
$headers .= "Reply-To: ". "harvix@harvix.com" . "\r\n";
$headers .= "CC: harvix@harvix.com\r\n";
$headers .= "MIME-Version: 1.0\r\n";
$headers .= "Content-Type: text/html; charset=ISO-8859-1\r\n";
mail($to,$subject,$message,$headers);
?>

<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Harvix | Research engine for students</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Research engine for students ">
    <meta name="author" content="Harvix Search">

    <!-- Le styles -->
    <link href="http://harvix.com/bootstrap2.css" rel="stylesheet">
    <style type="text/css">

      body {
        padding-top: 20px;
        padding-bottom: 40px;
      }

      /* Custom container */
      .container-narrow {
        margin: 0 auto;
        max-width: 700px;
      }
      .container-narrow > hr {
        margin: 30px 0;
      }

      /* Main marketing message and sign up button */
      .jumbotron {
        margin: 60px 0;
        text-align: center;
      }
      .jumbotron h1 {
        font-size: 72px;
        line-height: 1;
      }
      .jumbotron .btn {
        font-size: 21px;
        padding: 14px 24px;
      }

      /* Supporting marketing content */
      .marketing {
        margin: 60px 0;
      }
      .marketing p + h4 {
        margin-top: 28px;
      }

    </style>

    <!-- HTML5 shim, for IE6-8 support of HTML5 elements -->
    <!--[if lt IE 9]>
      <script src="http://html5shim.googlecode.com/svn/trunk/html5.js"></script>
    <![endif]-->

    <!-- Fav and touch icons -->
  

	<link rel="apple-touch-icon-precomposed" sizes="144x144" href="http://www.harvix.com/images/harvixshort2.jpg">
    <link rel="apple-touch-icon-precomposed" sizes="114x114" href="http://www.harvix.com/images/harvixshort2.jpg">
      <link rel="apple-touch-icon-precomposed" sizes="72x72" href="http://www.harvix.com/images/harvixshort2.jpg">
                    <link rel="apple-touch-icon-precomposed" href="http://www.harvix.com/images/harvixshort2.jpg">
                                   <link rel="shortcut icon" href="http://www.harvix.com/images/harvixshort2.jpg">


</head>

  <body>
  

 <div class="container-narrow">

      <div class="masthead">
        <h3 class="muted">Notes Saved</h3>
      </div>

      <hr>

      <div class="jumbotron">
        <h1>Your Notes have been saved to your email account.</h1>
      </div>
	
	
      <hr>
      
      <div class="footer">
        <p>&copy; Harvix 2014</p>
      </div>

    </div> <!-- /container -->


</body>
</html>

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

<!--Last name, First name. "Article Title." Website Title. Publisher of Website, Day Month Year article was published. Web. Day Month Year article was accessed. <URL>.-->
<!--Cain, Kevin. "The Negative Effects of Facebook on Communication." Social Media Today RSS N.p., 29 June 2012. Web. 02 Jan. 2013.-->

<?php
$one = $_REQUEST['one'] ;
$two = $_REQUEST['two'] ;
$three = $_REQUEST['three'] ;
$four = $_REQUEST['four'] ;
$five = $_REQUEST['five'] ;
$six = $_REQUEST['six'] ;
$seven = $_REQUEST['seven'] ;

echo"<p>$one. \"$two.\" $three. $four, $five. Web. $six. $seven.</p>";
?>

</body>
</html>

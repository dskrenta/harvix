<?php
  //send email
  $from = $_REQUEST['from'] ;
  $subject = $_REQUEST['subject'] ;
  $message = $_REQUEST['message'] ;
  mail("harvix.com@gmail.com", $subject,
  $message, "From:" . $from);
?>




<!DOCTYPE html>
<html lang="en">
<body>  

<script>
  window.location.assign("http://harvix.com/about")
</script>


</body>
</html>



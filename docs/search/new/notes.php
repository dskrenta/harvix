<?php
$notes = $_POST["notes"];
$email = $_POST["email"];
$title = $_POST["title"];

$to = "$email";
$subject = "$title - Notes";
$message = "$notes";
$from = "harvix.com@gmail.com";
$headers = "From:" . $from;
mail($to,$subject,$message,$headers);
?>

<script>
window.location.assign("<?php echo $page_url; ?>")
</script>



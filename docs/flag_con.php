<?php
$page_url = $_POST["page_url"];
$type = $_POST["type"];
$query = $_POST["query"];
$title = $_POST["title"]; 
$snippet = $_POST["snippet"];
$url = $_POST["url"];

$to = "harvix.com@gmail.com";
$subject = "Automated $type content message";
$message = "URL: $page_url TYPE: $type CONTENT: $title, $snippet, $url QUERY: $query";
$from = "harvix.com@gmail.com";
$headers = "From:" . $from;
mail($to,$subject,$message,$headers);
?>

<script>
window.location.assign("$page_url")
</script>

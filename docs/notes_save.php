<?php
//$page_url = "http://harvix.com/search/new/dev5.cgi?q=$query";
$type = $_GET["type"];
$query = $_GET["query"];
$title = $_GET["title"];
$snippet = $_GET["snippet"];
$url = $_GET["url"];
$page_url = "http://harvix.com/search/new/mst3kv2.cgi?q=$query";

$to = "harvix.com@gmail.com";
$subject = "Automated $type content message";
$message = "URL: $page_url TYPE: $type CONTENT: $title, $snippet, $url QUERY: $query";
$from = "harvix.com@gmail.com";
$headers = "From:" . $from;
mail($to,$subject,$message,$headers);
?>

<script>
window.location.assign("<?php echo $page_url; ?>")
</script>

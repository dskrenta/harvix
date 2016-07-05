<?php
$search = $_GET['q'];
if(strpos($search, "http://") !== false) 
{
}
else 
{
$search = "http://$search";
}
$json = json_decode(file_get_contents("http://api.diffbot.com/v2/article?token=5db92311c3bd3c1a34bc9f2e1855f419&url=".$search.""));
if ($json)
{
$title = $json->title;
$author = $json->author;
$date = $json-> date;
$images = $json->images;
$text = $json->text;
$tags = $json->tags;
$type = $json->type;
$url = $json->url;
$html = $json->html;

echo "$title <br> $author <br> $date <br> $type <br> $url <br> <br> <br>";

if ($tags)
{
foreach ($json->tags as $tag)
{
echo "&nbsp; [$tag]";
}
}

if ($images)
{
foreach ($json->images as $image)
{
$imageurl = $image->url;
echo"<br><img src='$imageurl'><br>";
}
}

if ($text)
{
$text = str_replace("\n","<br><br>", $text);
echo "<br> <br> $text <br> <br>";
}

else
{
echo $html;
}
}
?>

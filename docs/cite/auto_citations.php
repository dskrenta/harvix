<?php

$form_header = "<!DOCTYPE html>
	<html>
	<head>
	    <style>
	        /* Basic Grey */
	        .basic-grey {
	            width: 400px;
	            margin-right: auto;
	            margin-left: auto;
	            background: #EEE;
	            padding: 20px 30px 20px 30px;
	            font: 12px Georgia, 'Times New Roman', Times, serif;
	            color: #888;
	            text-shadow: 1px 1px 1px #FFF;
	            border:1px solid #DADADA;
	        }
	        .basic-grey h1 {
	            font: 25px Georgia, 'Times New Roman', Times, serif;
	            padding: 0px 0px 10px 40px;
	            display: block;
	            border-bottom: 1px solid #DADADA;
	            margin: -10px -30px 30px -30px;
	            color: #888;
	        }
	        .basic-grey h1>span {
	            display: block;
	            font-size: 11px;
	        }
	        .basic-grey label {
	            display: block;
	            margin: 0px 0px 5px;
	        }
	        .basic-grey label>span {
	            float: left;
	            width: 80px;
	            text-align: right;
	            padding-right: 10px;
	            margin-top: 10px;
	            color: #888;
	        }
	        .basic-grey input[type='text'], .basic-grey input[type='email'], .basic-grey textarea,.basic-grey select{
	            border: 1px solid #DADADA;
	            color: #888;
	            height: 24px;
	            margin-bottom: 16px;
	            margin-right: 6px;
	            margin-top: 2px;
	            outline: 0 none;
	            padding: 3px 3px 3px 5px;
	            width: 70%;
	            font: normal 12px/12px Georgia, 'Times New Roman', Times, serif;
	        }
	        .basic-grey select {
	            background: #FFF url('down-arrow.png') no-repeat right;
	            background: #FFF url('down-arrow.png') no-repeat right);
	            appearance:none;
	            -webkit-appearance:none; 
	            -moz-appearance: none;
	            text-indent: 0.01px;
	            text-overflow: '';
	            width: 72%;
	            height: 30px;
	        }
	        .basic-grey textarea{
	            height:100px;
	        }
	        .basic-grey .button {
	            background: #E48F8F;
	            border: none;
	            padding: 10px 25px 10px 25px;
	            color: #FFF;
	        }
	        .basic-grey .button:hover {
	            background: #CF7A7A
	        }
	    </style>
	    <title>Harvix Citations</title>
	</head>
	<body>

	
	";
$form_footer = "
	 <script type='text/javascript'>
			var date = new Date();
			var month_Names = [ 'January', 'February', 'March', 'April', 'May', 'June',
    		'July', 'August', 'September', 'October', 'November', 'December' ];
   			document.getElementById('medium').value = 'Web';
			document.getElementById('year_accessed').value = date.getFullYear();
			document.getElementById('month_accessed').value = month_Names[date.getMonth()];
			document.getElementById('day_accessed').value = date.getDate();
	</script>
	</form>
	</body>
	</html>";
if ($_SERVER["REQUEST_METHOD"] == "POST"){
	$url = $_POST["url"];
	// function get_url_contents($url){
	//          $crl = curl_init();
	//          $timeout = 5;
	//          curl_setopt ($crl, CURLOPT_URL,$url);
	//          curl_setopt ($crl, CURLOPT_RETURNTRANSFER, 1);
	//          curl_setopt ($crl, CURLOPT_CONNECTTIMEOUT, $timeout);
	//          $ret = curl_exec($crl);
	//         curl_close($crl);
	//         return $ret;
	// }
	// $page = get_url_contents($url);
	// $title_start = strpos($page,"</title>");
	// $title_count =  $title_start - strpos($page,"<title>") + 7;
	// $title = substr($page, $title_start, 5);
	// echo $title;
	$article_day = "Day published not found";
	$article_month = "Month published not found";
	$article_year = "Year published not found";
	$request_url = "http://api.diffbot.com/v2/article?token=528accf4004e80e5c4c7d555a8a6a9ac&url=";
	$full_url = $request_url . $url;
	$json = file_get_contents($full_url);
	$data = json_decode($json, TRUE);
	$article_title = $data['title'];
	$author_name = $data['author'];
	$last_name = substr($author_name, strpos($author_name, " "));
	$first_name = substr($author_name, 0, strpos($author_name, " "));
	$article_title = htmlentities($article_title ,ENT_QUOTES);
	if( isset( $data['date'] ) ){
		$article_date = $data['date'];
		$day = strpos($article_date, " ");
		$month = strpos($article_date, " ", $day + 1);
		$year = strpos($article_date, " ", $month + 1);
		$month_blank =  $year - $month;
		$article_day = substr($article_date, $day, 3);
		$article_month = substr($article_date, $month, $month_blank);
		$article_year = substr($article_date, $year, 5);


	}
	$page_title_url_start = strpos($url, ".");
	$page_title_url_end = strpos($url, "//");
	$page_title_strpos = $page_title_url_start - 2 -  $page_title_url_end;
	$page_title = substr($url, strpos($url, "//") + 2, $page_title_strpos);

	echo (" $form_header
		<form method='post' action='final_cite.php' class='basic-grey'>
		<h1>Is this all correct?</h1>
		<label>
        <span>First Name:</span>
        <input id='first_name' type='text' name='first_name' value='$first_name' placeholder='first name not found' />
    </label>
    <label>
        <span>Last Name:</span>
        <input id='last_name' type='text' name='last_name' value='$last_name' placeholder='last name not found' />
    </label>
    
    <label>
        <span>Page Title:</span>
        <input id='page_title' type='text' name='page_title'  value='$article_title' placeholder='page title not found' />
    </label>
    <label>
        <span>Website Name:</span>
        <input id='website_title' type='text' name='website_title' value='$page_title' placeholder='website name not found' />
    </label>
    <label>
        <span>Year accessed:</span>
        <input type='text' id='year_accessed' name='year_accessed' placeholder='year accessed not found'>
    </label> 
    <label>
        <span>Month accessed:</span>
        <input type='text' id='month_accessed' name='month_accessed' placeholder='month acceseed not found'>
    </label>
    <label>
        <span>Day accessed:</span>
        <input type='text' name='day_accessed' id='day_accessed' placeholder='Day accessed' placeholder='day accessed not found'>
    </label>
    <label>
        <span>Month published:</span>
        <input type='text' id='publication_month' name='publication_month'  value='$article_month' placeholder='month published not found'>
    </label> 
    <label>
        <span>Publication Year:</span>
        <input type='text' id='publication_year' name='publication_year' value='$article_year'  placeholder='publication year not found'>
    </label>
    <label>
        <span>Publication day:</span>
        <input type='text' name='publication_day' id='release_day' value='$article_day' placeholder=' publication day not found' >
    </label> 
     <label>
        <span>Meduim:</span>
        <input type='text' name='Medium' id='medium' placeholder='Medium' placeholder='medium not found'>
    </label> 

    </label>
    <label>
        <span>Publisher:</span>
        <input id='publisher_title' type='text' name='publisher_title' value='$page_title' placeholder='publisher not found' />
     </label>
     <label>
        <span>&nbsp;</span> 
        <input type='submit' class='button' value='All good' /> 
    </label> 
    $form_footer

");
}

else{

	echo "$form_header
	    <form method='post' action='auto_citations.php' class='basic-grey'>
	    <h1>URL for citations</h1>
	    <label>
	        <span>URL:</span>
	        <input id='url' type='url' name='url' placeholder='http://en.wikipedia.org/wiki/Apple_Inc.' />
	    </label>
	    <label>
	        <span>&nbsp;</span> 
	        <input type='submit' class='button' value='Send' /> 
	    </label> 
	$form_footer";
	}
?>



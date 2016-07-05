<?php 

$my_account = 'Harvixseach'; // Account ID. modify to fit your needs 
$subid = ''; // if sending traffic with sub affiliates. modify to fit your needs 
$rpp = 1; // number of results to return. modify to fit your needs 

$ua = urlencode($_SERVER['HTTP_USER_AGENT']); // user agent. do not modify 
$ip = $_SERVER['REMOTE_ADDR']; // IP address of user requesting search. do not modify 

// acquire search terms 
//if(isset($_REQUEST['terms']) && !empty($_REQUEST['terms'])){ 
//     $terms = urlencode($_REQUEST['terms']); 
//}else{ 
//     //$terms = urlencode('my default keyword'); /// you may uncomment this line and comment the line below to display results when users first land your page
//     echo get_search_form(); 
//     exit; 
//} 
  
$terms = $_GET["terms"];

$url = "http://xml.admedia.com/xml.php?affiliate=$my_account&subid=$subid&IP=$ip&rpp=$rpp&ua=$ua&Terms=$terms"; 

$result = call_xml($url, $ua); 

// check if results came back from the feed 
if (strstr($result, "title") === FALSE) {     $msg = "No results found.";}else{$msg="";} 

echo get_search_form($terms, $msg); 
echo format_result($result); 

/* 
     Parses and display the result of the XML feed 
     @param $result - The result of the XML feed 
     @returns - the HTML version of the XML results 
*/ 
function format_result($result){ 
     $title = array(); 
     $url = array(); 
     $redirect = array(); 
     $description = array(); 

     preg_match_all('#<title>(.*?)</title>#', $result, $title); 
     preg_match_all('#<url>(.*?)</url>#', $result, $url); 
     preg_match_all('#<redirect>(.*?)</redirect>#', $result, $redirect); 
     preg_match_all('#<description>(.*?)</description>#', $result, $description); 

     //$res = $redirect[0][0];

     $items = count($title[1]); 
     $rv = ''; 
     for($i=0; $i<$items; $i++){ 
          $rv .= ' 
               <li> 
               <iframe width="500px" height="500px" src='.$redirect[1][$i].'></iframe><br> 
                '.$description[1][$i].'<br>'. 
                $url[1][$i]. 
                '<br><br></li>'; 
//	  $rv = "<iframe src=" . "$res" . "></iframe>"; 
	  //$ahtml ="Positive";      

     }// end for 
      
     return $rv;
     //return $ahtml;
 
}// end function 

/* 
     Obtains the search form 
     @param $terms - the default search term 
     @param $msg - alert message 
      
     @returns - The HTML form 
*/ 
function get_search_form($terms="", $msg=""){ 
          if (!empty($msg)) { 
              $msg = "<font color='red'><b>$msg</b></font><hr>"; 
          }// end if 
           
          $form = " 
                    $msg 
                    Please enter your search term 
                    <br><br> 
                    <form method='post' action='".$_SERVER["PHP_SELF"]."'> 
                         Keyword: <input type='text' name='terms' value='$terms'> 
                         <br> 
                         <br> 
                         <input type='submit' value='Search'> 
                    </form><hr> 
               "; 
          return $form; 

}// end function 


/* 
     Calls the XML feed 
     @param $url - the URL of the feed to call 
     @param $ua - The user agent 
      
     @returns - the result of the query from the feed 
*/ 
function call_xml($url, $ua="") 
{ 
    $hostname=trim($_SERVER['HTTP_HOST']); 
     
    $ch = curl_init($url); 
    curl_setopt($ch, CURLOPT_USERAGENT, $ua); 
    curl_setopt($ch, CURLOPT_REFERER, $hostname); 
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1); 
    curl_setopt($ch, CURLOPT_HEADER, 0); 
    $result = curl_exec($ch); 
    curl_close($ch); 
    return $result; 
}// end function 

?> 

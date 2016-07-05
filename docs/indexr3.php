<script>
if( /Android|webOS|iPhone|iPad|iPod|BlackBerry/i.test(navigator.userAgent) ) 
{
	window.location.assign("http://www.harvix.com/mobileindex.html")
}
</script>

<?php
// finds ramdom number between 0,10
$num = rand(0,20);

// matches num with the designated background 
switch ($num)
{
case 0:
	$background = "http://www.hdwallpapersarena.com/wp-content/uploads/2012/09/yamuna-river-agra-india.jpg";
	break;	
case 1:
        $background = "https://fbcdn-sphotos-f-a.akamaihd.net/hphotos-ak-ash4/241849_500567746635379_269106673_o.jpg";
        break; 
case 2:
        $background = "http://wallpicshd.com/wp-content/uploads/2013/04/Animal-Tiger-Wallpaper-Full-HD.jpg";
        break; 
case 3:
        $background = "http://wallpaperan.com/wallpaper/night_fall_on_eiffel_tower_wallpaper.jpg";
        break; 
case 4:
        $background = "http://d13pix9kaak6wt.cloudfront.net/background/daniel.radding_1339982506_57.jpg";
        break; 
case 5:
        $background = "https://sphotos-a.xx.fbcdn.net/hphotos-ash3/622368_10151206907666934_361236178_o.jpg";
        break; 
case 6:
        $background = "https://sphotos-a.xx.fbcdn.net/hphotos-ash3/242117_10151237193471934_51721669_o.jpg";
        break; 
case 7:
        $background = "https://sphotos-b.xx.fbcdn.net/hphotos-frc1/456547_10151189203766934_1576465912_o.jpg";
        break; 
case 8:
        $background = "http://wakpaper.com/large/Houses_wallpapers_228.jpg";
        break; 
case 9:
        $background = "http://www.hdcarwallpapers.in/hdwallpapers/yamaha-sports-race-wallpapers.jpg";
        break; 
case 10:
        $background = "https://fbcdn-sphotos-e-a.akamaihd.net/hphotos-ak-frc1/290799_10151189200236934_330592782_o.jpg";
        break; 
case 11:
        $background = "http://www.hdwallpaperstop.com/wp-content/uploads/2013/02/Aircraft-wallpapers.jpg";
        break;
case 12:
        $background = "http://uniquenaturewallpapers.com/wp-content/uploads/2013/04/Jaguar-Hd-Wallpaper-Free-Download.jpg";
        break;
case 13:
        $background = "http://2.bp.blogspot.com/-dcgYv-SFEu0/TZVuveCkq1I/AAAAAAAAI2A/vK0PXUJ8aKw/s1600/tiger_wallpapers_hd_Bengal_Tiger_hd_wallpaper.jpg";
        break;
case 14:
        $background = "http://www.hdwallpapersbest.com/wp-content/uploads/2013/04/animal-hd-wallpapers-166.jpg";
        break;
case 15:
        $background = "http://hdwallpapersgallery.com/wp-content/uploads/2013/02/Animal-tiger-black-wallpaper.jpg";
        break;
case 16:
        $background = "http://www.macwallhd.com/wp-content/Wallpapers/Animals/Cats%20Behaving%20on%20Mac%20Animals%20Wallpapers-764196526.jpeg";
        break;
case 17:
        $background = "http://www.walllopers.com/wp-content/uploads/2013/03/green-chameleon-animal-wallpaper-1920x1200-487.jpg";
        break;
case 18:
        $background = "http://good-wallpapers.com/pictures/8676/1600_Ariel%20Atom%20V8.jpg";
        break;
case 19:
        $background = "http://www.wallbest.com/wallpapers/1920x1080-1080p/moto-sports-wallpaper-1003112-www.wallbest.com.jpg";
        break;
case 20:
        $background = "http://loadpaper.com/large/Skydiving_wallpapers_436.jpg";
        break;
}
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
    <link href="bootstrap2.css" rel="stylesheet">
    <style type="text/css">
      body {
        padding-top: 60px;
        padding-bottom: 40px;
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


<style>

fter{
    content:"";
    display:table;
}
 
.cf:after{
    clear:both;
}
 
.cf{
    zoom:1;
}

.logo{color: black; font-size: 40px; font-family:  Helvetica, sans-serif; font-size: normal; line-height: normal;}

body {
       background-image:url('<?php echo $background; ?>');
       background-repeat:no-repeat;
       background-size: 100%;
}



div.spacer{height:200px;}


div.spacer2{height:100px;}

.form-wrapper2 {
    width: 1000px;
    padding: 10px;
    margin: 0px auto 0px auto;
    background: #444;
    background: rgba(0,0,0,.2);
    box-shadow: 0 1px 1px rgba(0,0,0,.4) inset, 0 1px 0 rgba(255,255,255,.2);
    margin-bottom:30px;
}



/* Form wrapper styling */
.form-wrapper {
    width: 780px;
    padding: 10px;
    margin: 0px auto 0px auto;
    background: #444;
    background: rgba(0,0,0,.2);
    box-shadow: 0 1px 1px rgba(0,0,0,.4) inset, 0 1px 0 rgba(255,255,255,.2);
    margin-bottom:30px;
}
 
/* Form text input */
 
.form-wrapper input {
    width: 500px;
    height: 40px;
    padding: 10px 5px;
    float: left;    
    font: Normal 20px 'Helvetica Neue';
    border: 0;
    border-radius: 3px 0 0 3px;  
    background: #eee;
}
 
.form-wrapper input:focus {
    outline: 0;
    background: #fff;
    box-shadow: 0 0 2px rgba(0,0,0,.8) inset;
}
 
.form-wrapper input::-webkit-input-placeholder {
   color: black;
   font-weight: normal;
   font-style: italic;
}
 
.form-wrapper input:-moz-placeholder {
    color: black;
    font-weight: normal;
    font-style: italic;
}
 
.form-wrapper input:-ms-input-placeholder {
    color: black;
    font-weight: normal;
    font-style: italic;
}    
 
/* Form submit button */
.form-wrapper button {
    overflow: visible;
    position: relative;
    float: right;
    border: 0;
    padding: 0;
    cursor: pointer;
    height: 40px;
    width: 110px;
    font: bold 15px/40px 'lucida sans', 'trebuchet MS', 'Tahoma';
    color: #fff;
    text-transform: uppercase;
    background: #d83c3c;
    border-radius: 0 3px 3px 0;      
    text-shadow: 0 -1px 0 rgba(0, 0 ,0, .3);
}   
   
.form-wrapper button:hover{     
    background: #e54040;
}   
   
.form-wrapper button:active,
.form-wrapper button:focus{   
    background: #c42f2f;
    outline: 0;   
}
 
.form-wrapper button:before { /* left arrow */
    content: '';
    position: absolute;
    border-width: 8px 8px 8px 0;
    border-style: solid solid solid none;
    border-color: transparent #d83c3c transparent;
    top: 12px;
    left: -6px;
}
 
.form-wrapper button:hover:before{
    border-right-color: #e54040;
}
 
.form-wrapper button:focus:before,
.form-wrapper button:active:before{
        border-right-color: #c42f2f;
}      
 
.form-wrapper button::-moz-focus-inner { /* remove extra button spacing for Mozilla Firefox */
    border: 0;
    padding: 0;
} 

#scrollable {
    overflow:auto;
    width:100%;
    height:160px;
}


#scrollable-img {
    overflow: auto;
    width:100%;
    height:300px;
}


#items {
    width: 1000px; /* itemWidth x itemCount */
}

.item {
    float:left;
}

.item2 {
    width:400px;
    height:200px;
    float:left;
}

.item3 {
    width:350px;
    height:220px;
    float:left;
}

.itemfacts {
    width:300px;
    height:200px;
    float:left;
}

.itemwiki {
    width:100%;
    float:left;
}


</style>

<script type="text/javascript">

  var _gaq = _gaq || [];
  _gaq.push(['_setAccount', 'UA-30447587-1']);
  _gaq.push(['_trackPageview']);

  (function() {
    var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
    ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
    var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
  })();

</script>



<script type="text/javascript">

  var _gaq = _gaq || [];
  _gaq.push(['_setAccount', 'UA-30658262-1']);
  _gaq.push(['_trackPageview']);

  (function() {
    var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
    ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
    var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
  })();

</script>


</head>

  <body>
  
    <div class="navbar navbar-inverse  navbar-fixed-top">
      <div class="navbar-inner">
          <a class="btn btn-navbar" data-toggle="collapse" data-target=".nav-collapse">
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </a>
          <div class="nav-collapse collapse">
            <ul class="nav">
    	<li><a href="index.php">SEARCH</a></li>
	<li><a href="images.html">IMAGES</a></li>
  	<li><a href="videos.html">VIDEOS</a></li>
	<li><a href="docs.html">NOTES</a></li>
	<li><a href="games2.cgi">GAMES</a></li>
	<li><a href="docs.html">NEWS</a></li>
  	<li><a href="store.html">STORE</a></li>
        </ul>
        </div><!--/.nav-collapse -->
      </div>
    </div>


<center>



<div class="spacer"></div>


<form id="searchForm" name="searchForm" action="http://harvix.com/msnew3.cgi" onsubmit="submitted('h'); return false" class="form-wrapper cf">
<table cellpadding="5"><tr><td>
<div class="logo">
<strong><span style="color:white">Har</span><span style="color:red">vix</span></strong>
</div>
</td><td>
<input id="searchBox" autofocus="autofocus" autocomplete="off" type="text" spellcheck="false" name="q" placeholder="What would you like to learn about?" required />
<button type="submit">Search</button>
</td></tr></table></form>


<div class="spacer2"></div>

<form id="searchForm" class="form-wrapper2 cf">

<img src="data:image/jpeg;base64,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">

<img src="data:image/jpeg;base64,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">

<img src="data:image/jpeg;base64,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">

<img src="data:image/jpeg;base64,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">

</form>


</center>



	 <div class="navbar navbar-inverse  navbar-fixed-bottom">
      <div class="navbar-inner">
          <a class="btn btn-navbar" data-toggle="collapse" data-target=".nav-collapse">
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </a>
          <div class="nav-collapse collapse">
            <ul class="nav">
              <li><a href="newabout.html">About Harvix</a></li>
              <li><a href="newterms.html">Terms + Privacy</a></li>
	<li><a href="newterms.html">Business Solutions</a></li>
	<li><a href="newterms.html">Academic Solutions</a></li>
	<li><a href="https://www.facebook.com/Harvixsearch">Find us on Facebook</a></li>
	  <li><a href="https://www.twitter.com/@Harvix">Follow @Harvix on Twitter</a></li>
	<li><a href=""><b>&copy; 2013 Harvix</b></a></li>	    
	</ul>
	</div><!--/.nav-collapse -->
      </div>
    </div>

  </body>
</html>



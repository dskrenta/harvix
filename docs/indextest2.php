<?php
// finds ramdom number between 0,10
$num = rand(0,10);

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
        $background = "http://www.desktopwallpaper2.com/photo/bc90706a34113525d52f13524a04a6f1.jpg";
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
        $background = "https://fbcdn-sphotos-f-a.akamaihd.net/hphotos-ak-prn1/330529_10151371729846934_426887010_o.jpg";
        break; 
case 9:
        $background = "http://www.buybyoffers.com/wp-content/uploads/2012/12/background.jpg";
        break; 
case 10:
        $background = "https://fbcdn-sphotos-e-a.akamaihd.net/hphotos-ak-frc1/290799_10151189200236934_330592782_o.jpg";
        break; 
}
?>

<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Harvix | Research engine for students</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="">
    <meta name="author" content="">

    <!-- Le styles -->
    <link href="bootstrap2.css" rel="stylesheet">
    

	<script src="http://code.jquery.com/jquery-1.8.2.js"></script>
    	<script src="http://code.jquery.com/ui/1.9.0/jquery-ui.js"></script>
    	<link rel="stylesheet" href="/resources/demos/style.css" />

	<!--#include virtual="/autocomplete.html" -->


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

.logo{color: black; font-size: 50px; font-family:  Helvetica, sans-serif; font-size: normal; line-height: normal;}

body {
       background-image:url('<?php echo $background; ?>');
       background-repeat:no-repeat;
       background-size: 100%;
}



div.spacer{height:200px;}

/* Form wrapper styling */
.form-wrapper {
    width: 820px;
    padding: 4px;
    margin: 0px auto 0px auto;
    background: #444;
    background: rgba(0,0,0,.2);
    box-shadow: 0 1px 1px rgba(0,0,0,.4) inset, 0 1px 0 rgba(255,255,255,.2);
}
 
/* Form text input */
 
.form-wrapper input {
    width: 500px;
    height: 20px;
    padding: 10px 5px;
    float: left;    
    font: bold 20px 'Helvetica';
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

</style>

<script>
function isiPhone(){
    return (
        (navigator.platform.indexOf("iPhone") != -1)
        || (navigator.platform.indexOf("iPod") != -1)
        || (navigator.platform.indexOf("iPad") != -1)
    );
}
if(isiPhone()){
   window.location.replace("mobileharvix/index.html";);
}
</script>


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
	<li><a href="docs.html">DOCUMENTS</a></li>
	<li><a href="games2.cgi">GAMES</a></li>
        </ul>
        </div><!--/.nav-collapse -->
      </div>
    </div>


<center>



<div class="spacer"></div>

<div class="ui-widget">
<form id="searchForm" name="searchForm" action="http://harvix.com/msnew3.cgi" onsubmit="submitted('h'); return false" class="form-wrapper cf">
<table cellpadding="5"><tr><td
<div class="logo">
<strong><span style="color:white">Har</span><span style="color:red">vix</span></strong>
</div>
</td><td>
<input id="searchBox" autofocus="autofocus" autocomplete="off" type="text" spellcheck="false" name="q" placeholder="What would you like to learn about?" required />
<button type="submit">Search</button>
</td></tr></table></form>
</div>

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
              <li><a href="newterms.html">Terms & Privacy</a></li>
	<li><a href="https://www.facebook.com/Harvixsearch">Find us on Facebook</a></li>
	  <li><a href="https://www.twitter.com/@Harvix">Follow @Harvix on Twitter</a></li>
	<li><a href=""><b>&copy; 2013 Harvix</b></a></li>	    
	</ul>
	</div><!--/.nav-collapse -->
      </div>
    </div>




    <!-- Le javascript
    ================================================== -->
    <!-- Placed at the end of the document so the pages load faster -->
    <script src="http://twitter.github.com/bootstrap/assets/js/jquery.js"></script>
    <script src="http://twitter.github.com/bootstrap/assets/js/bootstrap-transition.js"></script>
    <script src="http://twitter.github.com/bootstrap/assets/js/bootstrap-alert.js"></script>
    <script src="http://twitter.github.com/bootstrap/assets/js/bootstrap-modal.js"></script>
    <script src="http://twitter.github.com/bootstrap/assets/js/bootstrap-dropdown.js"></script>
    <script src="http://twitter.github.com/bootstrap/assets/js/bootstrap-scrollspy.js"></script>
    <script src="http://twitter.github.com/bootstrap/assets/js/bootstrap-tab.js"></script>
    <script src="http://twitter.github.com/bootstrap/assets/js/bootstrap-tooltip.js"></script>
    <script src="http://twitter.github.com/bootstrap/assets/js/bootstrap-popover.js"></script>
    <script src="http://twitter.github.com/bootstrap/assets/js/bootstrap-button.js"></script>
    <script src="http://twitter.github.com/bootstrap/assets/js/bootstrap-collapse.js"></script>
    <script src="http://twitter.github.com/bootstrap/assets/js/bootstrap-carousel.js"></script>
    <script src="http://twitter.github.com/bootstrap/assets/js/bootstrap-typeahead.js"></script>

<div id="fb-root"></div>
<script>(function(d, s, id) {
  var js, fjs = d.getElementsByTagName(s)[0];
  if (d.getElementById(id)) return;
  js = d.createElement(s); js.id = id;
  js.src = "//connect.facebook.net/en_US/all.js#xfbml=1";
  fjs.parentNode.insertBefore(js, fjs);
}(document, 'script', 'facebook-jssdk'));</script>

  </body>
</html>

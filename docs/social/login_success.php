<?php
session_start();
?>

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
	$background = "http://wallpaper.pickywallpapers.com/1920x1080/snowboard-hdr-jump.jpg";
	break;	
case 1:
        $background = "https://fbcdn-sphotos-f-a.akamaihd.net/hphotos-ak-ash4/241849_500567746635379_269106673_o.jpg";
        break; 
case 2:
        $background = "http://wallpicshd.com/wp-content/uploads/2013/04/Animal-Tiger-Wallpaper-Full-HD.jpg";
        break; 
case 3:
        $background = "http://www.wallgc.com/images/2012/12/felix-baumgartnerskydiving-hd-sports.jpg";
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
        $background = "http://bestwallpaper2013.com/wp-content/uploads/2013/05/Tesla-Model-S-416-2013-Tesla-Model-S-416-HD-Wallpaper.jpg";
        break;
case 13:
        $background = "http://2.bp.blogspot.com/-dcgYv-SFEu0/TZVuveCkq1I/AAAAAAAAI2A/vK0PXUJ8aKw/s1600/tiger_wallpapers_hd_Bengal_Tiger_hd_wallpaper.jpg";
        break;
case 14:
        $background = "http://www.wallgc.com/images/2013/02/hd-new-york-high-definition-stock.jpg";
        break;
case 15:
        $background = "http://cdn8.staztic.com/app/a/2564/2564719/amazing-hdr-photos-wallpaper-2-7-s-307x512.jpg";
        break;
case 16:
        $background = "http://www.macwallhd.com/wp-content/Wallpapers/Animals/Cats%20Behaving%20on%20Mac%20Animals%20Wallpapers-764196526.jpeg";
        break;
case 17:
        $background = "http://www.walllopers.com/wp-content/uploads/2013/03/green-chameleon-animal-wallpaper-1920x1200-487.jpg";
        break;
case 18:
        $background = "http://t.wallpaperweb.org/wallpaper/known_places/1366x768/amazingsearesortwallpaper1235_1366x768.jpg";
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
    <link href="http://harvix.com/assets/bootstrap.css" rel="stylesheet">
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

/* Form wrapper styling */
.form-wrapper {
    width: 780px;
    padding: 10px;
    margin: 0px auto 0px auto;
    background: #444;
    background: rgba(0,0,0,.2);
    box-shadow: 0 1px 1px rgba(0,0,0,.4) inset, 0 1px 0 rgba(255,255,255,.2);
}
 
/* Form text input */
 
.form-wrapper input {
    width: 500px;
    height: 40px;
    padding: 5px 5px;
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



<!-- start Mixpanel --><script type="text/javascript">(function(e,b){if(!b.__SV){var a,f,i,g;window.mixpanel=b;a=e.createElement("script");a.type="text/javascript";a.async=!0;a.src=("https:"===e.location.protocol?"https:":"http:")+'//cdn.mxpnl.com/libs/mixpanel-2.2.min.js';f=e.getElementsByTagName("script")[0];f.parentNode.insertBefore(a,f);b._i=[];b.init=function(a,e,d){function f(b,h){var a=h.split(".");2==a.length&&(b=b[a[0]],h=a[1]);b[h]=function(){b.push([h].concat(Array.prototype.slice.call(arguments,0)))}}var c=b;"undefined"!==
typeof d?c=b[d]=[]:d="mixpanel";c.people=c.people||[];c.toString=function(b){var a="mixpanel";"mixpanel"!==d&&(a+="."+d);b||(a+=" (stub)");return a};c.people.toString=function(){return c.toString(1)+".people (stub)"};i="disable track track_pageview track_links track_forms register register_once alias unregister identify name_tag set_config people.set people.set_once people.increment people.append people.track_charge people.clear_charges people.delete_user".split(" ");for(g=0;g<i.length;g++)f(c,i[g]);
b._i.push([a,e,d])};b.__SV=1.2}})(document,window.mixpanel||[]);
mixpanel.init("6b7b40427940a64fc16ee92f6fbd612a");</script><!-- end Mixpanel -->



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
	<li><a href="docs.html">NOTES</a></li>
	<li><a href="games2.cgi">GAMES</a></li>
	<li><a href="news.html">NEWS</a></li>
        <li><a href="store.html">STORE</a></li>
          <li class="dropdown">
                        <a href="#" class="dropdown-toggle" data-toggle="dropdown">TRENDING <b class="caret"></b></a>
                        <ul class="dropdown-menu">
                          <li class="nav-header">Trending on Harvix</li>
                          <li><a href="http://harvix.com/msnew3.cgi?q=Detroit+Bankruptcy">Detroit Bankruptcy</a></li>
                          <li><a href="http://harvix.com/msnew3.cgi?q=Edward+Snowden">Edward Snowden</a></li>
			  <li><a href="http://harvix.com/msnew3.cgi?q=Summer+Recipes">Summer Recipes</a></li>
			  <li><a href="http://harvix.com/msnew3.cgi?q=Alex+Rodriguez">Alex Rodriguez</a></li>
			  <li><a href="http://harvix.com/msnew3.cgi?q=Kate+Middleton+Boy">Kate Middleton Boy</a></li>
			  <li><a href="http://harvix.com/msnew3.cgi?q=J.K.+Rowling">J.K. Rowling</a></li>
                        </ul>
                      </li>
	</ul>

	<ul class="nav pull-right">
                      <li class="dropdown">
                        <a href="#" class="dropdown-toggle" data-toggle="dropdown"><?php echo $_SESSION['myusername']; ?> <b class="caret"></b></a>
                        <ul class="dropdown-menu">
                          <li><a href="http://harvix.com/social/mypage.php"><?php echo $_SESSION['myusername']; ?></a></li>
                          <li><a href="http://harvix.com/social/logout.php">Sign Out</a></li>
			  <li><a href="http://harvix.com/social/settings.php">Settings</a></li>
                        </ul>
                      </li>
                    </ul>

        </div><!--/.nav-collapse -->
      </div>
    </div>


<center>



<div class="spacer"></div>


<form id="searchForm" name="searchForm" action="http://harvix.com/msnew3.cgi" onsubmit="submitted('h'); return false" class="form-wrapper cf">
<table cellpadding="5"><tr><td
<div class="logo">
<strong><span style="color:white">Har</span><span style="color:red">vix</span></strong>
</div>
</td><td>
<input id="searchBox" autofocus="autofocus" autocomplete="off" type="text" spellcheck="false" name="q" placeholder="What would you like to learn about?" required x-webkit-speech="" speech="" onwebkitspeechchange="this.form.submit();" />
<button type="submit">Search</button>
</td></tr></table></form>

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



    <script src="http://harvix.com/assets/jquery.js"></script>
    <script src="http://harvix.com/assets/dropdown.js"></script>
  

</body>
</html>

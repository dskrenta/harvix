#!/usr/bin/perl
use strict;

# magic - do not change
print "Content-type: text/html\n\n";
my $page = $ENV{QUERY_STRING} || shift || 1;
# end magic


if ( $page eq '1' )
{
print <<EOF

<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Harvix Games</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Harvix free online  Games">
    <meta name="author" content="Harvix Search">

    <!-- Le styles -->
    <link href="http://twitter.github.com/bootstrap/assets/css/bootstrap.css" rel="stylesheet">
    <link href="http://twitter.github.com/bootstrap/assets/css/bootstrap-responsive.css" rel="stylesheet">
    <style>

    /* GLOBAL STYLES
    -------------------------------------------------- */
    /* Padding below the footer and lighter body text */

    body {
      padding-bottom: 40px;
      color: #5a5a5a;
    }



    /* CUSTOMIZE THE NAVBAR
    -------------------------------------------------- */

    /* Special class on .container surrounding .navbar, used for positioning it into place. */
    .navbar-wrapper {
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      z-index: 10;
      margin-top: 20px;
      margin-bottom: -90px; /* Negative margin to pull up carousel. 90px is roughly margins and height of navbar. */
    }
    .navbar-wrapper .navbar {

    }

    /* Remove border and change up box shadow for more contrast */
    .navbar .navbar-inner {
      border: 0;
      -webkit-box-shadow: 0 2px 10px rgba(0,0,0,.25);
         -moz-box-shadow: 0 2px 10px rgba(0,0,0,.25);
              box-shadow: 0 2px 10px rgba(0,0,0,.25);
    }

    /* Downsize the brand/project name a bit */
    .navbar .brand {
      padding: 14px 20px 16px; /* Increase vertical padding to match navbar links */
      font-size: 16px;
      font-weight: bold;
      text-shadow: 0 -1px 0 rgba(0,0,0,.5);
    }

    /* Navbar links: increase padding for taller navbar */
    .navbar .nav > li > a {
      padding: 15px 20px;
    }

    /* Offset the responsive button for proper vertical alignment */
    .navbar .btn-navbar {
      margin-top: 10px;
    }



    /* CUSTOMIZE THE NAVBAR
    -------------------------------------------------- */

    /* Carousel base class */
    .carousel {
      margin-bottom: 60px;
    }

    .carousel .container {
      position: relative;
      z-index: 9;
    }

    .carousel-control {
      height: 80px;
      margin-top: 0;
      font-size: 120px;
      text-shadow: 0 1px 1px rgba(0,0,0,.4);
      background-color: transparent;
      border: 0;
    }

    .carousel .item {
      height: 500px;
    }
    .carousel img {
      position: absolute;
      top: 0;
      left: 0;
      min-width: 100%;
      height: 500px;
    }

    .carousel-caption {
      background-color: transparent;
      position: static;
      max-width: 550px;
      padding: 0 20px;
      margin-top: 200px;
    }
    .carousel-caption h1,
    .carousel-caption .lead {
      margin: 0;
      line-height: 1.25;
      color: #fff;
      text-shadow: 0 1px 1px rgba(0,0,0,.4);
    }
    .carousel-caption .btn {
      margin-top: 10px;
    }



    /* MARKETING CONTENT
    -------------------------------------------------- */

    /* Center align the text within the three columns below the carousel */
    .marketing .span4 {
      text-align: center;
    }
    .marketing h2 {
      font-weight: normal;
    }
    .marketing .span4 p {
      margin-left: 10px;
      margin-right: 10px;
    }


    /* Featurettes
    ------------------------- */

    .featurette-divider {
      margin: 80px 0; /* Space out the Bootstrap <hr> more */
    }
    .featurette {
      padding-top: 120px; /* Vertically center images part 1: add padding above and below text. */
      overflow: hidden; /* Vertically center images part 2: clear their floats. */
    }
    .featurette-image {
      margin-top: -120px; /* Vertically center images part 3: negative margin up the image the same amount of the padding to center it. */
    }

    /* Give some space on the sides of the floated elements so text doesn't run right into it. */
    .featurette-image.pull-left {
      margin-right: 40px;
    }
    .featurette-image.pull-right {
      margin-left: 40px;
    }

    /* Thin out the marketing headings */
    .featurette-heading {
      font-size: 50px;
      font-weight: 300;
      line-height: 1;
      letter-spacing: -1px;
    }



    /* RESPONSIVE CSS
    -------------------------------------------------- */

    \@media (max-width: 979px) {

      .container.navbar-wrapper {
        margin-bottom: 0;
        width: auto;
      }
      .navbar-inner {
        border-radius: 0;
        margin: -20px 0;
      }

      .carousel .item {
        height: 500px;
      }
      .carousel img {
        width: auto;
        height: 500px;
      }

      .featurette {
        height: auto;
        padding: 0;
      }
      .featurette-image.pull-left,
      .featurette-image.pull-right {
        display: block;
        float: none;
        max-width: 40%;
        margin: 0 auto 20px;
      }
    }


    \@media (max-width: 767px) {

      .navbar-inner {
        margin: -20px;
      }

      .carousel {
        margin-left: -20px;
        margin-right: -20px;
      }
      .carousel .container {

      }
      .carousel .item {
        height: 300px;
      }
      .carousel img {
        height: 300px;
      }
      .carousel-caption {
        width: 65%;
        padding: 0 70px;
        margin-top: 100px;
      }
      .carousel-caption h1 {
        font-size: 30px;
      }
      .carousel-caption .lead,
      .carousel-caption .btn {
        font-size: 18px;
      }

      .marketing .span4 + .span4 {
        margin-top: 40px;
      }

      .featurette-heading {
        font-size: 30px;
      }
      .featurette .lead {
        font-size: 18px;
        line-height: 1.5;
      }

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



    <!-- NAVBAR
    ================================================== -->
    <div class="navbar-wrapper">
      <!-- Wrap the .navbar in .container to center it within the absolutely positioned parent. -->
      <div class="container">

        <div class="navbar navbar-inverse">
          <div class="navbar-inner">
            <!-- Responsive Navbar Part 1: Button for triggering responsive navbar (not covered in tutorial). Include responsive CSS to utilize. -->
            <a class="btn btn-navbar" data-toggle="collapse" data-target=".nav-collapse">
              <span class="icon-bar"></span>
              <span class="icon-bar"></span>
              <span class="icon-bar"></span>
            </a>
            <a class="brand" href="index.php">Harvix</a>
            <!-- Responsive Navbar Part 2: Place all navbar contents you want collapsed withing .navbar-collapse.collapse. -->
            <div class="nav-collapse collapse">
              <ul class="nav">
                <li><a href="games2.cgi">Top Games</a></li>
                <li><a href="games2.cgi?strategy">Strategy</a></li>
                <li><a href="games2.cgi?racing">Racing</a></li>
		<li><a href="games2.cgi?shooting">Shooting</a></li>
		<li><a href="games2.cgi?zombie">Zombie</a></li>
		<li><a href="games2.cgi?arcade">Arcade</a></li>
              </ul>
            </div><!--/.nav-collapse -->
          </div><!-- /.navbar-inner -->
        </div><!-- /.navbar -->

      </div> <!-- /.container -->
    </div><!-- /.navbar-wrapper -->



    <!-- Carousel
    ================================================== -->
    <div id="myCarousel" class="carousel slide">
      <div class="carousel-inner">
        <div class="item active">
	<img src="http://kidmania.files.wordpress.com/2012/06/plantsvszombies.jpg" width="100%" alt="">
          <div class="container">
            <div class="carousel-caption">
              <h1>Plants Vs. Zombies</h1>
              <a class="btn btn-large btn-primary" href="games2.cgi?zombie11">Play Now</a>
            </div>
          </div>
        </div>
	  <div class="item">          
	<img src="https://lh4.googleusercontent.com/-cl9TQrM2HMw/TW6tHvXT2pI/AAAAAAAAAhc/epswFeXpLR8/s1600/tower8.jpg" width="100%" alt="">
          <div class="container">
            <div class="carousel-caption">
              <h1>Warzone Tower Defense</h1>
              <a class="btn btn-large btn-primary" href="games2.cgi?2">Play Now</a>
            </div>
          </div>
        </div>
        <div class="item">
          <img src="http://cdn2.kongregate.com/game_icons/0025/7656/thumbnail_site.jpg?17844-op" width="100%" alt="">
          <div class="container">
            <div class="carousel-caption">
              <h1>Learn to Fly 2</h1>
              <a class="btn btn-large btn-primary" href="games2.cgi?3">Play Now</a>
            </div>
          </div>
        </div>
        <div class="item">
          <img src="http://cdn1.kongcdn.com/game_icons/0028/0121/CycloManiacs_Thumb_site.jpg?10535-op" width="100%" alt="">
          <div class="container">
            <div class="carousel-caption">
              <h1>CycloManiac</h1>
              <a class="btn btn-large btn-primary" href="games2.cgi?4">Play Now</a>
            </div>
          </div>
        </div>
<div class="item">
          <img src="http://cdn3.kongregate.com/game_icons/0026/8119/icon_coaster2_100_site.png?15265-op" width="100%" alt="">
          <div class="container">
            <div class="carousel-caption">
              <h1>Coaster Racer 2</h1>
              <a class="btn btn-large btn-primary" href="games2.cgi?6">Play Now</a>
            </div>
          </div>
        </div>
<div class="item">
          <img src="http://cdn4.kongregate.com/game_icons/0003/4247/100x75.jpg?5315-op" width="100%" alt="">
          <div class="container">
            <div class="carousel-caption">
              <h1>Destroyer of Worlds</h1>
              <a class="btn btn-large btn-primary" href="games2.cgi?7">Play Now</a>
            </div>
          </div>
        </div>
<div class="item">
          <img src="http://cdn1.kongregate.com/game_icons/0021/0029/125x100_site.png?24304-op" width="100%" alt="">
          <div class="container">
            <div class="carousel-caption">
              <h1>Collapse It</h1>
              <a class="btn btn-large btn-primary" href="games2.cgi?8">Play Now</a>
            </div>
          </div>
        </div>
<div class="item">
          <img src="http://cdn2.kongregate.com/game_icons/0014/1274/thumbnail.png?7548-op" width="100%" alt="">
          <div class="container">
            <div class="carousel-caption">
              <h1>Ski Maniacs</h1>
              <a class="btn btn-large btn-primary" href="games2.cgi?9">Play Now</a>
            </div>
          </div>
        </div>
<div class="item">
          <img src="http://cdn2.kongregate.com/game_icons/0016/2437/soccerballs_94x73.png?5382-op" width="100%" algt="">
          <div class="container">
            <div class="carousel-caption">
              <h1>Soccer Balls</h1>
              <a class="btn btn-large btn-primary" href="games2.cgi?10">Play Now</a>
            </div>
          </div>
        </div>
<div class="item">
          <img src="http://cdn3.kongregate.com/game_icons/0007/9773/penguinz_thumb_100x100.jpg?4019-op" width="100%" alt="">
          <div class="container">
            <div class="carousel-caption">
              <h1>Penguinz</h1>
              <a class="btn btn-large btn-primary" href="games2.cgi?11">Play Now</a>
            </div>
          </div>
        </div>
<div class="item">
          <img src="http://cdn2.kongregate.com/game_icons/0031/5056/125x100_site.jpg?7971-op" width="80%" algt="">
          <div class="container">
            <div class="carousel-caption">
              <h1>Legend of the Void</h1>
              <a class="btn btn-large btn-primary" href="games2.cgi?12">Play Now</a>
            </div>
          </div>
        </div>



      </div>
      <a class="left carousel-control" href="#myCarousel" data-slide="prev">&lsaquo;</a>
      <a class="right carousel-control" href="#myCarousel" data-slide="next">&rsaquo;</a>
    </div><!-- /.carousel -->



    <!-- Marketing messaging and featurettes
    ================================================== -->
    <!-- Wrap the rest of the page in another container to center all the content. -->

    <div class="container marketing">

<h2>Top Games:</h2>
          <div class="row-fluid">
            <ul class="thumbnails">
              <li class="span4">
                <div class="thumbnail">
                  <img src="http://www.thecoolestgames.net/content/icons/warzone-tower-defense-extended-icon-1.jpg" alt="">
                  <div class="caption">
                    <h3>Warzone Tower Defense</h3>
                    <p><a href="games2.cgi?2" class="btn btn-primary">Play Now</a></p>
                  </div>
                </div>
              </li>
              <li class="span4">
                <div class="thumbnail">
                  <img src="http://cdn2.kongregate.com/game_icons/0025/7656/thumbnail_site.jpg?17844-op" alt="">
                  <div class="caption">
                    <h3>Learn to Fly 2</h3>
                    <p><a href="games2.cgi?3" class="btn btn-primary">Play Now</a></p>
                  </div>
                </div>
              </li>
              <li class="span4">
                <div class="thumbnail">
                  <img src="http://cdn1.kongcdn.com/game_icons/0028/0121/CycloManiacs_Thumb_site.jpg?10535-op" alt="">
                  <div class="caption">
                    <h3>CycloManiac</h3>
                    <p><a href="games2.cgi?4" class="btn btn-primary">Play Now</a></p>
                  </div>
                </div>
              </li>
            </ul>
          </div>
   <div class="row-fluid">
            <ul class="thumbnails">
              <li class="span4">
                <div class="thumbnail">
                  <img src="http://cdn3.kongregate.com/game_icons/0026/8119/icon_coaster2_100_site.png?15265-op" alt="">
                  <div class="caption">
                    <h3>Coaster Racer 2</h3>
                    <p><a href="games2.cgi?6" class="btn btn-primary">Play Now</a></p>
                  </div>
                </div>
              </li>
              <li class="span4">
                <div class="thumbnail">
                  <img src="http://cdn4.kongregate.com/game_icons/0003/4247/100x75.jpg?5315-op" alt="">
                  <div class="caption">
                    <h3>Destroyer of Worlds</h3>
                    <p><a href="games2.cgi?7" class="btn btn-primary">Play Now</a></p>
                  </div>
                </div>
              </li>
              <li class="span4">
                <div class="thumbnail">
                  <img src="http://cdn1.kongregate.com/game_icons/0021/0029/125x100_site.png?24304-op" alt="">
                  <div class="caption">
                    <h3>Collapse It</h3>
                    <p><a href="games2.cgi?8" class="btn btn-primary">Play Now</a></p>
                  </div>
                </div>
              </li>
            </ul>
          </div>
   <div class="row-fluid">
            <ul class="thumbnails">
              <li class="span4">
                <div class="thumbnail">
                  <img src="http://cdn2.kongregate.com/game_icons/0014/1274/thumbnail.png?7548-op" alt="">
                  <div class="caption">
                    <h3>Ski Maniacs</h3>
                    <p><a href="games2.cgi?9" class="btn btn-primary">Play Now</a></p>
                  </div>
                </div>
              </li>
              <li class="span4">
                <div class="thumbnail">
                  <img src="http://cdn2.kongregate.com/game_icons/0016/2437/soccerballs_94x73.png?5382-op" alt="">
                  <div class="caption">
                    <h3>Soccer Balls</h3>
                    <p><a href="games2.cgi?10" class="btn btn-primary">Play Now</a></p>
                  </div>
                </div>
              </li>
              <li class="span4">
                <div class="thumbnail">
                  <img src="http://cdn3.kongregate.com/game_icons/0007/9773/penguinz_thumb_100x100.jpg?4019-op" alt="">
                  <div class="caption">
                    <h3>Penguinz</h3>
                    <p><a href="games2.cgi?11" class="btn btn-primary">Play Now</a></p>
                  </div>
                </div>
              </li>
            </ul>
          </div>
 <div class="row-fluid">
            <ul class="thumbnails">
              <li class="span4">
                <div class="thumbnail">
                  <img src="http://cdn2.kongregate.com/game_icons/0031/5056/125x100_site.jpg?7971-op" alt="">
                  <div class="caption">
                    <h3>Legend of the Void</h3>
                    <p><a href="games2.cgi?12" class="btn btn-primary">Play Now</a></p>
                  </div>
                </div>
              </li>
              <li class="span4">
                <div class="thumbnail">
                  <img src="http://cdn4.kongcdn.com/game_icons/0019/0478/thumb100x75.jpg?9359-op" alt="">
                  <div class="caption">
                    <h3>Gravitee Wars</h3>
                    <p><a href="games2.cgi?13" class="btn btn-primary">Play Now</a></p>
                  </div>
                </div>
              </li>
              <li class="span4">
                <div class="thumbnail">
                  <img src="http://cdn4.kongcdn.com/game_icons/0031/3382/game_thumb_site.png?18429-op" alt="">
                  <div class="caption">
                    <h3>Flaming Zombooka 3</h3>
                    <p><a href="games2.cgi?14" class="btn btn-primary">Play Now</a></p>
                  </div>
                </div>
              </li>
            </ul>
          </div>
 <div class="row-fluid">
            <ul class="thumbnails">
              <li class="span4">
                <div class="thumbnail">
                  <img src="http://cdn4.kongcdn.com/game_icons/0036/5922/formula2012_kong_site.png?28760-op" alt="">
                  <div class="caption">
                    <h3>Formula Racer 2012</h3>
                    <p><a href="games2.cgi?5" class="btn btn-primary">Play Now</a></p>
                  </div>
                </div>
              </li>
	</div>


	  <hr class="featurette-divider">


      <!-- FOOTER -->
      <footer>
        <p class="pull-right"><a href="#">Back to top</a></p>
        <p>&copy; 2012 Harvix</p>
      </footer>

    </div><!-- /.container -->



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
    <script>
      !function ($) {
        $(function(){
          // carousel demo
          $('#myCarousel').carousel()
        })
      }(window.jQuery)
    </script>
  </body>
</html>


EOF
;
}



if ( $page eq '2' )
{
print_header();
print"<h3>Warzone Tower Defense</h3>\n";
print"<embed type=\"application/x-shockwave-flash\" pluginspage=\"http://www.macromedia.com/go/getflashplayer\" src=\"http://towerdefense-games.com/images/games_3/warzone-tower-defense/warzone-tower-defense.swf\" quality=\"high\" name=\"warzone-tower-defense\" width=\"700\" height=\"500\"></embed>";
print_footer();
}

if ( $page eq '3' )
{
print_header();
print"<h3>Learn to Fly</h3>\n";
print"<embed width=\"700\" height=\"500\" base=\"http://external.kongregate-games.com/gamez/0011/5608/live/\" src=\"http://external.kongregate-games.com/gamez/0011/5608/live/embeddable_115608.swf\" type=\"application/x-shockwave-flash\"></embed>";
print_footer();
}

if ( $page eq '4' )
{
print_header();
print"<h3>CycloManiac</h3>\n";
print"<embed width=\"700\" height=\"500\" base=\"http://external.kongregate-games.com/gamez/0005/3442/live/\" src=\"http://external.kongregate-games.com/gamez/0005/3442/live/embeddable_53442.swf\" type=\"application/x-shockwave-flash\"></embed>";
print_footer();
}

if ( $page eq '5' )
{
print_header();
print"<h3>Formula Racer 2012</h3>\n";
print"<embed width=\"700\" height=\"500\" base=\"http://external.kongregate-games.com/gamez/0014/2671/live/\" src=\"http://external.kongregate-games.com/gamez/0014/2671/live/embeddable_142671.swf\" type=\"application/x-shockwave-flash\"></embed>";
print_footer();
}

if ( $page eq '6' )
{
print_header();
print"<h3>Coaster Racer 2</h3>\n";
print"<embed width=\"700\" height=\"500\" base=\"http://external.kongregate-games.com/gamez/0011/8219/live/\" src=\"http://external.kongregate-games.com/gamez/0011/8219/live/embeddable_118219.swf\" type=\"application/x-shockwave-flash\"></embed>";
print_footer();
}

if ( $page eq '7' )
{
print_header();
print"<h3>Destroyer of Worlds</h3>\n";
print"<embed width=\"700\" height=\"500\" base=\"http://external.kongregate-games.com/gamez/0001/7831/live/\" src=\"http://external.kongregate-games.com/gamez/0001/7831/live/embeddable_17831.swf\" type=\"application/x-shockwave-flash\"></embed>";
print_footer();
}

if ( $page eq '8' )
{
print_header();
print"<h3>Collapse it</h3>\n";
print"<embed width=\"700\" height=\"500\" base=\"http://external.kongregate-games.com/gamez/0010/3695/live/\" src=\"http://external.kongregate-games.com/gamez/0010/3695/live/embeddable_103695.swf\" type=\"application/x-shockwave-flash\"></embed>";
print_footer();
}


if ( $page eq '9' )
{
print_header();
print"<h3>Ski Maniacs</h3>\n";
print"<embed width=\"700\" height=\"500\" base=\"http://external.kongregate-games.com/gamez/0007/1433/live/\" src=\"http://external.kongregate-games.com/gamez/0007/1433/live/embeddable_71433.swf\" type=\"application/x-shockwave-flash\"></embed>";
print_footer();
}


if ( $page eq '10' )
{
print_header();
print"<h3>Soccer Balls</h3>\n";
print"<embed width=\"700\" height=\"500\" base=\"http://external.kongregate-games.com/gamez/0008/2051/live/\" src=\"http://external.kongregate-games.com/gamez/0008/2051/live/embeddable_82051.swf\" type=\"application/x-shockwave-flash\"></embed>";
print_footer();
}

if ( $page eq '11' )
{
print_header();
print"<h3>Penguinz</h3>\n";
print"<embed width=\"700\" height=\"500\" base=\"http://external.kongregate-games.com/gamez/0004/0599/live/\" src=\"http://external.kongregate-games.com/gamez/0004/0599/live/embeddable_40599.swf\" type=\"application/x-shockwave-flash\"></embed>";
print_footer();
}

if ( $page eq '12' )
{
print_header();
print"<h3>Legend of the Void</h3>\n";
print"<embed width=\"700\" height=\"500\" base=\"http://external.kongregate-games.com/gamez/0012/9964/live/\" src=\"http://external.kongregate-games.com/gamez/0012/9964/live/embeddable_129964.swf\" type=\"application/x-shockwave-flash\">";
print_footer();
}

if ( $page eq '13' )
{
print_header();
print"<h3>Gravitee Wars</h3>\n";
print"<embed width=\"700\" height=\"500\" base=\"http://external.kongregate-games.com/gamez/0009/6087/live/\" src=\"http://external.kongregate-games.com/gamez/0009/6087/live/embeddable_96087.swf\" type=\"application/x-shockwave-flash\"></embed>";
print_footer();
}

if ( $page eq '14' )
{
print_header();
print"<h3>Flaming Zombooka 3</h3>\n";
print"<embed width=\"700\" height=\"500\" base=\"http://external.kongregate-games.com/gamez/0009/7363/live/\" src=\"http://external.kongregate-games.com/gamez/0009/7363/live/embeddable_97363.swf\" type=\"application/x-shockwave-flash\"></embed>";
print_footer();
}

if ( $page eq 'strategy1' )
{
print_header();
print"<h3>Bloom Defender</h3>\n";
print"<center><object classid=\"clsid:d27cdb6e-ae6d-11cf-96b8-444553540000\" width=\"700\" height=\"500\" align=\"middle\" id=\"Bloom-Defender\"><param name=\"movie\" value=\"http://www.qiqifiles.com/gameslist/16/Bloom-Defender.swf\"><param name=\"quality\" value=\"high\"><param name=\"AllowScriptAccess\" value=\"always\"><!--[if !IE]>--><object type=\"application/x-shockwave-flash\" data=\"http://www.qiqifiles.com/gameslist/16/Bloom-Defender.swf\" width=\"700\" height=\"500\"><param name=\"movie\" value=\"http://www.qiqifiles.com/gameslist/16/Bloom-Defender.swf\"><param name=\"quality\" value=\"high\"><param name=\"AllowScriptAccess\" value=\"always\"><!--<![endif]--><a href=\"http://www.adobe.com/go/getflash\"><img src=\"http://www.adobe.com/images/shared/download_buttons/get_flash_player.gif\" alt=\"Get Adobe Flash Player\"></a><!--[if !IE]>--></object><!--<![endif]--></object><br><!--Please keep the link be visible and don't change the link, otherwise your site may be disabled to hotlink our games.-->Play <a href='http://www.gameslist.com' target='_blank'><b>New Games</b></a> at GamesList.com</center>";
print_footer();
}

if ( $page eq 'strategy2' )
{
print_header();
print"<h3>Mythic Fort Defense</h3>\n";
print"<center><object classid=\"clsid:d27cdb6e-ae6d-11cf-96b8-444553540000\" width=\"700\" height=\"500\" align=\"middle\" id=\"Mythic-Fort-Defense\"><param name=\"movie\" value=\"http://www.qiqifiles.com/gameslist/17/Mythic-Fort-Defense.swf\"><param name=\"quality\" value=\"high\"><param name=\"AllowScriptAccess\" value=\"always\"><!--[if !IE]>--><object type=\"application/x-shockwave-flash\" data=\"http://www.qiqifiles.com/gameslist/17/Mythic-Fort-Defense.swf\" width=\"700\" height=\"500\"><param name=\"movie\" value=\"http://www.qiqifiles.com/gameslist/17/Mythic-Fort-Defense.swf\"><param name=\"quality\" value=\"high\"><param name=\"AllowScriptAccess\" value=\"always\"><!--<![endif]--><a href=\"http://www.adobe.com/go/getflash\"><img src=\"http://www.adobe.com/images/shared/download_buttons/get_flash_player.gif\" alt=\"Get Adobe Flash Player\"></a><!--[if !IE]>--></object><!--<![endif]--></object><br><!--Please keep the link be visible and don't change the link, otherwise your site may be disabled to hotlink our games.--><a href='http://www.gameslist.com' target='_blank'><b>Play Game</b></a> at GamesList.com</center>";
print_footer();
}

if ( $page eq 'strategy3' )
{
print_header();
print"<h3>Monster Slayer</h3>\n";
print"<embed width=\"700\" height=\"500\" base=\"http://external.kongregate-games.com/gamez/0009/2661/live/\" src=\"http://external.kongregate-games.com/gamez/0009/2661/live/embeddable_92661.swf\" type=\"application/x-shockwave-flash\"></embed>";
print_footer();
}

if ( $page eq 'strategy4' )
{
print_header();
print"<h3>Warlords: Call to Arms</h3>\n";
print"<embed width=\"700\" height=\"500\" base=\"http://external.kongregate-games.com/gamez/0000/8598/live/\" src=\"http://external.kongregate-games.com/gamez/0000/8598/live/embeddable_8598.swf\" type=\"application/x-shockwave-flash\"></embed>";
print_footer();
}

if ( $page eq 'strategy5' )
{
print_header();
print"<h3>Protector</h3>\n";
print"<embed width=\"700\" height=\"600\" base=\"http://external.kongregate-games.com/gamez/0000/6554/live/\" src=\"http://external.kongregate-games.com/gamez/0000/6554/live/embeddable_6554.swf\" type=\"application/x-shockwave-flash\"></embed>";
print_footer();
}

if ( $page eq 'strategy6' )
{
print_header();
print"<h3>Orbital Onslaught</h3>\n";
print"<embed width=\"700\" height=\"500\" base=\"http://external.kongregate-games.com/gamez/0010/9276/live/\" src=\"http://external.kongregate-games.com/gamez/0010/9276/live/embeddable_109276.swf\" type=\"application/x-shockwave-flash\"></embed>";
print_footer();
}

if ( $page eq 'strategy7' )
{
print_header();
print"<h3>Dungeon Defender</h3>\n";
print"<embed width=\"700\" height=\"500\" base=\"http://external.kongregate-games.com/gamez/0001/0869/live/\" src=\"http://external.kongregate-games.com/gamez/0001/0869/live/embeddable_10869.swf\" type=\"application/x-shockwave-flash\"></embed>";
print_footer();
}

if ( $page eq 'strategy8' )
{
print_header();
print"<h3>Battalion: Nemesis</h3>\n";
print"<embed width=\"700\" height=\"500\" base=\"http://external.kongregate-games.com/gamez/0002/2054/live/\" src=\"http://external.kongregate-games.com/gamez/0002/2054/live/embeddable_22054.swf\" type=\"application/x-shockwave-flash\"></embed>";
print_footer();
}

if ( $page eq 'strategy9' )
{
print_header();
print"<h3>The Osiris Conflict</h3>\n";
print"<embed width=\"700\" height=\"500\" base=\"http://external.kongregate-games.com/gamez/0011/8725/live/\" src=\"http://external.kongregate-games.com/gamez/0011/8725/live/embeddable_118725.swf\" type=\"application/x-shockwave-flash\"></embed>";
print_footer();
}

if ( $page eq 'strategy10' )
{
print_header();
print"<h3>Necropolis Defence</h3>\n";
print"<embed width=\"700\" height=\"500\" base=\"http://external.kongregate-games.com/gamez/0012/6091/live/\" src=\"http://external.kongregate-games.com/gamez/0012/6091/live/embeddable_126091.swf\" type=\"application/x-shockwave-flash\"></embed>";
print_footer();
}

if ( $page eq 'strategy11' )
{
print_header();
print"<h3>FurEyes Base Defence</h3>\n";
print"<embed width=\"700\" height=\"500\" base=\"http://external.kongregate-games.com/gamez/0007/3226/live/\" src=\"http://external.kongregate-games.com/gamez/0007/3226/live/embeddable_73226.swf\" type=\"application/x-shockwave-flash\"></embed>";
print_footer();
}

if ( $page eq 'strategy12' )
{
print_header();
print"<h3>Invasion From Hell</h3>\n";
print"<embed width=\"700\" height=\"500\" base=\"http://external.kongregate-games.com/gamez/0003/4551/live/\" src=\"http://external.kongregate-games.com/gamez/0003/4551/live/embeddable_34551.swf\" type=\"application/x-shockwave-flash\"></embed>";
print_footer();
}

if ( $page eq 'racing1' )
{
print_header();
print"<h3>V8 Muscle Cars</h3>\n";
print"<embed width=\"700\" height=\"500\" base=\"http://external.kongregate-games.com/gamez/0015/6422/live/\" src=\"http://external.kongregate-games.com/gamez/0015/6422/live/embeddable_156422.swf\" type=\"application/x-shockwave-flash\"></embed>";
print_footer();
}

if ( $page eq 'racing2' )
{
print_header();
print"<h3>Coaster Racer 2</h3>\n";
print"<embed width=\"700\" height=\"500\" base=\"http://external.kongregate-games.com/gamez/0011/8219/live/\" src=\"http://external.kongregate-games.com/gamez/0011/8219/live/embeddable_118219.swf\" type=\"application/x-shockwave-flash\"></embed>";
print_footer();
}

if ( $page eq 'racing3' )
{
print_header();
print"<h3>Formula Racer 2012</h3>\n";
print"<embed width=\"700\" height=\"500\" base=\"http://external.kongregate-games.com/gamez/0014/2671/live/\" src=\"http://external.kongregate-games.com/gamez/0014/2671/live/embeddable_142671.swf\" type=\"application/x-shockwave-flash\"></embed>";
print_footer();
}

if ( $page eq 'racing4' )
{
print_header();
print"<h3>Drift Runners</h3>\n";
print"<embed width=\"700\" height=\"500\" base=\"http://external.kongregate-games.com/gamez/0003/9130/live/\" src=\"http://external.kongregate-games.com/gamez/0003/9130/live/embeddable_39130.swf\" type=\"application/x-shockwave-flash\"></embed>";
print_footer();
}

if ( $page eq 'racing5' )
{
print_header();
print"<h3>Hot Rod Racing</h3>\n";
print"<embed width=\"700\" height=\"500\" base=\"http://external.kongregate-games.com/gamez/0013/7325/live/\" src=\"http://external.kongregate-games.com/gamez/0013/7325/live/embeddable_137325.swf\" type=\"application/x-shockwave-flash\"></embed>";
print_footer();
}

if ( $page eq 'racing6' )
{
print_header();
print"<h3>American Racing</h3>\n";
print"<embed width=\"700\" height=\"500\" base=\"http://external.kongregate-games.com/gamez/0015/6925/live/\" src=\"http://external.kongregate-games.com/gamez/0015/6925/live/embeddable_156925.swf\" type=\"application/x-shockwave-flash\"></embed>";
print_footer();
}

if ( $page eq 'racing7' )
{
print_header();
print"<h3>Neon Race 2</h3>\n";
print"<embed width=\"700\" height=\"500\" base=\"http://external.kongregate-games.com/gamez/0013/7834/live/\" src=\"http://external.kongregate-games.com/gamez/0013/7834/live/embeddable_137834.swf\" type=\"application/x-shockwave-flash\"></embed>";
print_footer();
}

if ( $page eq 'racing8' )
{
print_header();
print"<h3>Grand Prix Pro</h3>\n";
print"<embed width=\"700\" height=\"500\" base=\"http://external.kongregate-games.com/gamez/0011/5460/live/\" src=\"http://external.kongregate-games.com/gamez/0011/5460/live/embeddable_115460.swf\" type=\"application/x-shockwave-flash\"></embed>";
print_footer();
}

if ( $page eq 'racing9' )
{
print_header();
print"<h3>Space Punk Racer</h3>\n";
print"<embed width=\"700\" height=\"500\" base=\"http://external.kongregate-games.com/gamez/0012/4902/live/\" src=\"http://external.kongregate-games.com/gamez/0012/4902/live/embeddable_124902.swf\" type=\"application/x-shockwave-flash\"></embed>";
print_footer();
}

if ( $page eq 'racing10' )
{
print_header();
print"<h3>Coast Runners</h3>\n";
print"<embed width=\"700\" height=\"500\" base=\"http://external.kongregate-games.com/gamez/0010/6635/live/\" src=\"http://external.kongregate-games.com/gamez/0010/6635/live/embeddable_106635.swf\" type=\"application/x-shockwave-flash\"></embed>";
print_footer();
}

if ( $page eq 'racing11' )
{
print_header();
print"<h3>HyperDrive X</h3>\n";
print"<embed width=\"700\" height=\"500\" base=\"http://external.kongregate-games.com/gamez/0002/0575/live/\" src=\"http://external.kongregate-games.com/gamez/0002/0575/live/embeddable_20575.swf\" type=\"application/x-shockwave-flash\"></embed>";
print_footer();
}

if ( $page eq 'racing12' )
{
print_header();
print"<h3>Rudolphs Red Race</h3>\n";
print"<embed width=\"700\" height=\"500\" base=\"http://external.kongregate-games.com/gamez/0003/2188/live/\" src=\"http://external.kongregate-games.com/gamez/0003/2188/live/embeddable_32188.swf\" type=\"application/x-shockwave-flash\"></embed>";
print_footer();
}

if ( $page eq 'shooting1' )
{
print_header();
print"<h3>Heavy Weapons</h3>\n";
print"<embed width=\"700\" height=\"500\" base=\"http://external.kongregate-games.com/gamez/0004/5284/live/\" src=\"http://external.kongregate-games.com/gamez/0004/5284/live/embeddable_45284.swf\" type=\"application/x-shockwave-flash\"></embed>";
print_footer();
}

if ( $page eq 'shooting2' )
{
print_header();
print"<h3>Penguinz</h3>\n";
print"<embed width=\"700\” height=\"500\" base=\"http://external.kongregate-games.com/gamez/0004/0599/live/\" src=\"http://external.kongregate-games.com/gamez/0004/0599/live/embeddable_40599.swf\" type=\"application/x-shockwave-flash\"></embed>";
print_footer();
}

if ( $page eq 'shooting3' )
{
print_header();
print"<h3>Dead Metal</h3>\n";
print"<embed width=\"700\" height=\"500\" base=\"http://external.kongregate-games.com/gamez/0012/3789/live/\" src=\"http://external.kongregate-games.com/gamez/0012/3789/live/embeddable_123789.swf\" type=\"application/x-shockwave-flash\"></embed>";
print_footer();
}

if ( $page eq 'shooting4' )
{
print_header();
print"<h3>Jack the Fugitive</h3>\n";
print"<embed width=\"700\" height=\"500\" base=\"http://external.kongregate-games.com/gamez/0000/8850/live/\" src=\"http://external.kongregate-games.com/gamez/0000/8850/live/embeddable_8850.swf\" type=\"application/x-shockwave-flash\"></embed>";
print_footer();
}

if ( $page eq 'shooting5' )
{
print_header();
print"<h3>Hostage Crisis</h3>\n";
print"<embed width=\"700\" height=\"500\" base=\"http://external.kongregate-games.com/gamez/0009/5626/live/\" src=\"http://external.kongregate-games.com/gamez/0009/5626/live/embeddable_95626.swf\" type=\"application/x-shockwave-flash\"></embed>";
print_footer();
}

if ( $page eq 'shooting6' )
{
print_header();
print"<h3>Vital Bloodshed</h3>\n";
print"<embed width=\"700\" height=\"500\" base=\"http://external.kongregate-games.com/gamez/0011/1831/live/\" src=\"http://external.kongregate-games.com/gamez/0011/1831/live/embeddable_111831.swf\" type=\"application/x-shockwave-flash\"></embed>";
print_footer();
}

if ( $page eq 'shooting7' )
{
print_header();
print"<h3>MAD: Mutually Assured Destruction</h3>\n";
print"<embed width=\"700\" height=\"500\" base=\"http://external.kongregate-games.com/gamez/0000/5196/live/\" src=\"http://external.kongregate-games.com/gamez/0000/5196/live/embeddable_5196.swf\" type=\"application/x-shockwave-flash\"></embed>";
print_footer();
}

if ( $page eq 'shooting8' )
{
print_header();
print"<h3>Red Fluxion</h3>\n";
print"<embed width=\"700\" height=\"500\" base=\"http://external.kongregate-games.com/gamez/0006/1595/live/\" src=\"http://external.kongregate-games.com/gamez/0006/1595/live/embeddable_61595.swf\" type=\"application/x-shockwave-flash\"></embed>";
print_footer();
}

if ( $page eq 'shooting9' )
{
print_header();
print"<h3>Gun Express</h3>\n";
print"<embed width=\"700\" height=\"500\" base=\"http://external.kongregate-games.com/gamez/0008/6188/live/\" src=\"http://external.kongregate-games.com/gamez/0008/6188/live/embeddable_86188.swf\" type=\"application/x-shockwave-flash\"></embed>";
print_footer();
}

if ( $page eq 'shooting10' )
{
print_header();
print"<h3>Army of Destruction</h3>\n";
print"<embed width=\"700\" height=\"500\" base=\"http://external.kongregate-games.com/gamez/0000/3624/live/\" src=\"http://external.kongregate-games.com/gamez/0000/3624/live/embeddable_3624.swf\" type=\"application/x-shockwave-flash\"></embed>";
print_footer();
}

if ( $page eq 'shooting11' )
{
print_header();
print"<h3>Twisted Military</h3>\n";
print"<embed width=\"700\" height=\"500\" base=\"http://external.kongregate-games.com/gamez/0004/2629/live/\" src=\"http://external.kongregate-games.com/gamez/0004/2629/live/embeddable_42629.swf\" type=\"application/x-shockwave-flash\"></embed>";
print_footer();
}

if ( $page eq 'shooting12' )
{
print_header();
print"<h3>WWII Killer</h3>\n";
print"<object width=\"700\" height=\"500\"><param name=\"movie\" value=\"http://www.fupa.com/swf/wwii-killer/WWII_Killer.swf\"></param><embed src=\"http://www.fupa.com/swf/wwii-killer/WWII_Killer.swf\" type=\"application/x-shockwave-flash\" width=\"700\" height=\"500\"></embed></object>";
print_footer();
}

if ( $page eq 'zombie1' )
{
print_header();
print"<h3>Duse and Zombies</h3>\n";
print"<embed width=\"700\" height=\"500\" base=\"http://external.kongregate-games.com/gamez/0011/8810/live/\" src=\"http://external.kongregate-games.com/gamez/0011/8810/live/embeddable_118810.swf\" type=\"application/x-shockwave-flash\"></embed>";
print_footer();
}

if ( $page eq 'zombie2' )
{
print_header();
print"<h3>Nuclear Outrun</h3>\n";
print"<embed width=\"700\" height=\"500\" base=\"http://external.kongregate-games.com/gamez/0014/3076/live/\" src=\"http://external.kongregate-games.com/gamez/0014/3076/live/embeddable_143076.swf\" type=\"application/x-shockwave-flash\"></embed>";
print_footer();
}


if ( $page eq 'zombie3' )
{
print_header();
print"<h3>Flaming Zombooka 2</h3>\n";
print"<embed width=\"700\" height=\"500\" base=\"http://external.kongregate-games.com/gamez/0009/7363/live/\" src=\"http://external.kongregate-games.com/gamez/0009/7363/live/embeddable_97363.swf\" type=\"application/x-shockwave-flash\"></embed>";
print_footer();
}


if ( $page eq 'zombie4' )
{
print_header();
print"<h3>Robots vs. Zombies</h3>\n";
print"<embed width=\"700\" height=\"500\" base=\"http://external.kongregate-games.com/gamez/0011/8407/live/\" src=\"http://external.kongregate-games.com/gamez/0011/8407/live/embeddable_118407.swf\" type=\"application/x-shockwave-flash\"></embed>";
print_footer();
}


if ( $page eq 'zombie5' )
{
print_header();
print"<h3>Zombie Mice Annihilation</h3>\n";
print"<embed width=\"700\" height=\"500\" base=\"http://external.kongregate-games.com/gamez/0008/5391/live/\" src=\"http://external.kongregate-games.com/gamez/0008/5391/live/embeddable_85391.swf\" type=\"application/x-shockwave-flash\"></embed>";
print_footer();
}

if ( $page eq 'zombie6' )
{
print_header();
print"<h3>Zombie Infestation: Strain 116</h3>\n";
print"<embed width=\"700\" height=\"500\" base=\"http://external.kongregate-games.com/gamez/0003/8399/live/\" src=\"http://external.kongregate-games.com/gamez/0003/8399/live/embeddable_38399.swf\" type=\"application/x-shockwave-flash\"></embed>";
print_footer();
}

if ( $page eq 'zombie7' )
{
print_header();
print"<h3>Truckminator</h3>\n";
print"<embed width=\"700\" height=\"500\" base=\"http://external.kongregate-games.com/gamez/0013/8056/live/\" src=\"http://external.kongregate-games.com/gamez/0013/8056/live/embeddable_138056.swf\" type=\"application/x-shockwave-flash\"></embed>";
print_footer();
}

if ( $page eq 'zombie8' )
{
print_header();
print"<h3>Flaming Zombooka 3 : Carnival</h3>\n";
print"<embed width=\"700\" height=\"500\" base=\"http://external.kongregate-games.com/gamez/0012/9545/live/\" src=\"http://external.kongregate-games.com/gamez/0012/9545/live/embeddable_129545.swf\" type=\"application/x-shockwave-flash\"></embed>";
print_footer();
}

if ( $page eq 'zombie9' )
{
print_header();
print"<h3>Zombie Shootout</h3>\n";
print"<object classid=\"clsid:d27cdb6e-ae6d-11cf-96b8-444553540000\" codebase=\"http://fpdownload.macromedia.com/pub/shockwave/cabs/flash/swflash.cab#version=10,0,0,0\" id=\"gameObject\" width=\"700\" height=\"500\"><param name=\"movie\" value=\"/newGames/shooting-games/boxheadthezombiewars/boxheadthezombiewars_w.swf\"/><param name=\"menu\" value=\"false\"/><param name=\"allowscriptaccess\" value=\"samedomain\"/><param name=\"allownetworking\" value=\"all\"/><embed src=\"/newGames/shooting-games/boxheadthezombiewars/boxheadthezombiewars_w.swf\" width=\"700\" height=\"500\" menu=\"false\"  allowscriptaccess=\"samedomain\" allownetworking=\"all\" name=\"gameObject\" type=\"application/x-shockwave-flash\" pluginspage=\"http://www.macromedia.com/go/getflashplayer\"></embed></object>";
print_footer();
}

if ( $page eq 'zombie10' )
{
print_header();
print"<h3>Zombies can Fly</h3>\n";
print"<object classid=\"clsid:d27cdb6e-ae6d-11cf-96b8-444553540000\" codebase=\"http://fpdownload.macromedia.com/pub/shockwave/cabs/flash/swflash.cab#version=10,0,0,0\" width=\"700\" height=\"500\"><param name=\"allowScriptAccess\" value=\"sameDomain\"><param name=\"movie\" value=\"http://www.hairygames.com/files/flash/games/zombies-can-fly.swf\"><param name=\"quality\" value=\"high\"><embed src=\"http://www.hairygames.com/files/flash/games/zombies-can-fly.swf\" quality=\"high\" width=\"700\" height=\"500\" allowScriptAccess=\"sameDomain\" type=\"application/x-shockwave-flash\" pluginspage=\"http://www.macromedia.com/go/getflashplayer\"></embed></object>";
print_footer();
}

if ( $page eq 'zombie11' )
{
print_header();
print"<h3>Plants vs. Zombies</h3>\n";
print"<iframe src=\"http://www.gamezhero.com/get-game-code/f35a2bc72dfdc2aae569a0c7370bd7f5\" id=\"game_frame\" name=\"game_frame\" width=\"700\" height=\"500\" align=\"middle\" scrolling=\"No\" frameborder=\"0\"></iframe>";
print_footer();
}

if ( $page eq 'zombie12' )
{
print_header();
print"<h3>Zombocalypse</h3>\n";
print"<object width=\"700\" height=\"500\">
<param name=\"movie\" value=\"http://www.mad4flash.com/games/zombocalypse.swf\">
<embed src=\"http://www.mad4flash.com/games/zombocalypse.swf\" width=\"700\" height=\"400\"></embed></object>";
print_footer();
}

if ( $page eq 'arcade1' )
{
print_header();
print"<h3>Space Invaders</h3>\n";
print"<script type=\"text/javascript\" src=\"http://cdn.widgetserver.com/syndication/subscriber/InsertWidget.js\"></script><script type=\"text/javascript\">if (WIDGETBOX) WIDGETBOX.renderWidget(\'206ea855-d81d-4811-b8a6-4a846cd2fcbc\');</script>
<noscript>Get the <a href=\"http://www.widgetbox.com/widget/space-invaders\">Space Invaders</a> widget and many other <a href=\"http://www.widgetbox.com/\">great free widgets</a> at <a href=\"http://www.widgetbox.com\">Widgetbox</a>! Not seeing a widget? (<a href=\"http://support.widgetbox.com/\">More info</a>)</noscript>";
print_footer();
}

if ( $page eq 'arcade2' )
{
print_header();
print"<h3>Snake</h3>\n";
print"<script type=\"text/javascript\" src=\"http://cdn.widgetserver.com/syndication/subscriber/InsertWidget.js\"></script><script type=\"text/javascript\">if (WIDGETBOX) WIDGETBOX.renderWidget(\'dc942879-6076-40cc-acae-34c02d4d5ed9\');</script>
<noscript>Get the <a href=\"http://www.widgetbox.com/widget/snake\">Snake</a> widget and many other <a href=\"http://www.widgetbox.com/\">great free widgets</a> at <a href=\"http://www.widgetbox.com\">Widgetbox</a>! Not seeing a widget? (<a href=\"http://support.widgetbox.com/\">More info</a>)</noscript>
";
print_footer();
}

if ( $page eq 'arcade3' )
{
print_header();
print"<h3>Frogger</h3>\n";
print"<script type=\"text/javascript\" src=\"http://cdn.widgetserver.com/syndication/subscriber/InsertWidget.js\"></script><script type=\"text/javascript\">if (WIDGETBOX) WIDGETBOX.renderWidget(\'89ba79e7-8542-4cf6-9b87-3be2a3e9a263\');</script>
<noscript>Get the <a href=\"http://www.widgetbox.com/widget/neave-frogger\">Frogger</a> widget and many other <a href=\"http://www.widgetbox.com/\">great free widgets</a> at <a href=\"http://www.widgetbox.com\">Widgetbox</a>! Not seeing a widget? (<a href=\"http://support.widgetbox.com/\">More info</a>)</noscript>";
print_footer();
}

if ( $page eq 'arcade4' )
{
print_header();
print"<h3>Pong</h3>\n";
print"<script type=\"text/javascript\" src=\"http://cdn.widgetserver.com/syndication/subscriber/InsertWidget.js\"></script><script type=\"text/javascript\">if (WIDGETBOX) WIDGETBOX.renderWidget(\'3fd12a10-0db7-49b7-a1ca-30f2660650f9\');</script>
<noscript>Get the <a href=\"http://www.widgetbox.com/widget/pong\">Pong</a> widget and many other <a href=\"http://www.widgetbox.com/\">great free widgets</a> at <a href=\"http://www.widgetbox.com\">Widgetbox</a>! Not seeing a widget? (<a href=\"http://support.widgetbox.com/\">More info</a>)</noscript>";
print_footer();
}

if ( $page eq 'arcade5' )
{
print_header();
print"<h3>Hexxagon</h3>\n";
print"<script type=\"text/javascript\" src=\"http://cdn.widgetserver.com/syndication/subscriber/InsertWidget.js\"></script><script type=\"text/javascript\">if (WIDGETBOX) WIDGETBOX.renderWidget(\'9bdc823b-b2a5-43f4-b2dd-fb1e1bcc88a3\');</script>
<noscript>Get the <a href=\"http://www.widgetbox.com/widget/hexxagon\">Hexxagon</a> widget and many other <a href=\"http://www.widgetbox.com/\">great free widgets</a> at <a href=\"http://www.widgetbox.com\">Widgetbox</a>! Not seeing a widget? (<a href=\"http://support.widgetbox.com/\">More info</a>)</noscript>";
print_footer();
}

if ( $page eq 'arcade6' )
{
print_header();
print"<h3>Asteriods</h3>\n";
print"<script type=\"text/javascript\" src=\"http://cdn.widgetserver.com/syndication/subscriber/InsertWidget.js\"></script><script type=\"text/javascript\">if (WIDGETBOX) WIDGETBOX.renderWidget(\'8d127d35-bfac-4efa-89c1-e3d56fa7ff89\');</script>
<noscript>Get the <a href=\"http://www.widgetbox.com/widget/asteroids\">Asteroids</a> widget and many other <a href=\"http://www.widgetbox.com/\">great free widgets</a> at <a href=\"http://www.widgetbox.com\">Widgetbox</a>! Not seeing a widget? (<a href=\"http://support.widgetbox.com/\">More info</a>)</noscript>";
print_footer();
}

if ( $page eq 'arcade7' )
{
print_header();
print"<h3>Tic-Tac-Toe</h3>\n";
print"<script type=\"text/javascript\" src=\"http://cdn.widgetserver.com/syndication/subscriber/InsertWidget.js\"></script><script type=\"text/javascript\">if (WIDGETBOX) WIDGETBOX.renderWidget(\'891845d3-3517-4d33-b981-bcfbe26847cc\');</script>
<noscript>Get the <a href=\"http://www.widgetbox.com/widget/tictactoe\">Tic-Tac-Toe</a> widget and many other <a href=\"http://www.widgetbox.com/\">great free widgets</a> at <a href=\"http://www.widgetbox.com\">Widgetbox</a>! Not seeing a widget? (<a href=\"http://support.widgetbox.com/\">More info</a>)</noscript>";
print_footer();
}
if ( $page eq 'arcade8' )
{
print_header();
print"<h3>Donkey Kong</h3>\n";
print"<script type=\"text/javascript\" src=\"http://cdn.widgetserver.com/syndication/subscriber/InsertWidget.js\"></script><script type=\"text/javascript\">if (WIDGETBOX) WIDGETBOX.renderWidget(\'bdb4e76e-17b8-42bd-8a6b-63af9b9a8c1a\');</script>
<noscript>Get the <a href=\"http://www.widgetbox.com/widget/donkey-kong\">Donkey Kong</a> widget and many other <a href=\"http://www.widgetbox.com/\">great free widgets</a> at <a href=\"http://www.widgetbox.com\">Widgetbox</a>! Not seeing a widget? (<a href=\"http://support.widgetbox.com/\">More info</a>)</noscript>";
print_footer();
}

if ( $page eq 'arcade9' )
{
print_header();
print"<h3>Crazy Taxi</h3>\n";
print"<script type=\"text/javascript\" src=\"http://cdn.widgetserver.com/syndication/subscriber/InsertWidget.js\"></script><script type=\"text/javascript\">if (WIDGETBOX) WIDGETBOX.renderWidget(\'0d574159-b58a-4a27-9554-39f29fdfda1b\');</script>
<noscript>Get the <a href=\"http://www.widgetbox.com/widget/crazy-taxi-primarygames\">Crazy Taxi</a> widget and many other <a href=\"http://www.widgetbox.com/\">great free widgets</a> at <a href=\"http://www.widgetbox.com\">Widgetbox</a>! Not seeing a widget? (<a href=\"http://support.widgetbox.com/\">More info</a>)</noscript>";
print_footer();
}

if ( $page eq 'strategy' )
{
print <<EOX


<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Harvix Games</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Harvix free online  Games">
    <meta name="author" content="Harvix Search">

    <!-- Le styles -->
    <link href="http://twitter.github.com/bootstrap/assets/css/bootstrap.css" rel="stylesheet">
    <link href="http://twitter.github.com/bootstrap/assets/css/bootstrap-responsive.css" rel="stylesheet">
    <style>

    /* GLOBAL STYLES
    -------------------------------------------------- */
    /* Padding below the footer and lighter body text */

    body {
      padding-bottom: 40px;
      color: #5a5a5a;
    }



    /* CUSTOMIZE THE NAVBAR
    -------------------------------------------------- */

    /* Special class on .container surrounding .navbar, used for positioning it into place. */
    .navbar-wrapper {
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      z-index: 10;
      margin-top: 20px;
      margin-bottom: -90px; /* Negative margin to pull up carousel. 90px is roughly margins and height of navbar. */
    }
    .navbar-wrapper .navbar {

    }

    /* Remove border and change up box shadow for more contrast */
    .navbar .navbar-inner {
      border: 0;
      -webkit-box-shadow: 0 2px 10px rgba(0,0,0,.25);
         -moz-box-shadow: 0 2px 10px rgba(0,0,0,.25);
              box-shadow: 0 2px 10px rgba(0,0,0,.25);
    }

    /* Downsize the brand/project name a bit */
    .navbar .brand {
      padding: 14px 20px 16px; /* Increase vertical padding to match navbar links */
      font-size: 16px;
      font-weight: bold;
      text-shadow: 0 -1px 0 rgba(0,0,0,.5);
    }

    /* Navbar links: increase padding for taller navbar */
    .navbar .nav > li > a {
      padding: 15px 20px;
    }

    /* Offset the responsive button for proper vertical alignment */
    .navbar .btn-navbar {
      margin-top: 10px;
    }



    /* CUSTOMIZE THE NAVBAR
    -------------------------------------------------- */


    .carousel .container {
      position: relative;
      z-index: 9;
    }

    .carousel-control {
      height: 80px;
      margin-top: 0;
      font-size: 120px;
      text-shadow: 0 1px 1px rgba(0,0,0,.4);
      background-color: transparent;
      border: 0;
    }

    .carousel .item {
      height: 500px;
    }
    .carousel img {
      position: absolute;
      top: 0;
      left: 0;
      min-width: 100%;
      height: 500px;
    }

    .carousel-caption {
      background-color: transparent;
      position: static;
      max-width: 550px;
      padding: 0 20px;
      margin-top: 200px;
    }
    .carousel-caption h1,
    .carousel-caption .lead {
      margin: 0;
      line-height: 1.25;
      color: #fff;
      text-shadow: 0 1px 1px rgba(0,0,0,.4);
    }
    .carousel-caption .btn {
      margin-top: 10px;
    }



    /* MARKETING CONTENT
    -------------------------------------------------- */

    /* Center align the text within the three columns below the carousel */
    .marketing .span4 {
      text-align: center;
    }
    .marketing h2 {
      font-weight: normal;
    }
    .marketing .span4 p {
      margin-left: 10px;
      margin-right: 10px;
    }


    /* Featurettes
    ------------------------- */

    .featurette-divider {
      margin: 80px 0; /* Space out the Bootstrap <hr> more */
    }
    .featurette {
      padding-top: 120px; /* Vertically center images part 1: add padding above and below text. */
      overflow: hidden; /* Vertically center images part 2: clear their floats. */
    }
    .featurette-image {
      margin-top: -120px; /* Vertically center images part 3: negative margin up the image the same amount of the padding to center it. */
    }

    /* Give some space on the sides of the floated elements so text doesn't run right into it. */
    .featurette-image.pull-left {
      margin-right: 40px;
    }
    .featurette-image.pull-right {
      margin-left: 40px;
    }

    /* Thin out the marketing headings */
    .featurette-heading {
      font-size: 50px;
      font-weight: 300;
      line-height: 1;
      letter-spacing: -1px;
    }



    /* RESPONSIVE CSS
    -------------------------------------------------- */

    \@media (max-width: 979px) {

      .container.navbar-wrapper {
        margin-bottom: 0;
        width: auto;
      }
      .navbar-inner {
        border-radius: 0;
        margin: -20px 0;
      }

      .carousel .item {
        height: 500px;
      }
      .carousel img {
        width: auto;
        height: 500px;
      }

      .featurette {
        height: auto;
        padding: 0;
      }
      .featurette-image.pull-left,
      .featurette-image.pull-right {
        display: block;
        float: none;
        max-width: 40%;
        margin: 0 auto 20px;
      }
    }


    \@media (max-width: 767px) {

      .navbar-inner {
        margin: -20px;
      }

      .carousel {
        margin-left: -20px;
        margin-right: -20px;
      }
      .carousel .container {

      }
      .carousel .item {
        height: 300px;
      }
      .carousel img {
        height: 300px;
      }
      .carousel-caption {
        width: 65%;
        padding: 0 70px;
        margin-top: 100px;
      }
      .carousel-caption h1 {
        font-size: 30px;
      }
      .carousel-caption .lead,
      .carousel-caption .btn {
        font-size: 18px;
      }

      .marketing .span4 + .span4 {
        margin-top: 40px;
      }

      .featurette-heading {
        font-size: 30px;
      }
      .featurette .lead {
        font-size: 18px;
        line-height: 1.5;
      }

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


	</head>

  <body>



    <!-- NAVBAR
    ================================================== -->
    <div class="navbar-wrapper">
      <!-- Wrap the .navbar in .container to center it within the absolutely positioned parent. -->
      <div class="container">

        <div class="navbar navbar-inverse">
          <div class="navbar-inner">
            <!-- Responsive Navbar Part 1: Button for triggering responsive navbar (not covered in tutorial). Include responsive CSS to utilize. -->
            <a class="btn btn-navbar" data-toggle="collapse" data-target=".nav-collapse">
              <span class="icon-bar"></span>
              <span class="icon-bar"></span>
              <span class="icon-bar"></span>
            </a>
            <a class="brand" href="index.php">Harvix</a>
            <!-- Responsive Navbar Part 2: Place all navbar contents you want collapsed withing .navbar-collapse.collapse. -->
            <div class="nav-collapse collapse">
              <ul class="nav">
                <li><a href="games2.cgi">Top Games</a></li>
                <li><a href="games2.cgi?strategy">Strategy</a></li>
                <li><a href="games2.cgi?racing">Racing</a></li>
                <li><a href="games2.cgi?shooting">Shooting</a></li>
                <li><a href="games2.cgi?zombie">Zombie</a></li>
                <li><a href="games2.cgi?arcade">Arcade</a></li>
              </ul>
            </div><!--/.nav-collapse -->
          </div><!-- /.navbar-inner -->
        </div><!-- /.navbar -->

      </div> <!-- /.container -->
    </div><!-- /.navbar-wrapper -->




<p>
&nbsp;
<p>
&nbsp;
<p>
&nbsp;

    <!-- Marketing messaging and featurettes
    ================================================== -->
    <!-- Wrap the rest of the page in another container to center all the content. -->

    <div class="container marketing">

<h2>Top Strategy Games:</h2>
          <div class="row-fluid">
            <ul class="thumbnails">
              <li class="span4">
                <div class="thumbnail">
                  <img src="http://wantedgames.com/games/images/bloom-defender-icon-2.jpg" alt="">
                  <div class="caption">
                    <h3>Bloom Defender</h3>
                    <p><a href="games2.cgi?strategy1" class="btn btn-primary">Play Now</a></p>
                  </div>
                </div>
              </li>
              <li class="span4">
                <div class="thumbnail">
                  <img src="http://a.opiga.com/wp-content/thumbs/mythic-fort-defense_3008.jpg" alt="">
                  <div class="caption">
                    <h3>Mythic Fort Defense</h3>
                    <p><a href="games2.cgi?strategy2" class="btn btn-primary">Play Now</a></p>
                  </div>
                </div>
              </li>
              <li class="span4">
                <div class="thumbnail">
                  <img src="http://cdn2.kongcdn.com/game_icons/0018/3630/monster_slayers_100x75.png?11092-op" alt="">
                  <div class="caption">
                    <h3>Monster Slayer</h3>
                    <p><a href="games2.cgi?strategy3" class="btn btn-primary">Play Now</a></p>
                  </div>
                </div>
              </li>
            </ul>
          </div>
   <div class="row-fluid">
            <ul class="thumbnails">
              <li class="span4">
                <div class="thumbnail">
                  <img src="http://cdn3.kongcdn.com/game_icons/0001/5785/warlords.jpg?8512-op" alt="">
                  <div class="caption">
                    <h3>Warlords: Call to Arms</h3>
                    <p><a href="games2.cgi?strategy4" class="btn btn-primary">Play Now</a></p>
                  </div>
                </div>
              </li>
              <li class="span4">
                <div class="thumbnail">
                  <img src="http://cdn2.kongcdn.com/game_icons/0001/1709/logofinal-kong.png?15017-op" alt="">
                  <div class="caption">
                    <h3>Protector</h3>
                    <p><a href="games2.cgi?strategy5" class="btn btn-primary">Play Now</a></p>
                  </div>
                </div>
              </li>
              <li class="span4">
                <div class="thumbnail">
                  <img src="http://cdn1.kongcdn.com/game_icons/0023/2375/oo_icon3_125x100_site.png?9232-op" alt="">
                  <div class="caption">
                    <h3>Orbital Onslaught</h3>
                    <p><a href="games2.cgi?strategy6" class="btn btn-primary">Play Now</a></p>
                  </div>
                </div>
              </li>
            </ul>
          </div>
   <div class="row-fluid">
            <ul class="thumbnails">
              <li class="span4">
                <div class="thumbnail">
                  <img src="http://cdn2.kongcdn.com/game_icons/0002/0325/kong_thumbnail.jpg?6751-op" alt="">
                  <div class="caption">
                    <h3>Dungeon Defender</h3>
                    <p><a href="games2.cgi?strategy7" class="btn btn-primary">Play Now</a></p>
                  </div>
                </div>
              </li>
              <li class="span4">
                <div class="thumbnail">
                  <img src="http://cdn2.kongcdn.com/game_icons/0004/2691/battalion_icon.jpg?7412-op" alt="">
                  <div class="caption">
                    <h3>Battalion: Nemesis</h3>
                    <p><a href="games2.cgi?strategy8" class="btn btn-primary">Play Now</a></p>
                  </div>
                </div>
              </li>
              <li class="span4">
                <div class="thumbnail">
                  <img src="http://cdn1.kongcdn.com/game_icons/0027/0143/toc_thumb_kong_site.jpg?6454-op" alt="">
                  <div class="caption">
                    <h3>The Osiris Conflict</h3>
                    <p><a href="games2.cgi?strategy9" class="btn btn-primary">Play Now</a></p>
                  </div>
                </div>
              </li>
            </ul>
          </div>
 <div class="row-fluid">
            <ul class="thumbnails">
              <li class="span4">
                <div class="thumbnail">
                  <img src="http://cdn1.kongcdn.com/game_icons/0029/9574/1_site.jpg?8636-op" alt="">
                  <div class="caption">
                    <h3>Necropolis Defence</h3>
                    <p><a href="games2.cgi?strategy10" class="btn btn-primary">Play Now</a></p>
                  </div>
                </div>
              </li>
              <li class="span4">
                <div class="thumbnail">
                  <img src="http://cdn.flonga.com/games/thumb/fureyes-base-defense.jpg" alt="">
                  <div class="caption">
                    <h3>FurEyes Base Defence</h3>
                    <p><a href="games2.cgi?strategy11" class="btn btn-primary">Play Now</a></p>
                  </div>
                </div>
              </li>
              <li class="span4">
                <div class="thumbnail">
                  <img src="http://cdn1.kongcdn.com/game_icons/0006/7679/strategy.jpg?2833-op" alt="">
                  <div class="caption">
                    <h3>Invasion From Hell</h3>
                    <p><a href="games2.cgi?strategy12" class="btn btn-primary">Play Now</a></p>
                  </div>
                </div>
              </li>
            </ul>
          </div>
	<hr class="featurette-divider">


      <!-- FOOTER -->
      <footer>
        <p class="pull-right"><a href="#">Back to top</a></p>
        <p>&copy; 2012 Harvix</p>
      </footer>

    </div><!-- /.container -->



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
    <script>
      !function (48 48 {
        48 48function(){
          // carousel demo
          48 48'#myCarousel').carousel()
        })
      }(window.jQuery)
    </script>
  </body>
</html>

EOX
;
}

if ( $page eq 'racing' )
{
print <<EOX



<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Harvix Games</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Harvix free online  Games">
    <meta name="author" content="Harvix Search">

    <!-- Le styles -->
    <link href="http://twitter.github.com/bootstrap/assets/css/bootstrap.css" rel="stylesheet">
    <link href="http://twitter.github.com/bootstrap/assets/css/bootstrap-responsive.css" rel="stylesheet">
    <style>

    /* GLOBAL STYLES
    -------------------------------------------------- */
    /* Padding below the footer and lighter body text */

    body {
      padding-bottom: 40px;
      color: #5a5a5a;
    }



    /* CUSTOMIZE THE NAVBAR
    -------------------------------------------------- */

    /* Special class on .container surrounding .navbar, used for positioning it into place. */
    .navbar-wrapper {
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      z-index: 10;
      margin-top: 20px;
      margin-bottom: -90px; /* Negative margin to pull up carousel. 90px is roughly margins and height of navbar. */
    }
    .navbar-wrapper .navbar {

    }

    /* Remove border and change up box shadow for more contrast */
    .navbar .navbar-inner {
      border: 0;
      -webkit-box-shadow: 0 2px 10px rgba(0,0,0,.25);
         -moz-box-shadow: 0 2px 10px rgba(0,0,0,.25);
              box-shadow: 0 2px 10px rgba(0,0,0,.25);
    }

    /* Downsize the brand/project name a bit */
    .navbar .brand {
      padding: 14px 20px 16px; /* Increase vertical padding to match navbar links */
      font-size: 16px;
      font-weight: bold;
      text-shadow: 0 -1px 0 rgba(0,0,0,.5);
    }

    /* Navbar links: increase padding for taller navbar */
    .navbar .nav > li > a {
      padding: 15px 20px;
    }

    /* Offset the responsive button for proper vertical alignment */
    .navbar .btn-navbar {
      margin-top: 10px;
    }



    /* CUSTOMIZE THE NAVBAR
    -------------------------------------------------- */

    /* Carousel base class */
    .carousel {
      margin-bottom: 60px;
    }

    .carousel .container {
      position: relative;
      z-index: 9;
    }

    .carousel-control {
      height: 80px;
      margin-top: 0;
      font-size: 120px;
      text-shadow: 0 1px 1px rgba(0,0,0,.4);
      background-color: transparent;
      border: 0;
    }

    .carousel .item {
      height: 500px;
    }
    .carousel img {
      position: absolute;
      top: 0;
      left: 0;
      min-width: 100%;
      height: 500px;
    }

    .carousel-caption {
      background-color: transparent;
      position: static;
      max-width: 550px;
      padding: 0 20px;
      margin-top: 200px;
    }
    .carousel-caption h1,
    .carousel-caption .lead {
      margin: 0;
      line-height: 1.25;
      color: #fff;
      text-shadow: 0 1px 1px rgba(0,0,0,.4);
    }
    .carousel-caption .btn {
      margin-top: 10px;
    }



    /* MARKETING CONTENT
    -------------------------------------------------- */

    /* Center align the text within the three columns below the carousel */
    .marketing .span4 {
      text-align: center;
    }
    .marketing h2 {
      font-weight: normal;
    }
    .marketing .span4 p {
      margin-left: 10px;
      margin-right: 10px;
    }


    /* Featurettes
    ------------------------- */

    .featurette-divider {
      margin: 80px 0; /* Space out the Bootstrap <hr> more */
    }
    .featurette {
      padding-top: 120px; /* Vertically center images part 1: add padding above and below text. */
      overflow: hidden; /* Vertically center images part 2: clear their floats. */
    }
    .featurette-image {
      margin-top: -120px; /* Vertically center images part 3: negative margin up the image the same amount of the padding to center it. */
    }

    /* Give some space on the sides of the floated elements so text doesn't run right into it. */
    .featurette-image.pull-left {
      margin-right: 40px;
    }
    .featurette-image.pull-right {
      margin-left: 40px;
    }

    /* Thin out the marketing headings */
    .featurette-heading {
      font-size: 50px;
      font-weight: 300;
      line-height: 1;
      letter-spacing: -1px;
    }



    /* RESPONSIVE CSS
    -------------------------------------------------- */

    \@media (max-width: 979px) {

      .container.navbar-wrapper {
        margin-bottom: 0;
        width: auto;
      }
      .navbar-inner {
        border-radius: 0;
        margin: -20px 0;
      }

      .carousel .item {
        height: 500px;
      }
      .carousel img {
        width: auto;
        height: 500px;
      }

      .featurette {
        height: auto;
        padding: 0;
      }
      .featurette-image.pull-left,
      .featurette-image.pull-right {
        display: block;
        float: none;
        max-width: 40%;
        margin: 0 auto 20px;
      }
    }


    \@media (max-width: 767px) {

      .navbar-inner {
        margin: -20px;
      }

      .carousel {
        margin-left: -20px;
        margin-right: -20px;
      }
      .carousel .container {

      }
      .carousel .item {
        height: 300px;
      }
      .carousel img {
        height: 300px;
      }
      .carousel-caption {
        width: 65%;
        padding: 0 70px;
        margin-top: 100px;
      }
      .carousel-caption h1 {
        font-size: 30px;
      }
      .carousel-caption .lead,
      .carousel-caption .btn {
        font-size: 18px;
      }

      .marketing .span4 + .span4 {
        margin-top: 40px;
      }

      .featurette-heading {
        font-size: 30px;
      }
      .featurette .lead {
        font-size: 18px;
        line-height: 1.5;
      }

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


	</head>

  <body>



    <!-- NAVBAR
    ================================================== -->
    <div class="navbar-wrapper">
      <!-- Wrap the .navbar in .container to center it within the absolutely positioned parent. -->
      <div class="container">

        <div class="navbar navbar-inverse">
          <div class="navbar-inner">
            <!-- Responsive Navbar Part 1: Button for triggering responsive navbar (not covered in tutorial). Include responsive CSS to utilize. -->
            <a class="btn btn-navbar" data-toggle="collapse" data-target=".nav-collapse">
              <span class="icon-bar"></span>
              <span class="icon-bar"></span>
              <span class="icon-bar"></span>
            </a>
            <a class="brand" href="index.php">Harvix</a>
            <!-- Responsive Navbar Part 2: Place all navbar contents you want collapsed withing .navbar-collapse.collapse. -->
            <div class="nav-collapse collapse">
              <ul class="nav">
                <li><a href="games2.cgi">Top Games</a></li>
                <li><a href="games2.cgi?strategy">Strategy</a></li>
                <li><a href="games2.cgi?racing">Racing</a></li>
                <li><a href="games2.cgi?shooting">Shooting</a></li>
                <li><a href="games2.cgi?zombie">Zombie</a></li>
                <li><a href="games2.cgi?arcade">Arcade</a></li>
              </ul>
            </div><!--/.nav-collapse -->
          </div><!-- /.navbar-inner -->
        </div><!-- /.navbar -->

      </div> <!-- /.container -->
    </div><!-- /.navbar-wrapper -->




<p>
&nbsp;
<p>
&nbsp;
<p>
&nbsp;

    <!-- Marketing messaging and featurettes
    ================================================== -->
    <!-- Wrap the rest of the page in another container to center all the content. -->

    <div class="container marketing">

<h2>Top Racing Games:</h2>
          <div class="row-fluid">
            <ul class="thumbnails">
              <li class="span4">
                <div class="thumbnail">
                  <img src="http://cdn4.kongcdn.com/game_icons/0041/5421/musclecars_250x200_site.png?13985-op" alt="">
                  <div class="caption">
                    <h3>V8 Muscle Cars</h3>
                    <p><a href="games2.cgi?racing1" class="btn btn-primary">Play Now</a></p>
                  </div>
                </div>
              </li>
              <li class="span4">
                <div class="thumbnail">
                  <img src="http://cdn3.kongcdn.com/game_icons/0026/8119/icon_coaster2_100_site.png?15265-op" alt="">
                  <div class="caption">
                    <h3>Coaster Racer 2</h3>
                    <p><a href="games2.cgi?racing2" class="btn btn-primary">Play Now</a></p>
                  </div>
                </div>
              </li>
              <li class="span4">
                <div class="thumbnail">
                  <img src="http://cdn4.kongcdn.com/game_icons/0036/5922/formula2012_kong_site.png?28760-op" alt="">
                  <div class="caption">
                    <h3>Formula Racer 2012</h3>
                    <p><a href="games2.cgi?racing3" class="btn btn-primary">Play Now</a></p>
                  </div>
                </div>
              </li>
            </ul>
          </div>
   <div class="row-fluid">
            <ul class="thumbnails">
              <li class="span4">
                <div class="thumbnail">
                  <img src="http://cdn4.kongcdn.com/game_icons/0015/1608/drift2icon04_100x75.png?13221-op" alt="">
                  <div class="caption">
                    <h3>Drift Runners</h3>
                    <p><a href="games2.cgi?racing4" class="btn btn-primary">Play Now</a></p>
                  </div>
                </div>
              </li>
              <li class="span4">
                <div class="thumbnail">
                  <img src="http://cdn4.kongcdn.com/game_icons/0034/4507/hotrod_site.png?14609-op" alt="">
                  <div class="caption">
                    <h3>Hot Rod Racing</h3>
                    <p><a href="games2.cgi?racing5" class="btn btn-primary">Play Now</a></p>
                  </div>
                </div>
              </li>
              <li class="span4">
                <div class="thumbnail">
                  <img src="http://cdn1.kongcdn.com/game_icons/0041/6927/kong_250x200_site.png?22899-op" alt="">
                  <div class="caption">
                    <h3>American Racing</h3>
                    <p><a href="games2.cgi?racing6" class="btn btn-primary">Play Now</a></p>
                  </div>
                </div>
              </li>
            </ul>
          </div>
   <div class="row-fluid">
            <ul class="thumbnails">
              <li class="span4">
                <div class="thumbnail">
                  <img src="http://cdn4.kongcdn.com/game_icons/0034/6549/neon2_icon_125x100_site.png?14832-op" alt="">
                  <div class="caption">
                    <h3>Neon Race 2</h3>
                    <p><a href="games2.cgi?racing7" class="btn btn-primary">Play Now</a></p>
                  </div>
                </div>
              </li>
              <li class="span4">
                <div class="thumbnail">
                  <img src="http://upload.wikimedia.org/wikipedia/commons/thumb/8/84/Ayrton_Senna_1988_Canada.jpg/220px-Ayrton_Senna_1988_Canada.jpg" alt="">
                  <div class="caption">
                    <h3>Grand Prix Pro</h3>
                    <p><a href="games2.cgi?racing8" class="btn btn-primary">Play Now</a></p>
                  </div>
                </div>
              </li>
              <li class="span4">
                <div class="thumbnail">
                  <img src="http://cdn4.kongcdn.com/game_icons/0029/4846/a_site.jpg?3909-op" alt="">
                  <div class="caption">
                    <h3>Space Punk Racer</h3>
                    <p><a href="games2.cgi?racing9" class="btn btn-primary">Play Now</a></p>
                  </div>
                </div>
              </li>
            </ul>
          </div>
 <div class="row-fluid">
            <ul class="thumbnails">
              <li class="span4">
                <div class="thumbnail">
                  <img src="http://cdn3.kongcdn.com/game_icons/0022/1809/icon_coastrunner_100_site.png?15697-op" alt="">
                  <div class="caption">
                    <h3>Coast Runners</h3>
                    <p><a href="games2.cgi?racing10" class="btn btn-primary">Play Now</a></p>
                  </div>
                </div>
              </li>
              <li class="span4">
                <div class="thumbnail">
                  <img src="http://cdn2.kongcdn.com/game_icons/0003/9733/hdx.png?5778-op" alt="">
                  <div class="caption">
                    <h3>HyperDrive X</h3>
                    <p><a href="games2.cgi?racing11" class="btn btn-primary">Play Now</a></p>
                  </div>
                </div>
              </li>
              <li class="span4">
                <div class="thumbnail">
                  <img src="http://cdn1.kongcdn.com/game_icons/0006/2958/rudolphsredrace-100x75.jpg?6191-op" alt="">
                  <div class="caption">
                    <h3>Rudolph's Red Race</h3>
                    <p><a href="games2.cgi?racing12" class="btn btn-primary">Play Now</a></p>
                  </div>
                </div>
              </li>
            </ul>
          </div>
	<hr class="featurette-divider">


      <!-- FOOTER -->
      <footer>
        <p class="pull-right"><a href="#">Back to top</a></p>
        <p>&copy; 2012 Harvix</p>
      </footer>

    </div><!-- /.container -->



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
    <script>
      !function (48 48 {
        48 48function(){
          // carousel demo
          48 48'#myCarousel').carousel()
        })
      }(window.jQuery)
    </script>
  </body>
</html>

EOX
;
}

if ( $page eq 'shooting' )
{
print <<EOX

<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Harvix Games</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Harvix free online  Games">
    <meta name="author" content="Harvix Search">

    <!-- Le styles -->
    <link href="http://twitter.github.com/bootstrap/assets/css/bootstrap.css" rel="stylesheet">
    <link href="http://twitter.github.com/bootstrap/assets/css/bootstrap-responsive.css" rel="stylesheet">
    <style>

    /* GLOBAL STYLES
    -------------------------------------------------- */
    /* Padding below the footer and lighter body text */

    body {
      padding-bottom: 40px;
      color: #5a5a5a;
    }



    /* CUSTOMIZE THE NAVBAR
    -------------------------------------------------- */

    /* Special class on .container surrounding .navbar, used for positioning it into place. */
    .navbar-wrapper {
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      z-index: 10;
      margin-top: 20px;
      margin-bottom: -90px; /* Negative margin to pull up carousel. 90px is roughly margins and height of navbar. */
    }
    .navbar-wrapper .navbar {

    }

    /* Remove border and change up box shadow for more contrast */
    .navbar .navbar-inner {
      border: 0;
      -webkit-box-shadow: 0 2px 10px rgba(0,0,0,.25);
         -moz-box-shadow: 0 2px 10px rgba(0,0,0,.25);
              box-shadow: 0 2px 10px rgba(0,0,0,.25);
    }

    /* Downsize the brand/project name a bit */
    .navbar .brand {
      padding: 14px 20px 16px; /* Increase vertical padding to match navbar links */
      font-size: 16px;
      font-weight: bold;
      text-shadow: 0 -1px 0 rgba(0,0,0,.5);
    }

    /* Navbar links: increase padding for taller navbar */
    .navbar .nav > li > a {
      padding: 15px 20px;
    }

    /* Offset the responsive button for proper vertical alignment */
    .navbar .btn-navbar {
      margin-top: 10px;
    }



    /* CUSTOMIZE THE NAVBAR
    -------------------------------------------------- */

    /* Carousel base class */
    .carousel {
      margin-bottom: 60px;
    }

    .carousel .container {
      position: relative;
      z-index: 9;
    }

    .carousel-control {
      height: 80px;
      margin-top: 0;
      font-size: 120px;
      text-shadow: 0 1px 1px rgba(0,0,0,.4);
      background-color: transparent;
      border: 0;
    }

    .carousel .item {
      height: 500px;
    }
    .carousel img {
      position: absolute;
      top: 0;
      left: 0;
      min-width: 100%;
      height: 500px;
    }

    .carousel-caption {
      background-color: transparent;
      position: static;
      max-width: 550px;
      padding: 0 20px;
      margin-top: 200px;
    }
    .carousel-caption h1,
    .carousel-caption .lead {
      margin: 0;
      line-height: 1.25;
      color: #fff;
      text-shadow: 0 1px 1px rgba(0,0,0,.4);
    }
    .carousel-caption .btn {
      margin-top: 10px;
    }



    /* MARKETING CONTENT
    -------------------------------------------------- */

    /* Center align the text within the three columns below the carousel */
    .marketing .span4 {
      text-align: center;
    }
    .marketing h2 {
      font-weight: normal;
    }
    .marketing .span4 p {
      margin-left: 10px;
      margin-right: 10px;
    }


    /* Featurettes
    ------------------------- */

    .featurette-divider {
      margin: 80px 0; /* Space out the Bootstrap <hr> more */
    }
    .featurette {
      padding-top: 120px; /* Vertically center images part 1: add padding above and below text. */
      overflow: hidden; /* Vertically center images part 2: clear their floats. */
    }
    .featurette-image {
      margin-top: -120px; /* Vertically center images part 3: negative margin up the image the same amount of the padding to center it. */
    }

    /* Give some space on the sides of the floated elements so text doesn't run right into it. */
    .featurette-image.pull-left {
      margin-right: 40px;
    }
    .featurette-image.pull-right {
      margin-left: 40px;
    }

    /* Thin out the marketing headings */
    .featurette-heading {
      font-size: 50px;
      font-weight: 300;
      line-height: 1;
      letter-spacing: -1px;
    }



    /* RESPONSIVE CSS
    -------------------------------------------------- */

    \@media (max-width: 979px) {

      .container.navbar-wrapper {
        margin-bottom: 0;
        width: auto;
      }
      .navbar-inner {
        border-radius: 0;
        margin: -20px 0;
      }

      .carousel .item {
        height: 500px;
      }
      .carousel img {
        width: auto;
        height: 500px;
      }

      .featurette {
        height: auto;
        padding: 0;
      }
      .featurette-image.pull-left,
      .featurette-image.pull-right {
        display: block;
        float: none;
        max-width: 40%;
        margin: 0 auto 20px;
      }
    }


    \@media (max-width: 767px) {

      .navbar-inner {
        margin: -20px;
      }

      .carousel {
        margin-left: -20px;
        margin-right: -20px;
      }
      .carousel .container {

      }
      .carousel .item {
        height: 300px;
      }
      .carousel img {
        height: 300px;
      }
      .carousel-caption {
        width: 65%;
        padding: 0 70px;
        margin-top: 100px;
      }
      .carousel-caption h1 {
        font-size: 30px;
      }
      .carousel-caption .lead,
      .carousel-caption .btn {
        font-size: 18px;
      }

      .marketing .span4 + .span4 {
        margin-top: 40px;
      }

      .featurette-heading {
        font-size: 30px;
      }
      .featurette .lead {
        font-size: 18px;
        line-height: 1.5;
      }

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


	</head>

  <body>





    <!-- NAVBAR
    ================================================== -->
    <div class="navbar-wrapper">
      <!-- Wrap the .navbar in .container to center it within the absolutely positioned parent. -->
      <div class="container">

        <div class="navbar navbar-inverse">
          <div class="navbar-inner">
            <!-- Responsive Navbar Part 1: Button for triggering responsive navbar (not covered in tutorial). Include responsive CSS to utilize. -->
            <a class="btn btn-navbar" data-toggle="collapse" data-target=".nav-collapse">
              <span class="icon-bar"></span>
              <span class="icon-bar"></span>
              <span class="icon-bar"></span>
            </a>
            <a class="brand" href="index.php">Harvix</a>
            <!-- Responsive Navbar Part 2: Place all navbar contents you want collapsed withing .navbar-collapse.collapse. -->
            <div class="nav-collapse collapse">
              <ul class="nav">
                <li><a href="games2.cgi">Top Games</a></li>
                <li><a href="games2.cgi?strategy">Strategy</a></li>
                <li><a href="games2.cgi?racing">Racing</a></li>
                <li><a href="games2.cgi?shooting">Shooting</a></li>
                <li><a href="games2.cgi?zombie">Zombie</a></li>
                <li><a href="games2.cgi?arcade">Arcade</a></li>
              </ul>
            </div><!--/.nav-collapse -->
          </div><!-- /.navbar-inner -->
        </div><!-- /.navbar -->

      </div> <!-- /.container -->
    </div><!-- /.navbar-wrapper -->



<p>
&nbsp;
<p>
&nbsp;
<p>
&nbsp;

    <!-- Marketing messaging and featurettes
    ================================================== -->
    <!-- Wrap the rest of the page in another container to center all the content. -->

    <div class="container marketing">

<h2>Top Shooting Games:</h2>
          <div class="row-fluid">
            <ul class="thumbnails">
              <li class="span4">
                <div class="thumbnail">
                  <img src="http://cdn3.kongcdn.com/game_icons/0008/9132/heavyThumbnail.jpg?6530-op" alt="">
                  <div class="caption">
                    <h3>Heavy Weapons</h3>
                    <p><a href="games2.cgi?shooting1" class="btn btn-primary">Play Now</a></p>
                  </div>
                </div>
              </li>
              <li class="span4">
                <div class="thumbnail">
                  <img src="http://cdn3.kongcdn.com/game_icons/0007/9773/penguinz_thumb_100x100.jpg?4019-op" alt="">
                  <div class="caption">
                    <h3>Penguinz</h3>
                    <p><a href="games2.cgi?shooting2" class="btn btn-primary">Play Now</a></p>
                  </div>
                </div>
              </li>
              <li class="span4">
                <div class="thumbnail">
                  <img src="http://cdn2.kongcdn.com/game_icons/0029/0395/Dead_Metal_thumb_125x100_site.jpg?22956-op" alt="">
                  <div class="caption">
                    <h3>Dead Metal</h3>
                    <p><a href="games2.cgi?shooting3" class="btn btn-primary">Play Now</a></p>
                  </div>
                </div>
              </li>
            </ul>
          </div>
   <div class="row-fluid">
            <ul class="thumbnails">
              <li class="span4">
                <div class="thumbnail">
                  <img src="http://cdn4.kongcdn.com/game_icons/0001/6289/icon.jpg?3830-op" alt="">
                  <div class="caption">
                    <h3>Jack the Fugitive</h3>
                    <p><a href="games2.cgi?shooting4" class="btn btn-primary">Play Now</a></p>
                  </div>
                </div>
              </li>
              <li class="span4">
                <div class="thumbnail">
                  <img src="http://cdn4.kongcdn.com/game_icons/0018/9556/thumb_wksdhmej13538.jpg?5011-op" alt="">
                  <div class="caption">
                    <h3>Hostage Crisis</h3>
                    <p><a href="games2.cgi?shooting5" class="btn btn-primary">Play Now</a></p>
                  </div>
                </div>
              </li>
              <li class="span4">
                <div class="thumbnail">
                  <img src="http://cdn1.kongcdn.com/game_icons/0024/2541/StickWarfare_site.png?22687-op" alt="">
                  <div class="caption">
                    <h3>Vital Bloodshed</h3>
                    <p><a href="games2.cgi?shooting6" class="btn btn-primary">Play Now</a></p>
                  </div>
                </div>
              </li>
            </ul>
          </div>
   <div class="row-fluid">
            <ul class="thumbnails">
              <li class="span4">
                <div class="thumbnail">
                  <img src="http://cdn4.kongcdn.com/game_icons/0000/8995/thumb100x75.jpg?4696-op" alt="">
                  <div class="caption">
                    <h3>MAD: Mutually Assured Destruction</h3>
                    <p><a href="games2.cgi?shooting7" class="btn btn-primary">Play Now</a></p>
                  </div>
                </div>
              </li>
              <li class="span4">
                <div class="thumbnail">
                  <img src="http://cdn4.kongcdn.com/game_icons/0012/1655/Icon_Large2.png?3147-op" alt="">
                  <div class="caption">
                    <h3>Red Fluxion</h3>
                    <p><a href="games2.cgi?shooting8" class="btn btn-primary">Play Now</a></p>
                  </div>
                </div>
              </li>
              <li class="span4">
                <div class="thumbnail">
                  <img src="http://cdn4.kongcdn.com/game_icons/0017/0700/gunexpress_gameicon_100.jpg?4451-op" alt="">
                  <div class="caption">
                    <h3>Gun Express</h3>
                    <p><a href="games2.cgi?shooting9" class="btn btn-primary">Play Now</a></p>
                  </div>
                </div>
              </li>
            </ul>
          </div>
 <div class="row-fluid">
            <ul class="thumbnails">
              <li class="span4">
                <div class="thumbnail">
                  <img src="http://cdn1.kongcdn.com/game_icons/0000/6355/aod_icon_100x75.jpg?5202-op" alt="">
                  <div class="caption">
                    <h3>Army of Destruction</h3>
                    <p><a href="games2.cgi?shooting10" class="btn btn-primary">Play Now</a></p>
                  </div>
                </div>
              </li>
              <li class="span4">
                <div class="thumbnail">
                  <img src="http://cdn2.kongcdn.com/game_icons/0008/3832/_thumb_100x100.jpg?2921-op" alt="">
                  <div class="caption">
                    <h3>Twisted Military</h3>
                    <p><a href="games2.cgi?shooting11" class="btn btn-primary">Play Now</a></p>
                  </div>
                </div>
              </li>
              <li class="span4">
                <div class="thumbnail">
                  <img src="http://www.gamekb.com/thumbs_v2/00255/255998-kongregate-wwii-killer.jpg" alt="">
                  <div class="caption">
                    <h3>WWII Killer</h3>
                    <p><a href="games2.cgi?shooting12" class="btn btn-primary">Play Now</a></p>
                  </div>
                </div>
              </li>
            </ul>
          </div>
	<hr class="featurette-divider">


      <!-- FOOTER -->
      <footer>
        <p class="pull-right"><a href="#">Back to top</a></p>
        <p>&copy; 2012 Harvix</p>
      </footer>

    </div><!-- /.container -->



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
    <script>
      !function (48 48 {
        48 48function(){
          // carousel demo
          48 48'#myCarousel').carousel()
        })
      }(window.jQuery)
    </script>
  </body>
</html>
EOX
;
}

if ( $page eq 'zombie' )
{
print <<EOX

<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Harvix Games</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Harvix free online  Games">
    <meta name="author" content="Harvix Search">

    <!-- Le styles -->
    <link href="http://twitter.github.com/bootstrap/assets/css/bootstrap.css" rel="stylesheet">
    <link href="http://twitter.github.com/bootstrap/assets/css/bootstrap-responsive.css" rel="stylesheet">
    <style>

    /* GLOBAL STYLES
    -------------------------------------------------- */
    /* Padding below the footer and lighter body text */

    body {
      padding-bottom: 40px;
      color: #5a5a5a;
    }



    /* CUSTOMIZE THE NAVBAR
    -------------------------------------------------- */

    /* Special class on .container surrounding .navbar, used for positioning it into place. */
    .navbar-wrapper {
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      z-index: 10;
      margin-top: 20px;
      margin-bottom: -90px; /* Negative margin to pull up carousel. 90px is roughly margins and height of navbar. */
    }
    .navbar-wrapper .navbar {

    }

    /* Remove border and change up box shadow for more contrast */
    .navbar .navbar-inner {
      border: 0;
      -webkit-box-shadow: 0 2px 10px rgba(0,0,0,.25);
         -moz-box-shadow: 0 2px 10px rgba(0,0,0,.25);
              box-shadow: 0 2px 10px rgba(0,0,0,.25);
    }

    /* Downsize the brand/project name a bit */
    .navbar .brand {
      padding: 14px 20px 16px; /* Increase vertical padding to match navbar links */
      font-size: 16px;
      font-weight: bold;
      text-shadow: 0 -1px 0 rgba(0,0,0,.5);
    }

    /* Navbar links: increase padding for taller navbar */
    .navbar .nav > li > a {
      padding: 15px 20px;
    }

    /* Offset the responsive button for proper vertical alignment */
    .navbar .btn-navbar {
      margin-top: 10px;
    }



    /* CUSTOMIZE THE NAVBAR
    -------------------------------------------------- */

    /* Carousel base class */
    .carousel {
      margin-bottom: 60px;
    }

    .carousel .container {
      position: relative;
      z-index: 9;
    }

    .carousel-control {
      height: 80px;
      margin-top: 0;
      font-size: 120px;
      text-shadow: 0 1px 1px rgba(0,0,0,.4);
      background-color: transparent;
      border: 0;
    }

    .carousel .item {
      height: 500px;
    }
    .carousel img {
      position: absolute;
      top: 0;
      left: 0;
      min-width: 100%;
      height: 500px;
    }

    .carousel-caption {
      background-color: transparent;
      position: static;
      max-width: 550px;
      padding: 0 20px;
      margin-top: 200px;
    }
    .carousel-caption h1,
    .carousel-caption .lead {
      margin: 0;
      line-height: 1.25;
      color: #fff;
      text-shadow: 0 1px 1px rgba(0,0,0,.4);
    }
    .carousel-caption .btn {
      margin-top: 10px;
    }



    /* MARKETING CONTENT
    -------------------------------------------------- */

    /* Center align the text within the three columns below the carousel */
    .marketing .span4 {
      text-align: center;
    }
    .marketing h2 {
      font-weight: normal;
    }
    .marketing .span4 p {
      margin-left: 10px;
      margin-right: 10px;
    }


    /* Featurettes
    ------------------------- */

    .featurette-divider {
      margin: 80px 0; /* Space out the Bootstrap <hr> more */
    }
    .featurette {
      padding-top: 120px; /* Vertically center images part 1: add padding above and below text. */
      overflow: hidden; /* Vertically center images part 2: clear their floats. */
    }
    .featurette-image {
      margin-top: -120px; /* Vertically center images part 3: negative margin up the image the same amount of the padding to center it. */
    }

    /* Give some space on the sides of the floated elements so text doesn't run right into it. */
    .featurette-image.pull-left {
      margin-right: 40px;
    }
    .featurette-image.pull-right {
      margin-left: 40px;
    }

    /* Thin out the marketing headings */
    .featurette-heading {
      font-size: 50px;
      font-weight: 300;
      line-height: 1;
      letter-spacing: -1px;
    }



    /* RESPONSIVE CSS
    -------------------------------------------------- */

    \@media (max-width: 979px) {

      .container.navbar-wrapper {
        margin-bottom: 0;
        width: auto;
      }
      .navbar-inner {
        border-radius: 0;
        margin: -20px 0;
      }

      .carousel .item {
        height: 500px;
      }
      .carousel img {
        width: auto;
        height: 500px;
      }

      .featurette {
        height: auto;
        padding: 0;
      }
      .featurette-image.pull-left,
      .featurette-image.pull-right {
        display: block;
        float: none;
        max-width: 40%;
        margin: 0 auto 20px;
      }
    }


    \@media (max-width: 767px) {

      .navbar-inner {
        margin: -20px;
      }

      .carousel {
        margin-left: -20px;
        margin-right: -20px;
      }
      .carousel .container {

      }
      .carousel .item {
        height: 300px;
      }
      .carousel img {
        height: 300px;
      }
      .carousel-caption {
        width: 65%;
        padding: 0 70px;
        margin-top: 100px;
      }
      .carousel-caption h1 {
        font-size: 30px;
      }
      .carousel-caption .lead,
      .carousel-caption .btn {
        font-size: 18px;
      }

      .marketing .span4 + .span4 {
        margin-top: 40px;
      }

      .featurette-heading {
        font-size: 30px;
      }
      .featurette .lead {
        font-size: 18px;
        line-height: 1.5;
      }

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


	</head>

  <body>




    <!-- NAVBAR
    ================================================== -->
    <div class="navbar-wrapper">
      <!-- Wrap the .navbar in .container to center it within the absolutely positioned parent. -->
      <div class="container">

        <div class="navbar navbar-inverse">
          <div class="navbar-inner">
            <!-- Responsive Navbar Part 1: Button for triggering responsive navbar (not covered in tutorial). Include responsive CSS to utilize. -->
            <a class="btn btn-navbar" data-toggle="collapse" data-target=".nav-collapse">
              <span class="icon-bar"></span>
              <span class="icon-bar"></span>
              <span class="icon-bar"></span>
            </a>
            <a class="brand" href="index.php">Harvix</a>
            <!-- Responsive Navbar Part 2: Place all navbar contents you want collapsed withing .navbar-collapse.collapse. -->
            <div class="nav-collapse collapse">
              <ul class="nav">
                <li><a href="games2.cgi">Top Games</a></li>
                <li><a href="games2.cgi?strategy">Strategy</a></li>
                <li><a href="games2.cgi?racing">Racing</a></li>
                <li><a href="games2.cgi?shooting">Shooting</a></li>
                <li><a href="games2.cgi?zombie">Zombie</a></li>
                <li><a href="games2.cgi?arcade">Arcade</a></li>
              </ul>
            </div><!--/.nav-collapse -->
          </div><!-- /.navbar-inner -->
        </div><!-- /.navbar -->

      </div> <!-- /.container -->
    </div><!-- /.navbar-wrapper -->



<p>
&nbsp;
<p>
&nbsp;
<p>
&nbsp;

    <!-- Marketing messaging and featurettes
    ================================================== -->
    <!-- Wrap the rest of the page in another container to center all the content. -->

    <div class="container marketing">

<h2>Top Zombie Games:</h2>
          <div class="row-fluid">
            <ul class="thumbnails">
              <li class="span4">
                <div class="thumbnail">
                  <img src="http://cdn1.kongcdn.com/game_icons/0027/0483/125x100_site.png?13989-op" alt="">
                  <div class="caption">
                    <h3>Dude and Zombies</h3>
                    <p><a href="games2.cgi?zombie1" class="btn btn-primary">Play Now</a></p>
                  </div>
                </div>
              </li>
              <li class="span4">
                <div class="thumbnail">
                  <img src="http://cdn2.kongcdn.com/game_icons/0036/7540/nologo_125x100_site.png?8992-op" alt="">
                  <div class="caption">
                    <h3>Nuclear Outrun</h3>
                    <p><a href="games2.cgi?zombie2" class="btn btn-primary">Play Now</a></p>
                  </div>
                </div>
              </li>
              <li class="span4">
                <div class="thumbnail">
                  <img src="http://cdn1.kongcdn.com/game_icons/0022/1035/zombooka_levelPack_site.png?9938-op" alt="">
                  <div class="caption">
                    <h3>Flaming Zombooka 2</h3>
                    <p><a href="games2.cgi?zombie3" class="btn btn-primary">Play Now</a></p>
                  </div>
                </div>
              </li>
            </ul>
          </div>
   <div class="row-fluid">
            <ul class="thumbnails">
              <li class="span4">
                <div class="thumbnail">
                  <img src="http://assets.zui.com.s3.amazonaws.com/games/image/4f5c4631da29f126b700062f/thumb_robot-vs-zombies-arcade-game.jpg" alt="">
                  <div class="caption">
                    <h3>Robots vs. Zombies</h3>
                    <p><a href="games2.cgi?zombie4" class="btn btn-primary">Play Now</a></p>
                  </div>
                </div>
              </li>
              <li class="span4">
                <div class="thumbnail">
                  <img src="http://twotowersgames.com/thumb/zombies-mice-annihilation/zombies-mice-annihilation-230x130.jpg" alt="">
                  <div class="caption">
                    <h3>Zombie Mice Annihilation</h3>
                    <p><a href="games2.cgi?zombie5" class="btn btn-primary">Play Now</a></p>
                  </div>
                </div>
              </li>
              <li class="span4">
                <div class="thumbnail">
                  <img src="http://cdn1.kongcdn.com/game_icons/0007/5373/zombie116.jpg?4354-op" alt="">
                  <div class="caption">
                    <h3>Zombie Infestation: Strain 116</h3>
                    <p><a href="games2.cgi?zombie6" class="btn btn-primary">Play Now</a></p>
                  </div>
                </div>
              </li>
            </ul>
          </div>
   <div class="row-fluid">
            <ul class="thumbnails">
              <li class="span4">
                <div class="thumbnail">
                  <img src="http://cdn4.kongcdn.com/game_icons/0034/7437/truck_site.jpg?8576-op" alt="">
                  <div class="caption">
                    <h3>Truckminator</h3>
                    <p><a href="games2.cgi?zombie7" class="btn btn-primary">Play Now</a></p>
                  </div>
                </div>
              </li>
              <li class="span4">
                <div class="thumbnail">
                  <img src="http://cdn4.kongcdn.com/game_icons/0031/3382/game_thumb_site.png?18429-op" alt="">
                  <div class="caption">
                    <h3>Flaming Zombooka 3 : Carnival</h3>
                    <p><a href="games2.cgi?zombie8" class="btn btn-primary">Play Now</a></p>
                  </div>
                </div>
              </li>
              <li class="span4">
                <div class="thumbnail">
                  <img src="http://www.iconeasy.com/icon/png/Movie%20%26%20TV/Creeps/Zombie.png" alt="">
                  <div class="caption">
                    <h3>Zombie Shootout</h3>
                    <p><a href="games2.cgi?zombie9" class="btn btn-primary">Play Now</a></p>
                  </div>
                </div>
              </li>
            </ul>
          </div>
 <div class="row-fluid">
            <ul class="thumbnails">
              <li class="span4">
                <div class="thumbnail">
                  <img src="http://www.playingarcadegames.com/content/icons/zombies-can-fly-icon-1.jpg" alt="">
                  <div class="caption">
                    <h3>Zombies can Fly</h3>
                    <p><a href="games2.cgi?zombie10" class="btn btn-primary">Play Now</a></p>
                  </div>
                </div>
              </li>
              <li class="span4">
                <div class="thumbnail">
                  <img src="http://icondatabase.net/sites/default/files/icons/plants-vs.zombies-icon-32829.png" alt="">
                  <div class="caption">
                    <h3>Plants vs. Zombies</h3>
                    <p><a href="games2.cgi?zombie11" class="btn btn-primary">Play Now</a></p>
                  </div>
                </div>
              </li>
              <li class="span4">
                <div class="thumbnail">
                  <img src="http://cdn.flonga.com/games/thumb/zombocalypse.jpg" alt="">
                  <div class="caption">
                    <h3>Zombocalypse</h3>
                    <p><a href="games2.cgi?zombie12" class="btn btn-primary">Play Now</a></p>
                  </div>
                </div>
              </li>
            </ul>
          </div>
	<hr class="featurette-divider">


      <!-- FOOTER -->
      <footer>
        <p class="pull-right"><a href="#">Back to top</a></p>
        <p>&copy; 2012 Harvix</p>
      </footer>

    </div><!-- /.container -->



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
    <script>
      !function (48 48 {
        48 48function(){
          // carousel demo
          48 48'#myCarousel').carousel()
        })
      }(window.jQuery)
    </script>
  </body>
</html>

EOX
;
}

if ( $page eq 'arcade' )
{
print <<EOX

<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Harvix Games</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Harvix free online  Games">
    <meta name="author" content="Harvix Search">

    <!-- Le styles -->
    <link href="http://twitter.github.com/bootstrap/assets/css/bootstrap.css" rel="stylesheet">
    <link href="http://twitter.github.com/bootstrap/assets/css/bootstrap-responsive.css" rel="stylesheet">
    <style>

    /* GLOBAL STYLES
    -------------------------------------------------- */
    /* Padding below the footer and lighter body text */

    body {
      padding-bottom: 40px;
      color: #5a5a5a;
    }



    /* CUSTOMIZE THE NAVBAR
    -------------------------------------------------- */

    /* Special class on .container surrounding .navbar, used for positioning it into place. */
    .navbar-wrapper {
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      z-index: 10;
      margin-top: 20px;
      margin-bottom: -90px; /* Negative margin to pull up carousel. 90px is roughly margins and height of navbar. */
    }
    .navbar-wrapper .navbar {

    }

    /* Remove border and change up box shadow for more contrast */
    .navbar .navbar-inner {
      border: 0;
      -webkit-box-shadow: 0 2px 10px rgba(0,0,0,.25);
         -moz-box-shadow: 0 2px 10px rgba(0,0,0,.25);
              box-shadow: 0 2px 10px rgba(0,0,0,.25);
    }

    /* Downsize the brand/project name a bit */
    .navbar .brand {
      padding: 14px 20px 16px; /* Increase vertical padding to match navbar links */
      font-size: 16px;
      font-weight: bold;
      text-shadow: 0 -1px 0 rgba(0,0,0,.5);
    }

    /* Navbar links: increase padding for taller navbar */
    .navbar .nav > li > a {
      padding: 15px 20px;
    }

    /* Offset the responsive button for proper vertical alignment */
    .navbar .btn-navbar {
      margin-top: 10px;
    }



    /* CUSTOMIZE THE NAVBAR
    -------------------------------------------------- */

    /* Carousel base class */
    .carousel {
      margin-bottom: 60px;
    }

    .carousel .container {
      position: relative;
      z-index: 9;
    }

    .carousel-control {
      height: 80px;
      margin-top: 0;
      font-size: 120px;
      text-shadow: 0 1px 1px rgba(0,0,0,.4);
      background-color: transparent;
      border: 0;
    }

    .carousel .item {
      height: 500px;
    }
    .carousel img {
      position: absolute;
      top: 0;
      left: 0;
      min-width: 100%;
      height: 500px;
    }

    .carousel-caption {
      background-color: transparent;
      position: static;
      max-width: 550px;
      padding: 0 20px;
      margin-top: 200px;
    }
    .carousel-caption h1,
    .carousel-caption .lead {
      margin: 0;
      line-height: 1.25;
      color: #fff;
      text-shadow: 0 1px 1px rgba(0,0,0,.4);
    }
    .carousel-caption .btn {
      margin-top: 10px;
    }



    /* MARKETING CONTENT
    -------------------------------------------------- */

    /* Center align the text within the three columns below the carousel */
    .marketing .span4 {
      text-align: center;
    }
    .marketing h2 {
      font-weight: normal;
    }
    .marketing .span4 p {
      margin-left: 10px;
      margin-right: 10px;
    }


    /* Featurettes
    ------------------------- */

    .featurette-divider {
      margin: 80px 0; /* Space out the Bootstrap <hr> more */
    }
    .featurette {
      padding-top: 120px; /* Vertically center images part 1: add padding above and below text. */
      overflow: hidden; /* Vertically center images part 2: clear their floats. */
    }
    .featurette-image {
      margin-top: -120px; /* Vertically center images part 3: negative margin up the image the same amount of the padding to center it. */
    }

    /* Give some space on the sides of the floated elements so text doesn't run right into it. */
    .featurette-image.pull-left {
      margin-right: 40px;
    }
    .featurette-image.pull-right {
      margin-left: 40px;
    }

    /* Thin out the marketing headings */
    .featurette-heading {
      font-size: 50px;
      font-weight: 300;
      line-height: 1;
      letter-spacing: -1px;
    }



    /* RESPONSIVE CSS
    -------------------------------------------------- */

    \@media (max-width: 979px) {

      .container.navbar-wrapper {
        margin-bottom: 0;
        width: auto;
      }
      .navbar-inner {
        border-radius: 0;
        margin: -20px 0;
      }

      .carousel .item {
        height: 500px;
      }
      .carousel img {
        width: auto;
        height: 500px;
      }

      .featurette {
        height: auto;
        padding: 0;
      }
      .featurette-image.pull-left,
      .featurette-image.pull-right {
        display: block;
        float: none;
        max-width: 40%;
        margin: 0 auto 20px;
      }
    }


    \@media (max-width: 767px) {

      .navbar-inner {
        margin: -20px;
      }

      .carousel {
        margin-left: -20px;
        margin-right: -20px;
      }
      .carousel .container {

      }
      .carousel .item {
        height: 300px;
      }
      .carousel img {
        height: 300px;
      }
      .carousel-caption {
        width: 65%;
        padding: 0 70px;
        margin-top: 100px;
      }
      .carousel-caption h1 {
        font-size: 30px;
      }
      .carousel-caption .lead,
      .carousel-caption .btn {
        font-size: 18px;
      }

      .marketing .span4 + .span4 {
        margin-top: 40px;
      }

      .featurette-heading {
        font-size: 30px;
      }
      .featurette .lead {
        font-size: 18px;
        line-height: 1.5;
      }

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


	</head>

  <body>




    <!-- NAVBAR
    ================================================== -->
    <div class="navbar-wrapper">
      <!-- Wrap the .navbar in .container to center it within the absolutely positioned parent. -->
      <div class="container">

        <div class="navbar navbar-inverse">
          <div class="navbar-inner">
            <!-- Responsive Navbar Part 1: Button for triggering responsive navbar (not covered in tutorial). Include responsive CSS to utilize. -->
            <a class="btn btn-navbar" data-toggle="collapse" data-target=".nav-collapse">
              <span class="icon-bar"></span>
              <span class="icon-bar"></span>
              <span class="icon-bar"></span>
            </a>
            <a class="brand" href="index.php">Harvix</a>
            <!-- Responsive Navbar Part 2: Place all navbar contents you want collapsed withing .navbar-collapse.collapse. -->
            <div class="nav-collapse collapse">
              <ul class="nav">
                <li><a href="games2.cgi">Top Games</a></li>
                <li><a href="games2.cgi?strategy">Strategy</a></li>
                <li><a href="games2.cgi?racing">Racing</a></li>
                <li><a href="games2.cgi?shooting">Shooting</a></li>
                <li><a href="games2.cgi?zombie">Zombie</a></li>
                <li><a href="games2.cgi?arcade">Arcade</a></li>
              </ul>
            </div><!--/.nav-collapse -->
          </div><!-- /.navbar-inner -->
        </div><!-- /.navbar -->

      </div> <!-- /.container -->
    </div><!-- /.navbar-wrapper -->



<p>
&nbsp;
<p>
&nbsp;
<p>
&nbsp;

    <!-- Marketing messaging and featurettes
    ================================================== -->
    <!-- Wrap the rest of the page in another container to center all the content. -->

    <div class="container marketing">

<h2>Top Arcade Games:</h2>
          <div class="row-fluid">
            <ul class="thumbnails">
              <li class="span4">
                <div class="thumbnail">
                  <img src="http://fc00.deviantart.net/fs6/i/2005/049/f/0/space_invader_icon_2_by_moglenstar.png" alt="">
                  <div class="caption">
                    <h3>Space Invaders</h3>
                    <p><a href="games2.cgi?arcade1" class="btn btn-primary">Play Now</a></p>
                  </div>
                </div>
              </li>
              <li class="span4">
                <div class="thumbnail">
                  <img src="http://i1-mac.softpedia-static.com/screenshots/JSplash-Snake-Game_1.png" alt="">
                  <div class="caption">
                    <h3>Snake</h3>
                    <p><a href="games2.cgi?arcade2" class="btn btn-primary">Play Now</a></p>
                  </div>
                </div>
              </li>
              <li class="span4">
                <div class="thumbnail">
                  <img src="http://ecx.images-amazon.com/images/I/812VTuHOXzL._SL500_AA300_.png" alt="">
                  <div class="caption">
                    <h3>Frogger</h3>
                    <p><a href="games2.cgi?arcade3" class="btn btn-primary">Play Now</a></p>
                  </div>
                </div>
              </li>
            </ul>
          </div>
   <div class="row-fluid">
            <ul class="thumbnails">
              <li class="span4">
                <div class="thumbnail">
                  <img src="http://robcrocombe.files.wordpress.com/2012/07/pong1-e1343341339689.png" alt="">
                  <div class="caption">
                    <h3>Pong</h3>
                    <p><a href="games2.cgi?arcade4" class="btn btn-primary">Play Now</a></p>
                  </div>
                </div>
              </li>
              <li class="span4">
                <div class="thumbnail">
                  <img src="http://i1-linux.softpedia-static.com/screenshots/Hexxagon-best1000games_1.jpg" alt="">
                  <div class="caption">
                    <h3>Hexxagon</h3>
                    <p><a href="games2.cgi?arcade5" class="btn btn-primary">Play Now</a></p>
                  </div>
                </div>
              </li>
              <li class="span4">
                <div class="thumbnail">
                  <img src="http://soundwavestv.com/wp-content/uploads/2011/08/Asteroids-Movie.jpg" alt="">
                  <div class="caption">
                    <h3>Asteroids</h3>
                    <p><a href="games2.cgi?arcade6" class="btn btn-primary">Play Now</a></p>
                  </div>
                </div>
              </li>
            </ul>
          </div>
   <div class="row-fluid">
            <ul class="thumbnails">
              <li class="span4">
                <div class="thumbnail">
                  <img src="http://us.123rf.com/400wm/400/400/styleuneed/styleuneed1206/styleuneed120600111/13915155-tic-tac-toe-simbolo.jpg" alt="">
                  <div class="caption">
                    <h3>Tic-Tac-Toe</h3>
                    <p><a href="games2.cgi?arcade7" class="btn btn-primary">Play Now</a></p>
                  </div>
                </div>
              </li>
              <li class="span4">
                <div class="thumbnail">
                  <img src="http://upload.wikimedia.org/wikipedia/en/thumb/3/3f/Donkey_Kong_NES_Screenshot.png/200px-Donkey_Kong_NES_Screenshot.png" alt="">
                  <div class="caption">
                    <h3>Donkey Kong</h3>
                    <p><a href="games2.cgi?arcade8" class="btn btn-primary">Play Now</a></p>
                  </div>
                </div>
              </li>
              <li class="span4">
                <div class="thumbnail">
                  <img src="http://img.brothersoft.com/screenshots/softimage/c/crazy_taxi-65565-1.jpeg" alt="">
                  <div class="caption">
                    <h3>Crazy Taxi</h3>
                    <p><a href="games2.cgi?arcade9" class="btn btn-primary">Play Now</a></p>
                  </div>
                </div>
              </li>
            </ul>
	<hr class="featurette-divider">


      <!-- FOOTER -->
      <footer>
        <p class="pull-right"><a href="#">Back to top</a></p>
        <p>&copy; 2012 Harvix</p>
      </footer>

    </div><!-- /.container -->



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
    <script>
      !function (48 48 {
        48 48function(){
          // carousel demo
          48 48'#myCarousel').carousel()
        })
      }(window.jQuery)
    </script>
  </body>
</html>

EOX
;
}

sub print_header
{
print <<EOX


<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Harvix Games</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Harvix free online Games">
    <meta name="author" content="David Skrenta">

    <!-- Le styles -->
    <link href="http://twitter.github.com/bootstrap/assets/css/bootstrap.css" rel="stylesheet">
    <style type="text/css">
      body {
        padding-top: 20px;
        padding-bottom: 40px;
      }

      /* Custom container */
      .container-narrow {
        margin: 0 auto;
        max-width: 700px;
      }
      .container-narrow > hr {
        margin: 30px 0;
      }

      /* Main marketing message and sign up button */
      .jumbotron {
        margin: 60px 0;
        text-align: center;
      }
      .jumbotron h1 {
        font-size: 72px;
        line-height: 1;
      }
      .jumbotron .btn {
        font-size: 21px;
        padding: 14px 24px;
      }

      /* Supporting marketing content */
      .marketing {
        margin: 60px 0;
      }
      .marketing p + h4 {
        margin-top: 28px;
      }
    </style>
    <link href="http://twitter.github.com/bootstrap/assets/css/bootstrap-responsive.css" rel="stylesheet">

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


	</head>

  <body>

    <div class="container-narrow">

      <div class="masthead">
        <ul class="nav nav-pills pull-right">
          <li class="active"><a href="games2.cgi">Back to Home</a></li>
        </ul>
        <h3 class="muted">Harvix Games</h3>
      </div>

      <hr>

      <div class="jumbotron">

EOX
;
}


sub print_footer
{
print <<EOF
</div>

      <hr>

      <div class="row-fluid marketing">
        
<!-- begin htmlcommentbox.com -->
 <div id="HCB_comment_box"><a href="http://www.htmlcommentbox.com">HTML Comment Box</a> is loading comments...</div>
 <link rel="stylesheet" type="text/css" href="http://www.htmlcommentbox.com/static/skins/bootstrap/twitter-bootstrap.css" />
 <script type="text/javascript" language="javascript" id="hcb"> /*<!--*/ if(!window.hcb_user){hcb_user={};} (function(){s=document.createElement("script");s.setAttribute("type","text/javascript");s.setAttribute("src", "http://www.htmlcommentbox.com/jread?page="+escape((window.hcb_user && hcb_user.PAGE)||(""+window.location)).replace("+","%2B")+"&mod=%241%24wq1rdBcg%2467Xf3lAX9xPJwe3zcrLOQ/"+"&opts=478&num=10");if (typeof s!="undefined") document.getElementsByTagName("head")[0].appendChild(s);})(); /*-->*/ </script>
<!-- end htmlcommentbox.com -->
      </div>

      <hr>

      <div class="footer">
        <p>&copy; Harvix 2012</p>
      </div>

    </div> <!-- /container -->

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

  </body>
</html>
EOF
;
}


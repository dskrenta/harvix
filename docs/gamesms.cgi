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
    <title>Howlix Games</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Howlix free online  Games">
    <meta name="author" content=" David Skrenta">

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
    <link rel="apple-touch-icon-precomposed" sizes="144x144" href="http://twitter.github.com/bootstrap//assets/ico/apple-touch-icon-144-precomposed.png">
    <link rel="apple-touch-icon-precomposed" sizes="114x114" href="http://twitter.github.com/bootstrap//assets/ico/apple-touch-icon-114-precomposed.png">
      <link rel="apple-touch-icon-precomposed" sizes="72x72" href="http://twitter.github.com/bootstrap//assets/ico/apple-touch-icon-72-precomposed.png">
                    <link rel="apple-touch-icon-precomposed" href="http://twitter.github.com/bootstrap//assets/ico/apple-touch-icon-57-precomposed.png">
                                   <link rel="shortcut icon" href="http://twitter.github.com/bootstrap//assets/ico/favicon.png">
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
            <a class="brand" href="#">Howlix Games</a>
            <!-- Responsive Navbar Part 2: Place all navbar contents you want collapsed withing .navbar-collapse.collapse. -->
            <div class="nav-collapse collapse">
              <ul class="nav">
                <li class="active"><a href="#">Home</a></li>
                <li><a href="#about">Strategy</a></li>
                <li><a href="#contact">Car</a></li>
		<li><a href="#contact">Shooting</a></li>
		<li><a href="#contact">Sports</a></li>
		<li><a href="#contact">Action</a></li>
		<li><a href="#contact">Zombie</a></li>
		<li><a href="#contact">Arcade</a></li>
		<li><a href="#contact">HTML5</a></li>
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
          <img src="https://lh5.googleusercontent.com/-q6rFCgMV7Pk/TW6tJrjEuSI/AAAAAAAAAhk/r6awzIfOhZ8/s400/tower10.jpg" alt="">
          <div class="container">
            <div class="carousel-caption">
              <h1>Warzone Tower Defense</h1>
              <a class="btn btn-large btn-primary" href="games2.cgi?2">Play Now</a>
            </div>
          </div>
        </div>
        <div class="item">
          <img src="http://cdn1.kongregate.com/game_icons/0017/9536/icon5.jpg?8012-op" alt="">
          <div class="container">
            <div class="carousel-caption">
              <h1>Epic Battle Fantasy 3</h1>
              <a class="btn btn-large btn-primary" href="games2.cgi?3">Play Now</a>
            </div>
          </div>
        </div>
        <div class="item">
          <img src="http://cdn2.kongregate.com/game_icons/0018/3630/monster_slayers_100x75.png?11092-op" alt="">
          <div class="container">
            <div class="carousel-caption">
              <h1>Monster Slayers</h1>
              <a class="btn btn-large btn-primary" href="games2.cgi?4">Play Now</a>
            </div>
          </div>
        </div>
<div class="item">
          <img src="http://cdn4.kongregate.com/game_icons/0009/4952/ew3kong.jpg?4402-op" alt="">
          <div class="container">
            <div class="carousel-caption">
              <h1>Epic War 3</h1>
              <a class="btn btn-large btn-primary" href="games2.cgi?5">Play Now</a>
            </div>
          </div>
        </div>
<div class="item">
          <img src="http://cdn2.kongregate.com/game_icons/0026/4306/VillainousKongLogo_site.png?26585-op" alt="">
          <div class="container">
            <div class="carousel-caption">
              <h1>Villainous</h1>
              <a class="btn btn-large btn-primary" href="games2.cgi?6">Play Now</a>
            </div>
          </div>
        </div>
<div class="item">
          <img src="http://cdn2.kongregate.com/game_icons/0017/0636/ew4k.jpg?3349-op" alt="">
          <div class="container">
            <div class="carousel-caption">
              <h1>Epic War 4</h1>
              <a class="btn btn-large btn-primary" href="games2.cgi?7">Play Now</a>
            </div>
          </div>
        </div>
<div class="item">
          <img src="http://cdn3.kongregate.com/game_icons/0001/8807/pr2_thumb.png?31659-op" alt="">
          <div class="container">
            <div class="carousel-caption">
              <h1>Platform Racing 2</h1>
              <a class="btn btn-large btn-primary" href="games2.cgi?8">Play Now</a>
            </div>
          </div>
        </div>
<div class="item">
          <img src="http://cdn4.kongregate.com/game_icons/0019/0478/thumb100x75.jpg?9359-op" algt="">
          <div class="container">
            <div class="carousel-caption">
              <h1>Gravitee Wars</h1>
              <a class="btn btn-large btn-primary" href="games2.cgi?9">Play Now</a>
            </div>
          </div>
        </div>
<div class="item">
          <img src="http://cdn1.kongregate.com/game_icons/0028/0121/CycloManiacs_Thumb_site.jpg?10535-op" alt="">
          <div class="container">
            <div class="carousel-caption">
              <h1>CycloManiacs 2</h1>
              <a class="btn btn-large btn-primary" href="games2.cgi?10">Play Now</a>
            </div>
          </div>
        </div>
<div class="item">
          <img src="http://cdn2.kongregate.com/game_icons/0031/5056/125x100_site.jpg?7971-op" algt="">
          <div class="container">
            <div class="carousel-caption">
              <h1>Legend of the Void</h1>
              <a class="btn btn-large btn-primary" href="games2.cgi?11">Play Now</a>
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
                  <img src="http://cdn2.kongregate.com/game_icons/0025/7656/thumbnail_site.jpg?17844-op" alt="">
                  <div class="caption">
                    <h3>Learn to Fly 2</h3>
                    <p><a href="games2.cgi?2" class="btn btn-primary">Play Now</a></p>
                  </div>
                </div>
              </li>
              <li class="span4">
                <div class="thumbnail">
                  <img src="http://cdn1.kongregate.com/game_icons/0017/9536/icon5.jpg?8012-op" alt="">
                  <div class="caption">
                    <h3>Epic Battle Fantasy 3</h3>
                    <p><a href="games2.cgi?3" class="btn btn-primary">Play Now</a></p>
                  </div>
                </div>
              </li>
              <li class="span4">
                <div class="thumbnail">
                  <img src="http://cdn2.kongregate.com/game_icons/0018/3630/monster_slayers_100x75.png?11092-op" alt="">
                  <div class="caption">
                    <h3>Monster Slayers</h3>
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
                  <img src="http://cdn4.kongregate.com/game_icons/0009/4952/ew3kong.jpg?4402-op" alt="">
                  <div class="caption">
                    <h3>Epic War 3</h3>
                    <p><a href="games2.cgi?5" class="btn btn-primary">Play Now</a></p>
                  </div>
                </div>
              </li>
              <li class="span4">
                <div class="thumbnail">
                  <img src="http://cdn2.kongregate.com/game_icons/0026/4306/VillainousKongLogo_site.png?26585-op" alt="">
                  <div class="caption">
                    <h3>Villainous</h3>
                    <p><a href="games2.cgi?6" class="btn btn-primary">Play Now</a></p>
                  </div>
                </div>
              </li>
              <li class="span4">
                <div class="thumbnail">
                  <img src="http://cdn2.kongregate.com/game_icons/0017/0636/ew4k.jpg?3349-op" alt="">
                  <div class="caption">
                    <h3>Epic War 4</h3>
                    <p><a href="games2.cgi?7" class="btn btn-primary">Play Now</a></p>
                  </div>
                </div>
              </li>
            </ul>
          </div>
   <div class="row-fluid">
            <ul class="thumbnails">
              <li class="span4">
                <div class="thumbnail">
                  <img src="http://cdn3.kongregate.com/game_icons/0001/8807/pr2_thumb.png?31659-op" alt="">
                  <div class="caption">
                    <h3>Platform Racing 2</h3>
                    <p><a href="games2.cgi?8" class="btn btn-primary">Play Now</a></p>
                  </div>
                </div>
              </li>
              <li class="span4">
                <div class="thumbnail">
                  <img src="http://cdn4.kongregate.com/game_icons/0019/0478/thumb100x75.jpg?9359-op" alt="">
                  <div class="caption">
                    <h3>Gravitee Wars</h3>
                    <p><a href="games2.cgi?9" class="btn btn-primary">Play Now</a></p>
                  </div>
                </div>
              </li>
              <li class="span4">
                <div class="thumbnail">
                  <img src="http://cdn1.kongregate.com/game_icons/0028/0121/CycloManiacs_Thumb_site.jpg?10535-op" alt="">
                  <div class="caption">
                    <h3>CycloManiacs 2</h3>
                    <p><a href="games2.cgi?10" class="btn btn-primary">Play Now</a></p>
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
                    <p><a href="games2.cgi?11" class="btn btn-primary">Play Now</a></p>
                  </div>
                </div>
              </li>
              <li class="span4">
                <div class="thumbnail">
                  <img src="http://cdn4.kongregate.com/game_icons/0036/3878/125x100_site.png?19452-op" alt="">
                  <div class="caption">
                    <h3>BasketBalls Level Pack</h3>
                    <p><a href="games2.cgi?12" class="btn btn-primary">Play Now</a></p>
                  </div>
                </div>
              </li>
              <li class="span4">
                <div class="thumbnail">
                  <img src="http://cdn2.kongregate.com/game_icons/0042/8428/icon_cookiequest_kong_250x200_site.png?16578-op" alt="">
                  <div class="caption">
                    <h3>Flying Cookie Quest</h3>
                    <p><a href="games2.cgi?13" class="btn btn-primary">Play Now</a></p>
                  </div>
                </div>
              </li>
            </ul>
          </div>




      <hr class="featurette-divider">

<h2>Top HTML5 Games:</h2>
 <div class="row-fluid">
            <ul class="thumbnails">
              <li class="span4">
                <div class="thumbnail">
                  <img src="http://cdn2.kongregate.com/game_icons/0031/5056/125x100_site.jpg?7971-op" alt="">
                  <div class="caption">
                    <h3>Legend of the Void</h3>
                    <p><a href="games2.cgi?11" class="btn btn-primary">Play Now</a></p>
                  </div>
                </div>
              </li>
              <li class="span4">
                <div class="thumbnail">
                  <img src="http://cdn4.kongregate.com/game_icons/0036/3878/125x100_site.png?19452-op" alt="">
                  <div class="caption">
                    <h3>BasketBalls Level Pack</h3>
                    <p><a href="games2.cgi?12" class="btn btn-primary">Play Now</a></p>
                  </div>
                </div>
              </li>
              <li class="span4">
                <div class="thumbnail">
                  <img src="http://cdn2.kongregate.com/game_icons/0042/8428/icon_cookiequest_kong_250x200_site.png?16578-op" alt="">
                  <div class="caption">
                    <h3>Flying Cookie Quest</h3>
                    <p><a href="games2.cgi?13" class="btn btn-primary">Play Now</a></p>
                  </div>
                </div>
              </li>
            </ul>
          </div>



	  <hr class="featurette-divider">


      <!-- FOOTER -->
      <footer>
        <p class="pull-right"><a href="#">Back to top</a></p>
        <p>&copy; 2012 Howlix Search</p>
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
print"<h3>Learn to Fly 2</h3>\n";
print"<embed width=\"700\" height=\"500\" base=\"http://external.kongregate-games.com/gamez/0011/5608/live/\" src=\"http://external.kongregate-games.com/gamez/0011/5608/live/embeddable_115608.swf\" type=\"application/x-shockwave-flash\"></embed>";
print_footer();
}

if ( $page eq '3' )
{
print_header();
print"<h3>Epic Battle Fantasy 3</h3>\n";print"<embed width=\"700\" height=\"500\" base=\"http://external.kongregate-games.com/gamez/0009/0613/live/\" src=\"http://external.kongregate-games.com/gamez/0009/0613/live/embeddable_90613.swf\" type=\"application/x-shockwave-flash\"></embed>";
print_footer();
}

if ( $page eq '4' )
{
print_header();
print"<h3>Monster Slayers</h3>\n";print"<embed width=\"700\" height=\"500\" base=\"http://external.kongregate-games.com/gamez/0009/2661/live/\" src=\"http://external.kongregate-games.com/gamez/0009/2661/live/embeddable_92661.swf\" type=\"application/x-shockwave-flash\"></embed>";
print_footer();
}

if ( $page eq '5' )
{
print_header();
print"<h3>Epic War 3</h3>\n";print"<embed width=\"700\" height=\"500\" base=\"http://external.kongregate-games.com/gamez/0004/8201/live/\" src=\"http://external.kongregate-games.com/gamez/0004/8201/live/embeddable_48201.swf\" type=\"application/x-shockwave-flash\"></embed>";
print_footer();
}

if ( $page eq '6' )
{
print_header();
print"<h3>Villainous</h3>\n";print"<embed width=\"700\" height=\"500\" base=\"http://external.kongregate-games.com/gamez/0011/7271/live/\" src=\"http://external.kongregate-games.com/gamez/0011/7271/live/embeddable_117271.swf\" type=\"application/x-shockwave-flash\"></embed>";
print_footer();
}

if ( $page eq '7' )
{
print_header();
print"<h3>Epic War 4</h3>\n";print"<embed width=\"700\" height=\"500\" base=\"http://external.kongregate-games.com/gamez/0008/6156/live/\" src=\"http://external.kongregate-games.com/gamez/0008/6156/live/embeddable_86156.swf\" type=\"application/x-shockwave-flash\"></embed>";
print_footer();
}

if ( $page eq '8' )
{
print_header();
print"<h3>Platform Racing 2</h3>\n";print"<embed width=\"700\" height=\"500\" base=\"http://external.kongregate-games.com/gamez/0001/0110/live/\" src=\"http://external.kongregate-games.com/gamez/0001/0110/live/embeddable_10110.swf\" type=\"application/x-shockwave-flash\"></embed>";
print_footer();
}

if ( $page eq '9' )
{
print_header();
print"<h3>Gravitee Wars</h3>\n";print"<embed width=\"700\" height=\"500\" base=\"http://external.kongregate-games.com/gamez/0009/6087/live/\" src=\"http://external.kongregate-games.com/gamez/0009/6087/live/embeddable_96087.swf\" type=\"application/x-shockwave-flash\"></embed>";
print_footer();
}

if ( $page eq '10' )
{
print_header();
print"<h3>CycloManiacs 2</h3>\n";print"<embed width=\"700\" height=\"500\" base=\"http://external.kongregate-games.com/gamez/0012/1218/live/\" src=\"http://external.kongregate-games.com/gamez/0012/1218/live/embeddable_121218.swf\" type=\"application/x-shockwave-flash\"></embed>";
print_footer();
}

if ( $page eq '11' )
{
print_header();
print"<h3>Legend of the Void</h3>\n";print"<embed width=\"700\" height=\"500\" base=\"http://external.kongregate-games.com/gamez/0012/9964/live/\" src=\"http://external.kongregate-games.com/gamez/0012/9964/live/embeddable_129964.swf\" type=\"application/x-shockwave-flash\"></embed>";
print_footer();
}

if ( $page eq '12' )
{
print_header();
print"<h3>BasketBalls Level Pack</h3>\n";print"<embed width=\"700\" height=\"500\" base=\"http://external.kongregate-games.com/gamez/0014/2160/live/\" src=\"http://external.kongregate-games.com/gamez/0014/2160/live/embeddable_142160.swf\" type=\"application/x-shockwave-flash\"></embed>";
print_footer();
}

if ( $page eq '13' )
{
print_header();
print"<h3>Flying Cookie Quest</h3>\n";print"<embed width=\"700\" height=\"500\" base=\"http://external.kongregate-games.com/gamez/0016/0758/live/\" src=\"http://external.kongregate-games.com/gamez/0016/0758/live/embeddable_160758.swf\" type=\"application/x-shockwave-flash\"></embed>";
print_footer();
}

if ( $page eq '14')
{
print_header();
print"<h3>Warzone Tower Defense</h3>\n";
print"<embed type=\"application/x-shockwave-flash\" pluginspage=\"http://www.macromedia.com/go/getflashplayer\" src=\"http://towerdefense-games.com/images/games_3/warzone-tower-defense/warzone-tower-defense.swf\" quality=\"high\" name=\"warzone-tower-defense\" width=\"700\" height=\"500\"></embed>";
print_footer();
}



sub print_header
{
print <<EOX


<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Howlix Games</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Howlix free online Games">
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
    <link rel="apple-touch-icon-precomposed" sizes="144x144" href="http://twitter.github.com/bootstrap/assets/ico/apple-touch-icon-144-precomposed.png">
    <link rel="apple-touch-icon-precomposed" sizes="114x114" href="http://twitter.github.com/bootstrap/assets/ico/apple-touch-icon-114-precomposed.png">
      <link rel="apple-touch-icon-precomposed" sizes="72x72" href="http://twitter.github.com/bootstrap/assets/ico/apple-touch-icon-72-precomposed.png">
                    <link rel="apple-touch-icon-precomposed" href="http://twitter.github.com/bootstrap/assets/ico/apple-touch-icon-57-precomposed.png">
                                   <link rel="shortcut icon" href="http://twitter.github.com/bootstrap/assets/ico/favicon.png">
  </head>

  <body>

    <div class="container-narrow">

      <div class="masthead">
        <ul class="nav nav-pills pull-right">
          <li class="active"><a href="games2.cgi">Back to Home</a></li>
        </ul>
        <h3 class="muted">Howlix Games</h3>
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
        <p>&copy; Howlix Search 2012</p>
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


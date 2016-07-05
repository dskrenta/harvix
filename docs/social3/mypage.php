<?php
session_start();
?>

<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Harvix</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="">
    <meta name="author" content="">

    <!-- Le styles -->
    <link href="http://harvix.com/assets/bootstrap.css" rel="stylesheet">
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



    /* CUSTOMIZE THE CAROUSEL
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
      z-index: 10;
    }

    .carousel .item {
      height: 500px;
    }
    .carousel-img {
      position: absolute;
      top: 0;
      left: 0;
    }

    .carousel-caption {
      background-color: transparent;
      position: static;
      max-width: 550px;
      padding: 0 20px;
      margin-top: 100px;
    }
    .carousel-caption h1,
    .carousel-caption .lead {
      line-height: 1.25;
      color: #fff;
      text-shadow: 0 1px 1px rgba(0,0,0,.4);
    }
    .carousel-caption .btn {
      margin-top: 10px;
    }


   a:link {color:#black; text-decoration: none;}      /* unvisited link */
   a:visited {color:#black; text-decoration: none;}  /* visited link */
   a:hover {color:#black; text-decoration: none;}  /* mouse over link */
   a:active {color:#black; text-decoration: none;}  /* selected link */

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
      margin: 40px 0; /* Space out the Bootstrap <hr> more */
    }
    .featurette {
      overflow: hidden; /* Vertically center images part 2: clear their floats. */
    }


    /* Thin out the marketing headings */
    .featurette-heading {
      font-size: 40px;
      font-weight: 300;
      line-height: 1;
      letter-spacing: -1px;
    }

    </style>


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
            <button type="button" class="btn btn-navbar" data-toggle="collapse" data-target=".nav-collapse">
              <span class="icon-bar"></span>
              <span class="icon-bar"></span>
              <span class="icon-bar"></span>
            </button>
            <a class="brand" href=""><?php echo $_SESSION['myusername']; ?></a>
            <!-- Responsive Navbar Part 2: Place all navbar contents you want collapsed withing .navbar-collapse.collapse. -->
            <div class="nav-collapse collapse">
              <ul class="nav">
                <li class="active"><a href="http://harvix.com/social/mypage.php">Home</a></li>
                <li><a href="http://harvix.com/social/about.php">Media</a></li>
                <li><a href="http://harvix.com/social/photos.php">Followers</a></li>
		<li><a href="http://harvix.com/social/friends.php">Following</a></li>
		<li><a href="http://harvix.com/social/login_success.php">Search</a></li>
                <!-- Read about Bootstrap dropdowns at http://twbs.github.com/bootstrap/javascript.html#dropdowns -->
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
          </div><!-- /.navbar-inner -->
        </div><!-- /.navbar -->

      </div> <!-- /.container -->
    </div><!-- /.navbar-wrapper -->



    <!-- Carousel
    ================================================== -->
    <center>
    <div id="myCarousel" class="carousel slide">
      <div class="carousel-inner">
        <div class="item active">
          <img class="carousel-img" src="http://cache.gawkerassets.com/assets/images/gizmodo/2009/08/Pinstripe.jpg" alt="">
          <div class="container">
	     <div class="carousel-caption">
		<img class="img-polaroid" src="https://fbcdn-profile-a.akamaihd.net/hprofile-ak-ash4/c207.2.546.546/s160x160/207807_582977028394450_1334487058_n.jpg"/>
		<h1><?php echo $_SESSION['myusername']; ?></h1>
	        <p class="lead">CEO and Founder Harvix - Research engine for students, 14-year-old entrepreneur, Developer/Designer/Hacker, Scientist, and Athlete.</p>
	    	<p class="lead">San Carlos, California &middot; harvix.com</p>
            </div>
          </div>
        </div>
      </div>
    </div><!-- /.carousel -->
    </center>


    <!-- Marketing messaging and featurettes
    ================================================== -->
    <!-- Wrap the rest of the page in another container to center all the content. -->

    <div class="container marketing">

      <!-- START THE POSTS -->

      <div class="featurette">
	<h3 class="featurette-heading">dskrenta shared Harvix's photo</h3>
	<hr></hr>
        <img class="featurette-image img-rounded" width="100%" src="https://fbcdn-sphotos-g-a.akamaihd.net/hphotos-ak-prn2/965360_379419242157796_2023962751_o.jpg">
        <p>
	<p class="lead">We will be updating our background images soon! If you want to recommend a amazing picture, comment on this post.</p>
    	<div class="btn-group">
  	<button class="btn">Like</button>
  	<button class="btn">Comment</button>
  	<button class="btn">Share</button>
	</div>
      </div>

      <hr class="featurette-divider">

      <div class="featurette">
        <h3 class="featurette-heading">dskrenta updated their profile picture</h3>
        <hr></hr>
	<img class="featurette-image img-rounded" width="100%" src="https://fbcdn-sphotos-f-a.akamaihd.net/hphotos-ak-ash4/s720x720/207807_582977028394450_1334487058_n.jpg">
        <p>
        <div class="btn-group">
        <button class="btn">Like</button>
        <button class="btn">Comment</button>
        <button class="btn">Share</button>
        </div>
      </div>

      <hr class="featurette-divider">

      <div class="featurette">
        <h3 class="featurette-heading">dskrenta shared Rich Skrenta's photo</h3>
        <hr></hr>
	<img class="featurette-image img-rounded" width="100%" src="https://fbcdn-sphotos-h-a.akamaihd.net/hphotos-ak-frc1/1008280_10151734140146934_2104943686_o.jpg">
        <p>
        <div class="btn-group">
        <button class="btn">Like</button>
        <button class="btn">Comment</button>
        <button class="btn">Share</button>
        </div>
      </div>

      <hr class="featurette-divider">

      <!-- /END THE FEATURETTES -->


      <!-- FOOTER -->
      <footer>
        <p class="pull-right"><a href="#">Back to top</a></p>
        <p>&copy; 2013 Harvix &middot; <a href="http://harvix.com/newabout.html">About</a> &middot; <a href="http://harvix.com/newterms.html">Terms + Privacy</a></p>
      </footer>

    </div><!-- /.container -->



    <!-- Le javascript
    ================================================== -->
    <!-- Placed at the end of the document so the pages load faster -->
    <script src="http://harvix.com/assets/jquery.js"></script>
    <script src="http://harvix.com/assets/transition.js"></script>
    <script src="http://harvix.com/assets/alert.js"></script>
    <script src="http://harvix.com/assets/modal.js"></script>
    <script src="http://harvix.com/assets/dropdown.js"></script>
    <script src="http://harvix.com/assets/scrollspy.js"></script>
    <script src="http://harvix.com/assets/tab.js"></script>
    <script src="http://harvix.com/assets/tooltip.js"></script>
    <script src="http://harvix.com/assets/popover.js"></script>
    <script src="http://harvix.com/assets/button.js"></script>
    <script src="http://harvix.com/assets/collapse.js"></script>
    <script src="http://harvix.com/assets/carousel.js"></script>
    <script src="http://harvix.com/assets/typeahead.js"></script>
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


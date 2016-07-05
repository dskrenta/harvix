$(document).ready(function(){
    /*
    *   Global variables.
    */
    var pageHeight = $(window).height();
    var pageWidth = $(window).width();
    var navigationHeight = $("#navigation").outerHeight();
    
    /*
    *   ON RESIZE, check again
    */
    $(window).resize(function () {
        pageWidth = $(window).width();
        pageHeight = $(window).height();
    });
    
    /*
    *   ON LOAD
    */

    // Fix navigation.
    $('#navigation').fixedonlater();
    
    //Initialize scroll so if user droped to other part of page then home page.
    $(window).trigger('scroll');
   
    // Carousel "Quote slider" initialization.
    $('#quote-slider').carousel({
        interval: 20000
    })

    //Scroll spy and scroll filter
    $('#main-menu').onePageNav({
        currentClass: 'active',
        changeHash: false,
        scrollOffset: navigationHeight - 10,
        scrollThreshold: 0.5,
        scrollSpeed: 750,
        filter: '',
        easing: 'swing',
     });
    
    
    // Paralax initialization.
    // Exclude for mobile.
    if(pageWidth > 980){
        //Dont user paralax for tablet and mobile devices.
        $('#page-welcome').parallax("0%", 0.2);
        $('#page-features').parallax("0%", 0.07);
        $('#page-twitter').parallax("0%", 0.1);
    }
    
    //Emulate touch on table/mobile touchstart.
    if(typeof(window.ontouchstart) != 'undefined') {
        var touchElements = [".social-icons a", ".portfolio-items li", ".about-items .item"];
        
        $.each(touchElements, function (i, val) {
            $(val).each(function(i, obj) {
                $(obj).bind('click', function(e){
                
                    if($(this).hasClass('clickInNext')){
                        $(this).removeClass('clickInNext');
                    } else {
                        e.preventDefault();
                        e.stopPropagation();
                        
                        $(this).mouseover();
                        $(this).addClass('clickInNext');
                    }
                });
            });
        });
    }

    /*
    *   BLOCK | Navigation
    *
    *   Smooth scroll
    *   Main menu links
    *   Logo click on Welcome page
    */
    $('#page-welcome .logo a').click(function(){
        $('html, body').animate({
            scrollTop: $( $.attr(this, 'href') ).offset().top - navigationHeight + 4
            
        }, 800);
        
        //Fix jumping of navigation.
        setTimeout(function() {
            $(window).trigger('scroll');
        }, 900);
        
        return false;
    });
    
    
    /*
    *   PAGE | Welcome 
    *
    *   Initialize slider for welcome page H1 message.
    */
   $('#welcome-messages ul').bxSlider({
        mode: 'vertical',
        auto: true,
        minSlides: 1,
        responsive: true,
        touchEnabled: true,
        pager: false,
        controls: false,
        useCSS: false,
        pause: 10000
    });
    /*
    *   PAGE | WORK
    *
    *   .plugin-filter - Defines action links.
    *   .plugin-filter-elements - Defines items with li.
    */
    $('.plugin-filter').click(function(){
        return false;
    });
    $('.plugin-filter-elements').mixitup({
        targetSelector: '.mix',
        filterSelector: '.plugin-filter',
        sortSelector: '.sort',
        buttonEvent: 'click',
        effects: ['fade','rotateY'],
        listEffects: null,
        easing: 'smooth',
        layoutMode: 'grid',
        targetDisplayGrid: 'inline-block',
        targetDisplayList: 'block',
        gridClass: '',
        listClass: '',
        transitionSpeed: 600,
        showOnLoad: 'all',
        sortOnLoad: false,
        multiFilter: false,
        filterLogic: 'or',
        resizeContainer: true,
        minHeight: 0,
        failClass: 'fail',
        perspectiveDistance: '3000',
        perspectiveOrigin: '50% 50%',
        animateGridList: true,
        onMixLoad: null,
        onMixStart: null,
        onMixEnd: null
    });
    
    /*
    *   PAGE | Twitter 
    *   
    *   CONFIGURE FIRST
    *
    *   Pull latest tweets from user.
    *   Configuration: /plugins/twitter/index.php
    
    $('.twitterfeed').tweet({
        modpath: 'plugins/twitter/',
        username: 'TheGridelicious',
        count: 3
    });
    */
    
    //Prepare markup for twitter feed and carousel. Alow twitter to load. 1s, load time.
    setTimeout(function() {
        var myCarousel = $("#twitterfeed-slider");
        myCarousel.append("<ol class='carousel-indicators'></ol>");
        
        myCarousel.find('.tweet_list').addClass("carousel-inner");
        myCarousel.find('.tweet_list li').addClass('item').first().addClass("active");
            
        var indicators = myCarousel.find(".carousel-indicators"); 
        myCarousel.find(".carousel-inner").children(".item").each(function(index) {
            (index === 0) ? 
            indicators.append("<li data-target='#twitterfeed-slider' data-slide-to='"+index+"' class='active'></li>") : 
            indicators.append("<li data-target='#twitterfeed-slider' data-slide-to='"+index+"'></li>");
        });
        
        //After creating markup, start carousel.
       $('#twitterfeed-slider').carousel({
            interval: 5000,
            pause: "hover"
        });
        
    }, 1000);
});


/*
*   Ajax request.
*   Start loading.
*   Append loading notification.
*/
$( document ).ajaxSend( function() {

    // Show loader.
    if($(".loading").length == 0) {
        $("body").append('<div class="loading"><div class="progress progress-striped active"><div class="bar"></div></div></div>');
        $(".loading").slideDown();
        $(".loading .progress .bar").delay(300).css("width", "100%");
    }
});

/*
*   Reinitialize Scrollspy after ajax request is completed.
*   Refreshing will recalculate positions of each page in document.
*   Time delay is added to allow ajax loaded content to expand and change height of page.
*/
$( document ).ajaxComplete(function() {

    // Remove loading section.
    $(".loading").delay(1000).slideUp(500, function(){
        $(this).remove();
    });
    
    
    // Portfolio details - close.
    $(".close-portfolio span").click(function(e) {
        $(".portfolio-item-details").delay(500).slideUp(500, function(){
            $(this).remove();
        });
        
        window.location.hash= "!";
        return false;
    });
});


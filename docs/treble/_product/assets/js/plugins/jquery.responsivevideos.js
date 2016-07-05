/*!
 *  ResponsiveVideos.js v0.1
 *  Responsive iframe embeded video from YouTube/Vimeo.
 *  by Rewea: http://www.rewea.com
 *
 *  Copyright 2013 Rewea.com - Attribution-ShareAlike 3.0 Unported (CC BY-SA 3.0).
 *  http://creativecommons.org/licenses/by-sa/3.0/deed.en_US
 */
function responsivevideos(){  
    var $getVideos = $("iframe[src^='http://player.vimeo.com'], iframe[src^='http://www.youtube.com']");
    
    // Figure out and save aspect ratio for each video
    $getVideos.each(function() {
        //Get container width
        wrapperWidth =   $(this).parent().width();
        currentHeight =  $(this).height();
        currentWidth =   $(this).width();
        
        currentAspectRation =  currentHeight / currentWidth;
        
        $(this).removeAttr('height').removeAttr('width');
        $(this).width(wrapperWidth).height(parseInt(currentAspectRation * wrapperWidth));
    });
    
    
};

//Initialize after page is loaded
!function ($) {
    responsivevideos();
}(window.jQuery)


//On resize, adapt videos.
$(window).bind('resize', function() {
    responsivevideos();
});

//If there was ajax loaded content in ajax.
$( document ).ajaxComplete(function() {
    // Check if there is video and rezise it if needed.
    responsivevideos();
});
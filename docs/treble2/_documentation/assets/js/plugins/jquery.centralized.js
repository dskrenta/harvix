/*!
 *  centralized.js v0.1
 *  Centralize elements by width and height.
 *  Usage in combination with css, class .centralized
 *
    .centralized {
        left: 50%;
        top: 50%;
        float: left;
        position: relative;
        visibility: hidden;
        .opacity(0);
    }
 *
 *  by Rewea: http://www.rewea.com
 *
 *  Copyright 2013 Rewea.com - Attribution-ShareAlike 3.0 Unported (CC BY-SA 3.0).
 *  http://creativecommons.org/licenses/by-sa/3.0/deed.en_US
 */

function centralized(){
    var config = {
        'delay': 1500,
        'fadeSpeed': 500
    };
    
    var obj = $('.centralized');
    
    return obj.each(function(){
    
        setTimeout(function() {
            obj.css("margin-top", "-" + Math.max(0, (obj.outerHeight() / 2)) + "px");
            obj.css("margin-left", "-" + Math.max(0, (obj.outerWidth() / 2)) + "px");
            obj.css('visibility','visible');
            obj.fadeTo(500, 1);
            
       
        }, config.delay);
    });
    
};

// Centralize all objects.
!function ($) {
    centralized();
}(window.jQuery)


// Centralize after resize.
$(window).bind('resize', function() {
    centralized();
});
$(document).ready(function($){
    //scrolling menu
    var nav = $('#menu');

    $(window).scroll(function () {
            if ($(this).scrollTop() > 78) {
                    nav.addClass("f-nav");
            } else {
                    nav.removeClass("f-nav");
            }
    });

    //smoothe scrolling
    $('#menu a').click(function(){
        $('html, body').animate({
            scrollTop: $( $(this).attr('href') ).offset().top - 40
        }, 500);
        return false;
    });
});
var scrollTopOffset = $('#wrapper').outerHeight() + 60;

$('.nav-link').on('click', function(evt){
    // stop the default browser behaviour for the click
    // on the sidebar navigation link
    evt.preventDefault();
    // get a handle on the target element of the clicked link
    var $target = $($(this).attr('href'));
    // manually scroll the window vertically to the correct
    // offset to nicely display the target element at the top
    $(window).scrollTop($target.offset().top-(scrollTopOffset));
});

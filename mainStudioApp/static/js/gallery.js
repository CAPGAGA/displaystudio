// expand card on click
$(document).ready(function(){
    $(".gallery-card").click(function(e){
        $(".gallery-card").removeClass("active");
        e.preventDefault();
        $(this).toggleClass("active");
    })
})



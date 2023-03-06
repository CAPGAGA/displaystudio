$("#form-button").click(function(){
    if($('#form-check').is(":checked")){
    send_request($('#form-name').val(),$('#form-phone').val(),$('#form-email').val());
    }else{
    $('.warning-text').removeAttr('hidden');
    return false;
    }
})


function send_request(name, phone, email){
    const url = 'get-form'
    var csrftoken = getCookie('csrftoken');

    fetch(url, {
        method: 'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken': csrftoken,
        },
        body:JSON.stringify({'name':name, 'phone': phone, 'email': email})
    })

    .then((response) =>{
        return response.json()
    })

    .then((data)=>{
        console.log(data)
        location.reload()
    })
}

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
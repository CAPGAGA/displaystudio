const m_range = $('#m-range'),
m_total = $('#m-total'),

prices_m = {
    'olha': 40000,
    'buk': 48000,
    'dub': 49000,
    'oreh': 62800,
    'kiparis': 70000,
    'polystyle': 30000,
    'metr-mkad': 3000,
    'metr-pst-mkad': 5000,
    'delivery': 1500,
};

window.service_price = 0;

$(document).ready(function(){
    m_total.text(''.concat('Ваша площадь:', m_range.val(),'м2'));

})

$(document).on('input', m_range, function(){
    m_total.text(''.concat('Ваша площадь:', m_range.val(),'м2'));
    if(window.material_price){
        let m_price = 0;
        m_price = window.material_price * m_range.val();
        window.metr_price = m_price;
    }
})

$(document).on('click', '.construct-radio', function(){
    window.material_price = prices_m[$(this).attr('id')];

})

$(document).on('click', '.constructor-checkbox', function(){
    if($(this).prop("checked")){
        if($(this).attr('id').toString()!='montage'){
            console.log(1);
            window.service_price += prices_m[$(this).attr('id')];
        }
    }
    else{
        if($(this).attr('id').toString()!='montage'){
            console.log(1);
            window.service_price -= prices_m[$(this).attr('id')];
        }
    };
})

$(document).on('change', '.constructor-wrapper', function(){
    final_price = 0;
    if(window.service_price){
        final_price+=window.service_price;
    }
    if(window.metr_price){
        final_price+=window.metr_price;
    }
    if($('#montage').prop("checked") && final_price != 0){
        montage_price = window.metr_price * 0.1;
        final_price += montage_price;
    }

    $('.total-price').text('ИТОГ:'.concat(' ', final_price, 'руб.'));
})

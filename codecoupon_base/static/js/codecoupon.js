odoo.define('codecoupon_base.couponcontrol', function (require) {
    'use strict';
    var ajax = require('web.ajax');
    $(document).ready(function() {
        var dev_mode_message = '<p class="bg-info">It is necessary to <a onclick="window.location.replace(window.location.href)">reload the page</a> to apply the coupon</p>';
        $('.ccb_wrap').show();
        /* Apply discount coupon */
        $('.ccb_wrap form#ccb_to_apply').on('submit', function(e){
            e.preventDefault();
            var coupon_code = $('input[name="ccb_code"]').val();
            if(coupon_code.length > 0){
                /* Show load spinner */
                $('.wp-ccb_load').toggle();
                /* Ajax coupon check call */
                ajax.jsonRpc('/shop/codecoupon/check', 'call', {
                    'coupon_code': coupon_code
                }).then(function (data) {
                    data = $.parseJSON(data);
                    setTimeout(function(){
                        if(data['success'] == true){
                            if(data['develop'] == true){
                                /* If developer mode is enabled, automatic page reload is disabled */
                                $('.ccb_message').show().html('<p class="bg-'+data['flag']+'">'+data['message']+'</p>' + dev_mode_message);
                                $('.wp-ccb_load').toggle();
                            } else {
                                window.location.replace(window.location.href);
                            }
                        } else {
                            $('.ccb_message').show().html('<p class="bg-'+data['flag']+'">'+data['message']+'</p>');
                            $('.wp-ccb_load').toggle();
                        }
                    }, 500);
                });
            } else {
                $('.ccb_message').show().html('<p class="bg-warning">Coupon code is empty</p>');
            }
        });
        /* Delete discount coupon */
        $('.ccb_wrap form#ccb_to_remove').on('submit', function(e){
            e.preventDefault();
            var coupon_code = $('input[name="ccb_code"]').val();
            /* Show load spinner */
            $('.wp-ccb_load').toggle();
            /* Ajax call to delete the coupon */
            ajax.jsonRpc('/shop/codecoupon/remove', 'call', {
                'coupon_code': coupon_code
            }).then(function (data) {
                data = $.parseJSON(data);
                setTimeout(function(){
                    if(data['success'] == true){
                        if(data['develop'] == true){
                            /* If developer mode is enabled, automatic page reload is disabled */
                            $('.ccb_message').show().html('<p class="bg-'+data['flag']+'">'+data['message']+'</p>' + dev_mode_message);
                            $('.wp-ccb_load').toggle();
                        } else {
                            window.location.replace(window.location.href);
                        }
                    } else {
                        $('.ccb_message').show().html('<p class="bg-'+data['flag']+'">'+data['message']+'</p>');
                        $('.wp-ccb_load').toggle();
                    }
                }, 500);
            });
        });
    });
});
/* Coupon form hide on any cart change */
$('#cart_products').ready(function(){
    var object = this;
    $(object).on("change", "input.js_quantity", function(){
        /* Show load spinner and remove coupon form if order has a coupon applied */
        $('.wp-ccb_load').toggle();
        setTimeout(function(){
            if($('.ccb_wrap').hasClass('ccb_to_remove')){
                $('.ccb_wrap').remove();
                /* Auto page reload after the waiting time */
                setTimeout(function(){window.location.replace(window.location.href)}, 3000);
            }
            $('.wp-ccb_load').toggle();
        }, 250);
    });
});

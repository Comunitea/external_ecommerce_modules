odoo.define('follow_us_base.subscribe_actions', function (require) {
    'use strict';
    var ajax = require('web.ajax');

    $('.subscription-banner').ready(function() {
        var email = $('input[name="email"]').val(),
            channel = $('.subscription-banner').attr('data-channel'),
            regex = /^([a-zA-Z0-9_\.\-\+])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/;

        /* Subscribe action */
        $('.js_subscribe_banner_btn').on('click', function(e){
            e.preventDefault();
            if(!regex.test(email)){
                $('.fub_invalid').removeClass('hidden');
            }else{
                $('.wp-subscription_form .alert').addClass('hidden');
                ajax.jsonRpc('/followus/subscribe', 'call', {
                    'email': email,
                    'channel_ids': [channel]
                }).then(function (data) {
                    data = $.parseJSON(data);
                    if(data['success'] == true){
                        $('.subscription_form').hide();
                        $('.fub_thanks').removeClass('hidden');
                    }else{
                        $('.fub_error').removeClass('hidden');
                    }
                });
            }
        });

        /* Unsubscribe action */
        $('.js_un_subscribe_banner_btn').on('click', function(e){
            e.preventDefault();
            ajax.jsonRpc('/followus/unsubscribe', 'call', {
                    'email': email,
                    'channel_ids': [channel]
                }).then(function (data) {
                    data = $.parseJSON(data);
                    if(data['success'] == true){
                        $('.subscription_form').hide();
                        $('.fub_unsubscribed').removeClass('hidden');
                    }else{
                        $('.fub_error').removeClass('hidden');
                    }
                });
        });
    });

});
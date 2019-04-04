odoo.define('follow_us_base.subscribe_actions', function (require) {
    'use strict';
    var ajax = require('web.ajax');

    $(document).ready(function() {
        /* Subscribe action */
        $('.js_subscribe_btn').on('click', function(e){
            e.preventDefault();
            var email = $('input[name="email"]').val();
            var channel = $('.subscription_form').attr('data-channel');
            var regex = /^([a-zA-Z0-9_\.\-\+])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/;

            if(!regex.test(email)){
                $('.fub_invalid').removeClass('hidden');
            }else{
                ajax.jsonRpc('/followus/subscribe', 'call', {
                    'email': email,
                    'channel': channel
                }).then(function (data) {
                    data = $.parseJSON(data);
                    if(data['success'] == true){
                        $('.wp-subscription_form .alert').addClass('hidden');
                        $('.subscription_form').hide();
                        $('.fub_thanks').removeClass('hidden');
                    }else{
                        if(data['message'] != ''){
                            $('.fub_message').html(data['message']).removeClass('hidden');
                        }else{
                            $('.fub_error').removeClass('hidden');
                        }
                    }
                });
            }

        });
        /* Unsubscribe action */
        $('.js_un_subscribe_btn').on('click', function(e){
            e.preventDefault();
            var email = $('input[name="email"]').val();
            var channel = $('.un_subscription_form').attr('data-channel');

            ajax.jsonRpc('/followus/unsubscribe', 'call', {
                'email': email,
                'channel': channel
            }).then(function (data) {
                data = $.parseJSON(data);
                if(data['success'] == true){
                    $('.wp-subscription_form .alert').addClass('hidden');
                    $('.un_subscription_form').hide();
                    $('.fub_unsubscribed').removeClass('hidden');
                }else{
                    $('.fub_error').removeClass('hidden');
                }
            });
        });
    });
});

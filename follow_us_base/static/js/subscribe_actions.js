odoo.define('follow_us_base.subscribe_actions', function (require) {
    'use strict';
    var ajax = require('web.ajax');

    $(document).ready(function() {
        $('.js_subscribe_btn').on('click', function(e){
            e.preventDefault();
            var email = $('input[name="email"]').val(),
                regex = /^([a-zA-Z0-9_\.\-\+])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/,
                ids_to_subscribe = [],
                ids_to_unsubscribe = [],
                success_add = false,
                success_del = false;

            $('.channel-id input').each(function(){
                if($(this).prop('checked')){
                    ids_to_subscribe.push($(this).attr('data-channel'))
                }else{
                    ids_to_unsubscribe.push($(this).attr('data-channel'))
                }
            });

            if(!regex.test(email)){
                $('.fub_invalid').removeClass('hidden');
            }else{
                $('.wp-subscription_form .alert').addClass('hidden');
                if (ids_to_subscribe.length > 0){
                    console.log('To subscribe: ' + ids_to_subscribe)
                    /* Subscribe action */
                    ajax.jsonRpc('/followus/subscribe', 'call', {
                        'email': email,
                        'channel_ids': ids_to_subscribe
                    }).then(function (data) {
                        data = $.parseJSON(data);
                        if(data['success'] == true){
                            $('.subscription_form').hide();
                            $('.fub_save').removeClass('hidden');
                        }else{
                            $('.fub_error').removeClass('hidden');
                        }
                    });
                }
                if (ids_to_unsubscribe.length > 0){
                    console.log('To unsubscribe: ' + ids_to_unsubscribe)
                    /* Unsubscribe action */
                    ajax.jsonRpc('/followus/unsubscribe', 'call', {
                        'email': email,
                        'channel_ids': ids_to_unsubscribe
                    }).then(function (data) {
                        data = $.parseJSON(data);
                        if(data['success'] == true){
                            $('.subscription_form').hide();
                            $('.fub_save').removeClass('hidden');
                        }else{
                            $('.fub_error').removeClass('hidden');
                        }
                    });
                }
            }

        });
    });
});

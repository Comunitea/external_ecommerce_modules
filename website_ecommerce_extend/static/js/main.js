odoo.define('website_ecommerce_extend.contact_form', function (require) {
    "use strict";

    var core = require('web.core');
    var _t = core._t;

    $(document).ready(function(){
        var default_email_msg = _t("Please, write your email with a right format such: your_name@provider.domain");
        $(".s_website_form").validate({
            rules: {
                email_from: {
                    required: true,
                    email: true
                }
            },
            messages: {
                email_from: {
                    required: default_email_msg,
                    email: default_email_msg
                }
            }
        });
    });
});

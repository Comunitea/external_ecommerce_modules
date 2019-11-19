$(document).ready(function(){
    var core = require('web.core');
    var _t = core._t;
    var default_email_msg = _t('Please, enter a valid email address');
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
$(document).ready(function(){
    var default_email_msg = 'Por favor, introduce una dirección de correo electrónico válida';
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
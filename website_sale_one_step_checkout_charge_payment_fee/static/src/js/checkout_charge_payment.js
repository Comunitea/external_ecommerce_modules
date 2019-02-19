/**
* Patching an existing class for modify start method. It is necessary for convert default checkout in OSC.
* thus, only add a ajax call to reload page when an acquirer is changed if is necessary.
* Includes a load gif image when reload is required.
*/

odoo.define("website_sale_one_step_checkout_charge_payment_fee.osc", function (require) {
    "use strict";

    var inherit = require('website_sale_one_step_checkout.osc');
    var ajax = require('web.ajax');

    var OneStepCheckoutChargePayment = inherit.include({
        start: function () {
            var self = this;

            // activate event listener
            self.changeShipping();
            self.hideShow();

            // Editing Billing Address
            $('.js-billing-address .js_edit_address').on('click',
                function (e) {
                    self.editBilling(null, self, e)
                });

            // Editing shipping address
            $('.js-shipping-address .js_edit_address').on('click', function (e) {
                self.editShipping(self, e)
            });

            // Add new shipping address
            $("#add-shipping-address").on('click', 'a, input', function (e) {
                self.addShipping(self, e)
            });

            $('#address-modal').on('click', '#js_confirm_address', function (ev) {
                ev.preventDefault();
                ev.stopPropagation();
                // Upon confirmation, validate data.
                self.validateModalAddress();
                return false;
            });

            // when choosing an acquirer, display its order now button
            var $payment = $('#payment_method');
            $payment.on('click', 'input[name="acquirer"]', function (ev) {
                var payment_id = $(ev.currentTarget).val();
                $('div.oe_sale_acquirer_button[data-id]').addClass('hidden');
                $('div.oe_sale_acquirer_button[data-id="' + payment_id + '"]').removeClass('hidden');

                // Get acquirer to check for fee payment, when true then reload page
                // It is necessary for simulate default checkout in one step checkout
                var acquirer = $('input[name="acquirer"]:checked'),
                data = {};
                data = self.getPostFields(acquirer, data);
                data['payment_fee_id'] = payment_id

                return ajax.jsonRpc('/shop/checkout/charge_payment/', 'call', data).then(function (result) {

                    // Load spinner gif image
                    var $spn_div = $('#col-3');
                    var spinner = '<div class="wp-load-spinner"/>';
                    $spn_div.append(spinner);

                    if (result['reload_page'] === true) {
                        window.location.reload(true);
                    } else {
                        $spn_div.find('.wp-load-spinner').fadeOut(300);
                        $spn_div.find('.wp-load-spinner').detach();
                    }
                });
            });

            // when clicking checkout submit button validate address data first
            // if all is fine trigger payment transaction
            $('#col-3 .js_payment').on('click', 'form button[type=submit]', function (ev) {
                ev.preventDefault();
                ev.stopPropagation();

                self.checkData().then(function (result) {
                    if (result.success) {
                        // proceed to payment transaction
                        self.proceedPayment(ev);
                    } else {
                        return false;
                        // do nothing, address modal in edit mode
                        // will get automatically opened at this point
                    }
                });
                return false;
            });
        },validateModalAddress: function () {
            var self = this;
            var formElems = $('#osc-modal-form input, #osc-modal-form select'),
                data = {};

            data = self.getPostFields(formElems, data);

            // For validation we need `submitted`
            data.submitted = true;
            $('.oe_website_sale_osc .has-error').removeClass('has-error');

            // Show load spinner
            $('#col-3').append('<div class="wp-load-spinner"/>');

            // Ajax call
            ajax.jsonRpc('/shop/checkout/render_address/', 'call', data).then(function (result) {
                if (result.success) {
                    $('#js_confirm_address').attr("disabled", false);

                    // Update frontend address view
                    $('#col-1').html(result.template);

                    // Re-enable JS event listeners
                    $('.js-billing-address .js_edit_address').on('click', function (e) {
                        self.editBilling(null, self, e)
                    });
                    $('.js-shipping-address .js_edit_address').on('click', function (e) {
                        self.editShipping(self, e)
                    });
                    $("#add-shipping-address").on('click', 'a', function (e) {
                        self.addShipping(self, e)
                    });
                    self.changeShipping();

                    // Reload page and hide Modal in case of success
                    setTimeout(function(){
                        window.location.reload(true);
                        $('#address-modal').modal('hide');
                    }, 250)
                } else if (result.errors) {
                    // Hide load spinner in case of errors
                    $('div.wp-load-spinner').remove();
                    if (result.errors.error_message) {
                        $(".text-danger").remove();
                        var $name = $('.checkout_autoformat > .div_name');
                        var prefix = '<h5 class="text-danger">';
                        var suffix = '</h5>';
                        $(result.errors.error_message).each(function () {
                            $name.prepend(
                                prefix + this + suffix
                            )
                        })
                    }
                    self.displayFormErrors(result.errors);
                } else {
                    // ???
                    window.location.href = '/shop';
                }
            });
        },changeShipping: function () {
            // Change kanban shipping in OSC
            $('#osc_shipping').on('click', '.js_change_shipping', function () {
                if (!$('body.editor_enable').length) {
                    // Show load spinner
                    $('#col-3').append('<div class="wp-load-spinner"/>');
                    // Change old
                    var $old = $('.all_shipping').find('.panel.border_primary');
                    $old.find('.btn-ship').toggle();
                    $old.addClass('js_change_shipping');
                    $old.removeClass('border_primary');
                    // Set new
                    var $new = $(this).parent('div.one_kanban').find('.panel');
                    $new.find('.btn-ship').toggle();
                    $new.removeClass('js_change_shipping');
                    $new.addClass('border_primary');
                    // Action
                    var $form = $(this).parent('div.one_kanban').find('form.hide');
                    $.post($form.attr('action'), $form.serialize() + '&xhr=1');
                    // Reload page to apply new shipping rules
                    setTimeout(function(){
                        window.location.reload(true);
                    }, 250)
                }
            });
        }
    });
});
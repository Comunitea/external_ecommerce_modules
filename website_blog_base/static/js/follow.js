odoo.define('website_blog_base.follow', function (require) {
    'use strict';

    var sAnimation = require('website.content.snippets.animation');
    var sLegalFollow = sAnimation.registry.follow;

    sAnimation.registry.sLegalFollow = sLegalFollow.extend({

        _onClick: function () {
            var $legal_check = $('.js_checkbox_legal');
            var $legal = $('.js_input_legal');
            if (!$legal.is(":checked") && this.$target.attr("data-follow") === 'off') {
//                console.log('BLOG - Legal Follow not accepted. Show error');
                $legal_check.addClass('has-error');
                return false;
            }
            $legal_check.removeClass('has-error');
            this._toggle_legal(this.$target.attr("data-follow"));
            this._super();
        },
        _toggle_legal: function (follow) {
            var $legal_check = $('.js_checkbox_legal');
            var $legal = $('.js_input_legal');
            if ($legal.is(":checked") && follow === 'off') {
//                console.log('BLOG - Subscribed. Hide legal');
                $legal_check.addClass("hidden");
                $legal.prop("checked", true);
            }
            else {
//                console.log('BLOG - Unsubscribed. Show legal');
                $legal_check.removeClass("hidden");
                $legal.prop("checked", false);
            }
            return true;
        },
    });
});

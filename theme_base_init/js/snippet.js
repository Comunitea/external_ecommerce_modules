(function() {
    'use strict';
    var website = odoo.website;
    website.odoo_website = {};

    website.snippet.options.snippet_testimonial_options = website.snippet.Option.extend({
        onFocus: function() {
            alert("On focus!");
        }
    })
})();
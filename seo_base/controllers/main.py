# -*- coding: utf-8 -*-

from odoo import http, SUPERUSER_ID
from odoo.http import request

from odoo.addons.website_sale.controllers.main import WebsiteSale


class WebsiteSale(WebsiteSale):
    """
    Product redirecting to slug URL
    """
    @http.route('/shop/product/<model("product.template"):product>', type='http', auth="public", website=True)
    def product(self, product, category='', search='', **kwargs):

        if product.slug:
            return http.local_redirect(
                '/product/%s' % product.slug,
                dict(http.request.httprequest.args),
                True,
                code='301'
            )

        return super(WebsiteSale, self).product(product=product, category=category, search=search, **kwargs)

    """
    Product show on enter to new slug URL
    """
    @http.route('/product/<path:path>', type='http', auth="public", website=True)
    def _product(self, path, product=None, category='', search='', **kwargs):

        products_list = http.request.env['product.template']
        product = products_list.sudo().search([('slug', '=', path)], limit=1)
        user = request.env.user

        if product:
            if not product.website_published and user.id != SUPERUSER_ID and \
                    not (user.has_group('website.group_website_designer')
                         or user.has_group('website.group_website_publisher')):
                return request.render("website.403")
            else:
                return super(WebsiteSale, self).product(product=product, category=category, search=search, **kwargs)
        else:
            return http.request.env['ir.http'].reroute('/404')
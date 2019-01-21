# -*- coding: utf-8 -*-
# © 2018 Comunitea - Pavel Smirnov <pavel@comunitea.com>
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from odoo import http
from odoo.http import request
from odoo.addons.website_sale.controllers.main import WebsiteSale


class CategoryRedirect(WebsiteSale):
    """
    ECommerce category redirecting from custom Odoo URL to new friendly URL en base of SLUG field.
    """
    @http.route([
        '/shop',
        '/shop/page/<int:page>',
        '/shop/category/<model("product.public.category"):category>',
        '/shop/category/<model("product.public.category"):category>/page/<int:page>'
    ], type='http', auth='public', website=True)
    def shop(self, page=0, category=None, search='', ppg=False, **post):
        if category and category.slug:
            return http.local_redirect(
                '/category/%s' % category.slug,
                dict(http.request.httprequest.args),
                True,
                code='301'
            )
        return super(CategoryRedirect, self).shop(page=page, category=category, search=search, ppg=ppg, **post)

    """
    Search the eCommerce category en base of new SLUG URL.
    """
    @http.route('/category/<path:path>', type='http', auth='public', website=True)
    def _shop(self, path, page=0, category=None, search='', ppg=False, **post):
        cat_list = request.env['product.public.category']
        category = cat_list.sudo().search([('slug', '=', path)], limit=1)
        if category:
            result = super(CategoryRedirect, self).shop(
                page=page, category=category, search=search, ppg=ppg, **post)
        else:
            result = request.env['ir.http'].reroute('/404')
        return result


class ProductRedirect(WebsiteSale):
    """
    Product redirecting from custom Odoo URL to new friendly URL en base of SLUG field.
    """
    @http.route(['/shop/product/<model("product.template"):product>'], type='http', auth="public", website=True)
    def product(self, product, category='', search='', **kwargs):
        if product.slug:
            return http.local_redirect(
                '/product/%s' % product.slug,
                dict(http.request.httprequest.args),
                True,
                code='301'
            )
        return super(ProductRedirect, self).product(product=product, category=category, search=search, **kwargs)

    """
    Search the product en base of new SLUG URL
    """
    @http.route('/product/<path:path>', type='http', auth="public", website=True)
    def _product(self, path, product=None, category='', search='', **kwargs):
        prod_list = request.env['product.template']
        product = prod_list.sudo().search([('slug', '=', path)], limit=1)
        if product:
            result = super(ProductRedirect, self).product(
                product=product, category=category, search=search, **kwargs)
        else:
            result = request.env['ir.http'].reroute('/404')
        return result

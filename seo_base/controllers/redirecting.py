# -*- coding: utf-8 -*-
# © 2018 Comunitea - Pavel Smirnov <pavel@comunitea.com>
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from odoo import http, SUPERUSER_ID
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
        '/shop/category/<model("product.public.category"):category>/page/<int:page>',
        '/shop/brands'
    ], type='http', auth='public', website=True)
    def shop(self, page=0, category=None, brand=None, search='', ppg=False, **post):

        # Prevent search box inside category
        if search and category:
            return request.redirect("/shop?search=%s" % search)

        # If category is digit (in order_by parameter)
        if category and category.isdigit():
            category = request.env['product.public.category'].sudo().search([('id', '=', category)])

        # If not search box
        if category and category.slug:
            route = '/category/%s/page/%d' % (category.slug, page) if page else '/category/%s' % category.slug
            return http.local_redirect(
                route,
                dict(http.request.httprequest.args),
                True,
                code='301'
            )
        if brand:
            context = dict(request.env.context)
            context.setdefault('brand_id', int(brand))
            request.env.context = context
        return super(CategoryRedirect, self).shop(page=page, category=category, brand=brand, search=search, ppg=ppg,
                                                  **post)

    """
    Search the eCommerce category en base of new SLUG URL.
    """
    @http.route([
        '/category/<path:path>',
        '/category/<path:path>/page/<int:page>'
    ], type='http', auth='public', website=True)
    def _shop(self, path, page=0, category=None, search='', ppg=False, **post):
        cat_list = request.env['product.public.category']
        category = cat_list.sudo().search([('slug', '=', path)], limit=1)
        if category:
            result = super(CategoryRedirect, self).shop(page=page, category=category, search=search, ppg=ppg, **post)
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
    def slug_product(self, path, category='', search='', **kwargs):
        prod_list = request.env['product.template']

        # Search with user permissions
        product = prod_list.search([('slug', '=', path)], limit=1)

        # Search without user permissions
        product_sudo = prod_list.sudo().search([('slug', '=', path)], limit=1)

        """
        If the product exists (it is not important if the user has access to this product) 
        return the standard template with normal user permissions.
        """
        if product_sudo:
            return super(ProductRedirect, self).product(product=product, category=category, search=search, **kwargs)
        else:
            return request.env['ir.http'].reroute('/404')

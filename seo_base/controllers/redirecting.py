# -*- coding: utf-8 -*-
# © 2018 Comunitea - Pavel Smirnov <pavel@comunitea.com>
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from odoo import http, SUPERUSER_ID
from odoo.http import request
from odoo.addons.website_sale.controllers.main import WebsiteSale


def shop_control_access(website):
    if not website.web_public_shop:
        user = request.env.user
        rules = website.shop_access_rules

        is_b2b = user.has_group('sale.group_show_price_subtotal')
        is_portal = user.has_group('base.group_portal')
        is_admin = user.has_group('website.group_website_publisher') \
                   or user.has_group('website.group_website_publisher') \
                   or user.id == SUPERUSER_ID

        if not is_admin:
            if (rules == 'b2b' and not is_b2b) or (rules == 'portal' and not is_portal):
                if is_portal:
                    return request.render("website.403")
                else:
                    return request.redirect('/web/login?redirect=%s' % request.httprequest.path)
    return False


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

        # Call to the user access control function
        if request.website:
            result = shop_control_access(request.website)
            if result:
                return result

        # Prevent search box inside category
        if search and category:
            return request.redirect("/shop?search=%s" % search)

        # If category is digit (in order_by parameter)
        order = post.get('order', False)
        if order and isinstance(category, str):
            category = request.env['product.public.category'].sudo().search([('id', '=', category)])

        # If not search box
        if category and category.slug:
            route = '/category/%s/page/%d' % (category.slug, page) if page else '/category/%s' % category.slug
            return http.local_redirect(
                route,
                http.request.httprequest.args,
                True,
                code='301'
            )
        return super(CategoryRedirect, self).shop(page=page, category=category, brand=brand, search=search, ppg=ppg,
                                                  **post)

    @http.route([
        '/category/<path:path>',
        '/category/<path:path>/page/<int:page>'
    ], type='http', auth='public', website=True)
    def _shop(self, path, page=0, category=None, search='', ppg=False, **post):
        """
        Search the eCommerce category en base of new SLUG URL.
        """

        # Call to the user access control function
        if request.website:
            result = shop_control_access(request.website)
            if result:
                return result

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

    def _update_context(self):
        """
        Update request.env.context to keep in redirections and super calls
        """
        context = dict(request.env.context)
        context.update({
            # You can inherit this controller and update the context
        })
        request.env.context = context
        return

    @http.route(['/shop/product/<model("product.template"):product>'], type='http', auth="public", website=True)
    def product(self, product, category='', search='', **kwargs):
        """
        Template render on whether or not there is slug url and context updated by website warehouse
        """

        # Call to the user access control function
        if request.website:
            result = shop_control_access(request.website)
            if result:
                return result

        if product.slug:
            return http.local_redirect(
                '/product/%s' % product.slug,
                dict(http.request.httprequest.args),
                True,
                code='301'
            )

        self._update_context()
        return super(ProductRedirect, self).product(product=product, category=category, search=search, **kwargs)

    @http.route('/product/<path:path>', type='http', auth="public", website=True)
    def slug_product(self, path, category='', search='', **kwargs):
        """
        Template render by SLUG URL and context updated by website warehouse

        :return: the standard template with normal user permissions if the product exists else 404
        """

        # Call to the user access control function
        if request.website:
            result = shop_control_access(request.website)
            if result:
                return result

        prod_list = request.env['product.template']

        # Search with user permissions
        product = prod_list.search([('slug', '=', path)], limit=1)

        # Search without user permissions
        product_sudo = prod_list.sudo().search([('slug', '=', path)], limit=1)

        if product_sudo:
            self._update_context()
            return super(ProductRedirect, self).product(product=product, category=category, search=search, **kwargs)
        else:
            return request.env['ir.http'].reroute('/404')

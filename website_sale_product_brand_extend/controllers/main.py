# © 2016 Serpent Consulting Services Pvt. Ltd. (http://www.serpentcs.com)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import http
from odoo.http import request
from odoo.addons.website_sale.controllers.main import QueryURL
from odoo.addons.website_sale.controllers.main import WebsiteSale


class WebsiteSale(WebsiteSale):

    # Method to get the brands.
    @http.route(
        ['/page/product_brands'], type='http', auth='public', website=True
    )
    def product_brands(self, **post):
        b_obj = request.env['product.brand']
        domain = [('website_published', '=', True)] + \
            request.website.website_domain()
        if post.get('search'):
            domain += [('name', 'ilike', post.get('search'))]
        brand_rec = b_obj.sudo().search(domain)
        keep = QueryURL('/page/product_brands', brand_id=[])
        values = {
            'brand_rec': brand_rec,
            'keep': keep
        }
        if post.get('search'):
            values.update({'search': post.get('search')})
        return request.render(
            'website_sale_product_brand.product_brands', values
        )

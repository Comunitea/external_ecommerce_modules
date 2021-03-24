# © 2019 Comunitea - Pavel Smirnov <pavel@comunitea.com> & Ruben Seijas <ruben@comunitea.com>
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from odoo import api, fields, models, _

PROD_DOMAIN = [('website_published', '=', True),
               ('list_price', '>', '0'),
               ('website_description_short', '!=', ''),
               ('sale_ok', '=', True),
               ('image', '!=', '')]


class FeedExport(models.Model):
    _name = 'google_merchant_export.feed'

    name = fields.Char(string=_("Name"), required=True)
    author = fields.Char(string=_("Feed author:"))
    note = fields.Html(string=_("Help description (only for admin-users)"))
    link = fields.Char(string=_("URL of XML file"), compute='_set_export_feed_url')
    link_down = fields.Char(string=_("Download URL"), compute='_set_export_feed_url')
    export_all = fields.Boolean(string=_("Export all products"))
    product_ids = fields.Many2many('product.template', string=_("Products to add"), domain=PROD_DOMAIN)
    category_ids = fields.Many2many('product.public.category', string=_("Product categories to add"))
    total = fields.Integer(string=_("Products total"), compute='_set_total')

    def _set_export_feed_url(self):
        base_url = self.env['ir.config_parameter'].sudo().get_param('web.base.url')
        for feed in self:
            feed.link = '%s/google-merchant/open/feed-%d.xml' % (base_url, feed.id)
            feed.link_down = '%s/google-merchant/download/feed-%d.xml' % (base_url, feed.id)

    @api.multi
    @api.constrains('category_ids')
    def _add_cat_products(self):
        for feed in self:
            prod_list = []

            # Add products to the list
            products = feed.product_ids
            if products:
                prod_list.extend(products.ids)

            # Add products of categories to the list
            categories = feed.category_ids
            if categories:
                domain = PROD_DOMAIN
                domain += ('public_categ_ids', 'in', categories.ids)
                products = self.env['product.template'].search(domain)
                prod_list.extend(products.ids)

            # Remove duplicate product ids and sort new list by id
            remove_duplicates = list(set(prod_list))
            remove_duplicates.sort()

            feed.product_ids = [(6, 0, remove_duplicates)]

    def _set_total(self):
        for feed in self:
            # Set total number of products
            if feed.export_all:
                feed.total = self.env['product.template'].search_count(PROD_DOMAIN)
            else:
                feed.total = len(feed.product_ids)

    def open_feed(self):
        return {
            'type': 'ir.actions.act_url',
            'url': self.link,
            'target': 'new'
        }

    def download_feed(self):
        return {
            'type': 'ir.actions.act_url',
            'url': self.link_down,
            'target': 'new'
        }

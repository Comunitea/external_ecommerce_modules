# -*- coding: utf-8 -*-
# © 2018 Comunitea - Pavel Smirnov <pavel@comunitea.com>
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

import unicodedata
import re
from odoo import http, api, models, fields, _
from odoo.http import request


class ProductMeta(models.Model):
    _inherit = 'product.template'

    product_meta_title = fields.Char("SEO Meta Title", translate=True)
    product_meta_description = fields.Text("SEO Meta Description", translate=True)
    product_meta_keywords = fields.Char("SEO Meta Keywords", translate=True)
    slug = fields.Char(_("Friendly URL"), help=_("Friendly URL for redirection"))
    description = fields.Html(_("Full product description"), strip_style=True, translate=True)
    description_short = fields.Text(_("Short product description"), help=_("Short description for product page"),
                                    strip_style=True, translate=True)

    def _slug_validation(self, value):
        # Set current website
        host = request.httprequest.host.split(':')[0]
        website = self.env['website'].search([('domain', '=ilike', host)])

        # Unicode validation
        uni = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore').decode('ascii')
        value = re.sub('[\W_]', ' ', uni).strip().lower()
        value = re.sub('[-\s]+', '-', value)

        # Return with max length
        max_length = website.slug_length if (19 < website.slug_length < 100) else 40
        return value[:max_length]

    @api.multi
    def write(self, values):
        has_slug = values.get('slug', False)
        if not has_slug or has_slug == '':
            # If slug not exists or is empty -> create from product name & id and validate
            new_slug = '%s-%s' % (self.name, self.id)
            values.update({
                'slug': self._slug_validation(new_slug)
            })
        else:
            # If slug exists -> validate
            values.update({
                'slug': self._slug_validation(has_slug)
            })
        return super(ProductMeta, self).write(values)

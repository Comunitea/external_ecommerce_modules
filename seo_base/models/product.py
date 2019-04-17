# -*- coding: utf-8 -*-
# © 2018 Comunitea - Pavel Smirnov <pavel@comunitea.com>
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

import unicodedata
import re
import random
from odoo import http, api, models, fields, _
from odoo.http import request


class ProductMeta(models.Model):
    _inherit = 'product.template'

    product_meta_title = fields.Char(_("SEO Meta Title"), translate=True)
    product_meta_description = fields.Text(_("SEO Meta Description"), translate=True)
    product_meta_keywords = fields.Char(_("SEO Meta Keywords"), translate=True)
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
        value = value[:max_length]

        # Check if this SLUG value already exists in any product or category
        it_exists = self.sudo().search([('slug', '=', value)], limit=1).id
        if it_exists and not it_exists == self.id:
            # Add random URL part
            value = '%s-%d' % (value, random.randint(0, 999))
        # Return
        return value

    @api.multi
    def write(self, values):
        for record in self:
            has_slug = values.get('slug', False)
            if not has_slug or has_slug == '':
                # If slug not exists or is empty -> create from product name & id and validate
                if not record.slug:
                    new_slug = '%s-%s' % (record.name, record.id)
                else:
                    new_slug = record.slug
                values.update({
                    'slug': record._slug_validation(new_slug)
                })
            else:
                # If slug exists -> validate
                values.update({
                    'slug': record._slug_validation(has_slug)
                })
            # Write
            return super(ProductMeta, record).write(values)

    @api.model
    def create(self, values):
        has_slug = values.get('slug', False)
        if not has_slug or has_slug == '':
            # If slug isn't established -> create from product name
            new_slug = values['name']
            values.update({
                'slug': self._slug_validation(new_slug)
            })
        else:
            # If slug is established -> validate
            values.update({
                'slug': self._slug_validation(has_slug)
            })
        # Create
        return super(ProductMeta, self).create(values)

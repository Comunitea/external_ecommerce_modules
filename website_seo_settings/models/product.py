# -*- coding: utf-8 -*-
import re
import unicodedata

from odoo import http, api, models, fields, _
from odoo.http import request
from odoo.tools.translate import html_translate


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    website_meta_title = fields.Char(
        string=_("Meta Title"),
        translate=True
    )
    website_meta_description = fields.Text(
        string=_("Meta Description"),
        translate=True
    )
    website_meta_keywords = fields.Char(
        string=_("Meta Keywords"),
        translate=True
    )
    slug = fields.Char(
        string=_("Friendly URL"),
        help=_("Friendly URL for SEO redirection"),
        copy=False
    )
    website_description_short = fields.Text(
        string=_("Short Description"),
        help=_("Short description in plain text"),
        strip_style=True, translate=True
    )
    product_redirect = fields.Many2one(
        'product.template',
        string="Redirect to another product"
    )
    website_specifications = fields.Html(
        string=_('Specifications'),
        strip_style=True,
        translate=html_translate
    )

    def _slug_validation(self, value, count=0):
        # Set current website
        domain = []
        host = request and request.httprequest.host.split(':')[0]
        if host:
            domain = [('domain', '=ilike', host)]
        website = self.env['website'].search(domain, limit=1)

        # Unicode validation
        uni = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore')\
            .decode('ascii')
        value = re.sub('[\W_]', ' ', uni).strip().lower()
        value = re.sub('[-\s]+', '-', value)

        # Return with max length
        max_length = website.slug_length if (
            19 < website.slug_length < 100) else 40
        value = value[:max_length]

        # Check if this SLUG value already exists in any product or category
        it_exists = self.sudo().search([('slug', '=', value)], limit=1)
        if it_exists and not it_exists.id == self.id:
            count = count + 1
            value = str(count) + "-" + value
            value = value[:max_length]
            self._slug_validation(value, count)
        # Return
        return value

    @api.multi
    def write(self, values):
        for record in self:
            has_slug = values.get('slug', False)
            if not has_slug or has_slug == '':
                # If slug not exists or is empty -> create from
                # product name & id and validate
                if not record.slug or values.get('name', False):
                    if values.get('name', False):
                        new_slug = '%s-%s' % ( values.get('name'), record.id)
                    else:
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
            super(ProductTemplate, record).write(values)
            values.pop('slug')
        return True

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
        return super(ProductTemplate, self).create(values)

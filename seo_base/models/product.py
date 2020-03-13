# -*- coding: utf-8 -*-

import random
import re
import unicodedata

from odoo import api, models, fields, _


class ProductCustom(models.Model):
    _inherit = 'product.template'

    description_short = fields.Text(_("Short Description"), help=_("Short description for product detail page"),
                                    strip_style=True)
    description = fields.Html(_("Full HTML Description"), help=_("Full HTML description for product detail page"),
                              strip_style=True)
    slug = fields.Char(_("Friendly URL"), help=_("Friendly URL for SEO"))
    hide_website_price = fields.Boolean(_("Hide Website Price"), default=False, help=_(
        "If selected, hide price and 'add to cart', 'add to wishlist' and 'add qty' buttons. 'N/D' is shown instead."))
    product_meta_title = fields.Char("Meta Title", translate=True)
    product_meta_description = fields.Text("Meta Description", translate=True)
    product_meta_keywords = fields.Char("Meta Keywords", translate=True)

    def slug_validation(self, value):
        # Unicode validation
        uni = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore').decode('ascii')
        value = re.sub('[\W_]', ' ', uni).strip().lower()
        value = re.sub('[-\s]+', '-', value)
        value = value[:60]

        # Check if this SLUG value already exists in any product or category
        it_exists = self.sudo().search([('slug', '=', value)], limit=1).id
        if it_exists and not it_exists == self.id:
            # Add random URL part
            value = '%s-%d' % (value, random.randint(0, 999))
        return value

    @api.multi
    def write(self, values):
        base_url = self.env['ir.config_parameter'].get_param('web.base.url')
        for product in self:
            has_slug = values.get('slug', False)
            if not has_slug or has_slug == '':
                # If slug not exists or is empty -> create from product name & id and validate
                if not product.slug:
                    new_slug = '%s-%s' % (product.name, product.id)
                    slug = product.slug_validation(new_slug)
                else:
                    slug = product.slug_validation(product.slug)
            else:
                # If slug exists -> validate
                slug = product.slug_validation(has_slug)
            # Write
            values.update({
                'slug': slug,
                'url_presupuesto': '%s/product/%s' % (base_url, slug)
            })
            super(ProductCustom, product).write(values)
            values.pop('slug')
            values.pop('url_presupuesto')
        return True

    @api.model
    def create(self, values):
        base_url = self.env['ir.config_parameter'].get_param('web.base.url')
        has_slug = values.get('slug', False)
        if not has_slug or has_slug == '':
            # If slug isn't established -> create from product name
            new_slug = values['name']
            slug = self.slug_validation(new_slug)
        else:
            # If slug is established -> validate
            slug = self.slug_validation(has_slug)
        # Create
        values.update({
            'slug': slug,
            'url_presupuesto': '%s/product/%s' % (base_url, slug)
        })
        return super(ProductCustom, self).create(values)


class ProductPublicCategory(models.Model):
    _inherit = "product.public.category"

    slug = fields.Char('Friendly URL', help="Friendly URL for SEO")

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
                    'slug': ProductCustom._slug_validation(self, new_slug)
                })
            else:
                # If slug exists -> validate
                values.update({
                    'slug': ProductCustom._slug_validation(self, has_slug)
                })
            # Write
            super(ProductPublicCategory, record).write(values)
            values.pop('slug')
        return True

    @api.model
    def create(self, values):
        has_slug = values.get('slug', False)
        if not has_slug or has_slug == '':
            # If slug isn't established -> create from category name
            new_slug = values['name']
            values.update({
                'slug': ProductCustom._slug_validation(self, new_slug)
            })
        else:
            # If slug is established -> validate
            values.update({
                'slug': ProductCustom._slug_validation(self, has_slug)
            })
        # Write
        return super(ProductPublicCategory, self).create(values)
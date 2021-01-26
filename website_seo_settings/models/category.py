# -*- coding: utf-8 -*-

from odoo import api, fields, http, models, _

from odoo.addons.website_seo_settings.models.product import ProductTemplate


class ProductPublicCategory(models.Model):
    _inherit = 'product.public.category'

    website_meta_title = fields.Char(string=_("Meta Title"), translate=True)
    website_meta_description = fields.Text(string=_("Meta Description"), translate=True)
    website_meta_keywords = fields.Char(string=_("Meta Keywords"), translate=True)
    slug = fields.Char(string=_("Friendly URL"), help=_("Friendly URL for SEO redirection"))
    website_published = fields.Boolean(string=_('Website Published'), default=True,
                                       help=_("Only published categories are visible on the website"))
    category_redirect = fields.Many2one('product.public.category', string="Redirect to another public category")
    color = fields.Integer(string="Color Index")

    @api.multi
    def write(self, values):
        for record in self:
            has_slug = values.get('slug', False)
            if not has_slug or has_slug == '':
                # If slug not exists or is empty -> create from category name & id and validate
                if not record.slug:
                    new_slug = '%s-%s' % (record.name, record.id)
                else:
                    new_slug = record.slug
                values.update({
                    'slug': ProductTemplate._slug_validation(self, new_slug)
                })
            else:
                # If slug exists -> validate
                values.update({
                    'slug': ProductTemplate._slug_validation(self, has_slug)
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
                'slug': ProductTemplate._slug_validation(self, new_slug)
            })
        else:
            # If slug is established -> validate
            values.update({
                'slug': ProductTemplate._slug_validation(self, has_slug)
            })
        # Write
        return super(ProductPublicCategory, self).create(values)

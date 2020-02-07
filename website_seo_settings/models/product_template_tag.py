# -*- coding: utf-8 -*-

from odoo import api, fields, http, models, _

from odoo.addons.website_seo_settings.models.product import ProductTemplate


class ProductTemplateTag(models.Model):

    _inherit = 'product.template.tag'

    slug = fields.Char(string="Friendly URL", help=_("Friendly URL for SEO redirection"))
    website_meta_title = fields.Char(string=_("Meta Title"), translate=True)
    website_meta_description = fields.Text(string=_("Meta Description"), translate=True)
    website_meta_keywords = fields.Char(string=_("Meta Keywords"), translate=True)
    website_id = fields.Many2one('website', string="Website", help=_("Empty it means is available for all websites, "
                                                                     "otherwise select desired websites"))
    website_published = fields.Boolean(string=_('Website Published'), default=True,
                                       help=_("Only published tags are visible on the website"))
    sequence = fields.Integer('Sequence', default=9999)
    tag_redirect = fields.Many2one('product.template.tag', string="Redirect to another Product Tag")

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
            super(ProductTemplateTag, record).write(values)
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
        return super(ProductTemplateTag, self).create(values)

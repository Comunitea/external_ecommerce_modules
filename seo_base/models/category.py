# -*- coding: utf-8 -*-
# © 2018 Comunitea - Pavel Smirnov <pavel@comunitea.com>
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from odoo import http, api, models, fields, _
from .product import ProductMeta


class ECommerceCategory(models.Model):
    _inherit = 'product.public.category'

    slug = fields.Char(_("Friendly URL"), help=_("Friendly URL for redirection"))

    @api.multi
    def write(self, values):
        for record in self:
            has_slug = values.get('slug', False)
            if not has_slug or has_slug == '':
                # If slug not exists or is empty -> create from category name & id and validate it
                new_slug = '%s-%s' % (record.name, record.id)
                values.update({
                    'slug': ProductMeta._slug_validation(record, new_slug)
                })
            else:
                # If slug exists -> validate
                values.update({
                    'slug': ProductMeta._slug_validation(record, has_slug)
                })
            # Write
            return super(ECommerceCategory, record).write(values)

    @api.model
    def create(self, values):
        has_slug = values.get('slug', False)
        if not has_slug or has_slug == '':
            # If slug isn't established -> create from category name
            new_slug = values['name']
            values.update({
                'slug': ProductMeta._slug_validation(self, new_slug)
            })
        else:
            # If slug is established -> validate
            values.update({
                'slug': ProductMeta._slug_validation(self, has_slug)
            })
        # Write
        return super(ECommerceCategory, self).create(values)

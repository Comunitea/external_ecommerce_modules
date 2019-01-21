# -*- coding: utf-8 -*-
# © 2018 Comunitea - Pavel Smirnov <pavel@comunitea.com>
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

# import unicodedata
# import re
from odoo import http, api, models, fields, _
# from odoo.http import request
from .product import ProductMeta


class ECommerceCategory(models.Model):
    _inherit = 'product.public.category'

    slug = fields.Char(_("Friendly URL"), help=_("Friendly URL for redirection"))

    @api.multi
    def write(self, values):
        has_slug = values.get('slug', False)
        if not has_slug or has_slug == '':
            # If slug not exists or is empty -> create from category name & id and validate it
            new_slug = '%s-%s' % (self.name, self.id)
            values.update({
                'slug': ProductMeta._slug_validation(self, new_slug)
            })
        else:
            # If slug exists -> validate
            values.update({
                'slug': ProductMeta._slug_validation(self, has_slug)
            })
        return super(ECommerceCategory, self).write(values)

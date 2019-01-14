# -*- coding: utf-8 -*-
# © 2018 Comunitea - Pavel Smirnov <pavel@comunitea.com>
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from odoo import models, fields, _


class ProductMeta(models.Model):
    _inherit = 'product.template'

    product_meta_title = fields.Char("SEO Meta Title", translate=True)
    product_meta_description = fields.Text("SEO Meta Description", translate=True)
    product_meta_keywords = fields.Char("SEO Meta Keywords", translate=True)
    slug = fields.Char(_("Friendly URL"), help=_("Friendly URL for redirection"))
    description = fields.Html(_("Full product description"), strip_style=True)
    description_short = fields.Text(_("Short product description"), help=_("Short description for product page"),
                                    strip_style=True)

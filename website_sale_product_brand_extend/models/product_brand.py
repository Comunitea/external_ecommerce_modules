from odoo import fields, models


class ProductBrand(models.Model):
    _name = "product.brand"
    _inherit = ["product.brand", "website.published.mixin",
                "website.multi.mixin"]

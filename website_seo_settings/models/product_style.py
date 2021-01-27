from odoo import fields, models


class ProductStyle(models.Model):
    _inherit = "product.style"

    color = fields.Integer(string="Color Index")

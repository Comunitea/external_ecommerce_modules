# -*- coding: utf-8 -*-
# © 2018 Comunitea - Pavel Smirnov <pavel@comunitea.com>
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from odoo import api, fields, models, _


class SaleOrder(models.Model):
    _inherit = "sale.order"

    applied_coupon = fields.Many2one("codecoupon_base.coupons", string=_("Applied coupon"), default=False)

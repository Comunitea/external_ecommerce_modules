# -*- coding: utf-8 -*-
# © 2018 Comunitea - Pavel Smirnov <pavel@comunitea.com>
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from odoo import api, fields, models, _


class SaleOrder(models.Model):
    _inherit = "sale.order"

    applied_coupon = fields.Many2one("codecoupon_base.coupons", string=_("Applied coupon"), default=False)
    ccb_discount = fields.Monetary(
        compute="_total_ccb_discount",
        digits=0,
        string=_("Total coupon discount")
    )

    @api.depends("order_line.product_uom_qty")
    def _total_ccb_discount(self):
        for order in self:
            if order.applied_coupon:
                order.ccb_discount = sum(order.order_line
                                         .filtered(lambda x: x.product_id.default_code == order.applied_coupon.code)
                                         .mapped("price_subtotal"))
            else:
                order.ccb_discount = 0

    @api.multi
    @api.depends("website_order_line.product_uom_qty", "website_order_line.product_id", "website_order_line")
    def _compute_cart_info(self):
        for order in self:
            if order.applied_coupon:
                order.cart_quantity = int(sum(order.website_order_line
                                              .filtered(lambda x: x.product_id.default_code != order.applied_coupon.code)
                                              .mapped("product_uom_qty")))
            else:
                order.cart_quantity = int(sum(order.website_order_line.mapped("product_uom_qty")))

    @api.one
    def _compute_website_order_line(self):
        for order in self:
            if order.applied_coupon:
                order.website_order_line = order.order_line.filtered(
                    lambda x: x.product_id.default_code != order.applied_coupon.code)
            else:
                order.website_order_line = order.order_line

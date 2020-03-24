# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class SaleOrder(models.Model):
    _inherit = "sale.order"

    applied_coupon = fields.Many2one("checkout_coupon.coupons", string="Applied coupon")
    total_coupon_discount = fields.Monetary(
        compute='_compute_total_coupon_discount',
        digits=0,
        string='Total coupon discount',
        store=True,
        track_visibility='always'
    )

    @api.depends('order_line.product_uom_qty')
    def _compute_total_coupon_discount(self):
        for order in self:
            order.total_coupon_discount = sum(
                order.order_line.filtered(
                    lambda x: x.product_id.default_code == order.applied_coupon.code).mapped('price_subtotal'))

    @api.multi
    @api.depends('website_order_line.product_uom_qty', 'website_order_line.product_id', 'website_order_line')
    def _compute_cart_info(self):
        """
        For not compute payment fee as quantity in header icon because is not a real product.
        For not compute products packs as quantity in header icon because only we want a pack quantity.
        :return:
        """
        for order in self:
            order.cart_quantity = int(sum(
                order.website_order_line.filtered(lambda x: x.product_id.sale_ok and not x.payment_fee_line and (
                        'pack_parent_line_id' not in dir(x) or (
                            'pack_parent_line_id' in dir(x) and not x.pack_parent_line_id)
                )).mapped('product_uom_qty')
            ))

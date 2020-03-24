# -*- coding: utf-8 -*-

from odoo import api, fields, models


class SaleOrder(models.Model):
    """
        Redefine model to show cash on delivery amount in cart total
    """
    _inherit = 'sale.order'

    amount_cash_on_delivery = fields.Monetary(
        compute='_compute_amount_cash_on_delivery', digits=0,
        string='Cash on Delivery Amount',
        help="The amount without tax.", store=True, track_visibility='always')
    has_cash_on_delivery = fields.Boolean(
        compute='_compute_has_cash_on_delivery', string='Has cash on delivery',
        help="Has an order line set for cash on delivery", store=True)
    total_weight = fields.Float('Peso', digits=0, compute='_compute_amount_cash_on_delivery',
                                store=True, track_visibility='always')

    @api.multi
    def write(self, vals):
        """
        Associate mode payment with payment method to link website orders if exist a relation ship
        """
        payment = vals.get('payment_acquirer_id', False)
        print('PAYMENT', payment)
        if payment:
            mode = self.env['payment.acquirer'].sudo().search(
                [('id', '=', vals['payment_acquirer_id'])])
            if mode:
                vals.update({
                    'payment_mode_id': mode.payment_mode.id
                })
        return super(SaleOrder, self).write(vals)

    @api.depends('order_line.price_unit', 'order_line.tax_id', 'order_line.discount', 'order_line.product_uom_qty')
    def _compute_amount_cash_on_delivery(self):
        for order in self:
            if self.env.user.has_group('sale.group_show_price_subtotal'):
                order.amount_cash_on_delivery = sum(order.order_line.filtered('payment_fee_line')
                                                    .mapped('price_subtotal'))
            else:
                order.amount_cash_on_delivery = sum(order.order_line.filtered('payment_fee_line')
                                                    .mapped('price_total'))
            # Add Weight to order
            total_weight = 0
            for r in order.order_line.filtered(lambda x: x.product_id.type not in ('service', 'digital')):
                total_weight += r.product_id.weight * r.product_uom_qty
            order.total_weight = total_weight

    @api.depends('order_line.payment_fee_line')
    def _compute_has_cash_on_delivery(self):
        for order in self:
            order.has_cash_on_delivery = any(order.order_line.filtered('payment_fee_line'))

    def update_fee_line(self, acquirer):
        """
        Update fee line depending on the context for do not delete fee lines for default payment method.
        :param acquirer:
        :return:
        """
        if self._context.get('no_update_fee_line', False):
            return
        return super(SaleOrder, self).update_fee_line(acquirer)

    @api.multi
    @api.depends('website_order_line.product_uom_qty', 'website_order_line.product_id', 'website_order_line')
    def _compute_cart_info(self):
        """
        For not compute payment fee as quantity in header icon because is not a real product.
        For not compute products packs as quantity in header icon because only we want a pack quantity.
        When there are only products as service it means there is not a physical delivery.
        :return: default values less payment fee as quantity.
        """
        for order in self:
            order.cart_quantity = int(sum(
                order.website_order_line.filtered(
                    lambda x: not x.payment_fee_line and ('pack_parent_line_id' not in dir(x) or (
                            'pack_parent_line_id' in dir(x) and not x.pack_parent_line_id))
                ).mapped('product_uom_qty')
            ))
            order.only_services = all(line.product_id.type in ('service', 'digital')
                                      for line in order.website_order_line.filtered(lambda x: not x.payment_fee_line))

    @api.depends('order_line.price_unit', 'order_line.tax_id', 'order_line.discount', 'order_line.product_uom_qty')
    def _compute_amount_delivery(self):
        """
        For not compute payment fee as amount delivery for to sum into delivery.
        :return: default values less payment fee as amount delivery.
        """
        for order in self:
                
            if self.env.user.has_group('sale.group_show_price_subtotal'):
                order.amount_delivery = sum(order.order_line.filtered('is_delivery')
                                            .filtered(lambda x: not x.payment_fee_line).mapped('price_subtotal'))
            else:
                order.amount_delivery = sum(order.order_line.filtered('is_delivery')
                                            .filtered(lambda x: not x.payment_fee_line).mapped('price_total'))
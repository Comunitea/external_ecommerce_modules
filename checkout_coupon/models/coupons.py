# -*- coding: utf-8 -*-

import string
import random

from odoo import api, fields, models, _

from odoo.addons import decimal_precision as dp
from odoo.exceptions import ValidationError
from odoo.tools import float_compare, float_round


class Coupons(models.Model):
    _name = "checkout_coupon.coupons"
    _description = 'Website Coupon Discount'

    def code_generate(self):
        characters = string.ascii_uppercase + string.digits
        return ''.join(random.choice(characters) for _ in range(10))

    def _default_tax_id(self):
        user = self.env.user
        return self.env['account.tax'].search(
            [('company_id', '=', user.company_id.id), ('type_tax_use', '=', 'sale'),
             ('amount_type', '=', 'percent'), ('account_id', '!=', False)], limit=1, order='amount desc')

    def _get_default_currency_id(self):
        return self.env.user.company_id.currency_id.id

    _sql_constraints = [
        ("name_uniq", "unique (code)", "The coupon code must be unique!"),
    ]

    name = fields.Char(string="Name", required=True)
    description = fields.Text("Description")
    is_active = fields.Boolean(string="Is active?", default=True)
    start_date = fields.Date(string="Start Date")
    end_date = fields.Date(string="End Date")
    partner_ids = fields.Many2many("res.partner", domain=[("active", "=", True)],
                                   string="List of Partners who can use this coupon")
    code = fields.Char(string="Coupon code", default=code_generate, required=True)
    is_counted = fields.Boolean(string="Is counted?", default=False)
    total = fields.Integer(string="Balance of coupons")
    coupon_type = fields.Selection(
        selection=[
            ("sale_order", "For Sale Order"),
            ("all", "All Products"),
            ("product", "For a single product"),
            ("category", "For a single category"),
        ], string="Is applicable: ", default="sale_order"
    )
    discount_product_id = fields.Many2one("product.product", string="Applicable product",
                                          domain=[("active", "=", True)], oldname='product_id')
    discount_category_id = fields.Many2one("product.public.category", string="Applicable category",
                                           oldname='category_id')
    min_cart_value = fields.Integer(string="Minimum cart total")
    max_cart_value = fields.Integer(string="Maximum cart total")
    discount_type = fields.Selection([
        ('amount_tax_included', 'Fixed Amount (VAT included)'),
        ('amount_tax_excluded', 'Fixed Amount (VAT excluded)'),
        ('percentage', 'Percentage discount')
    ], string="Discount type", default='amount_tax_included', required=True)
    value = fields.Float(string="Discount value", default=1, required=True,
                         digits=dp.get_precision('Product Price'))
    tax_id = fields.Many2one('account.tax', string='Coupon VAT', required=True, default=_default_tax_id)
    discount_amount_currency_id = fields.Many2one(
        "res.currency",
        string="Discount Amount Currency",
        default=lambda a: a._get_default_currency_id())

    @api.constrains('coupon_type')
    def _check_coupon_type(self):
        for r in self:
            if r.coupon_type == 'all':
                self.discount_product_id = None
                self.discount_category_id = None
            elif r.coupon_type == 'product':
                self.discount_category_id = None
            elif r.coupon_type == 'category':
                self.discount_product_id = None

    @api.constrains('value')
    def _check_coupons_value(self):
        for r in self:
            if r.value < 0 or r.value == 0:
                raise ValidationError(_('Coupon value must be positive'))

    @api.constrains('total')
    def _check_coupons_total(self):
        for r in self:
            if r.total < 0:
                raise ValidationError(_('Number of coupons must be positive'))

    @api.constrains('start_date', 'end_date')
    def _check_dates(self):
        for r in self:
            if r.start_date > r.end_date:
                raise ValidationError(_('"End date" must be later then "Start date"'))

    @api.constrains('min_cart_value', 'max_cart_value')
    def _check_cart(self):
        for r in self:
            if r.min_cart_value < 0:
                raise ValidationError(_('"Minimum cart total" must be positive'))
            if r.max_cart_value < 0:
                raise ValidationError(_('"Maximum cart total" must be positive'))
            if r.min_cart_value > r.max_cart_value:
                raise ValidationError(_('"Minimum cart total" must be later then "Maximum cart total"'))

    @api.constrains('code')
    def _check_coupone_code_length(self):
        for r in self:
            if len(r.code) < 4:
                raise ValidationError(_('Coupon code must have at least four characters'))

    @api.multi
    def _prepare_order_line_discount(self, order):
        self.ensure_one()
        # take coupon tax
        taxes = self.tax_id
        # takes all applied taxes.
        # if not taxes:
        #     taxes = self.discount_product_id.taxes_id
        #     if not taxes:
        #         for tax in order.order_line.mapped('tax_id'):
        #             taxes += tax
        if order.fiscal_position_id:
            taxes = order.fiscal_position_id.map_tax(taxes)
        price = self.discount_amount_currency_id.compute(
            from_amount=self.value,
            to_currency=order.currency_id)
        if taxes:
            price_precision_digits = self.env[
                'decimal.precision'].precision_get('Product Price')
            amounts = taxes.compute_all(price, order.currency_id, 1, product=self.discount_product_id,
                                        partner=order.partner_shipping_id)
            result_discount = amounts['total_included']
            if self.discount_type == "amount_tax_excluded":
                result_discount = amounts['total_excluded']
            if float_compare(result_discount, price, precision_digits=price_precision_digits):
                average_tax = 100.0 - (price / result_discount) * 100
                price += (price * -average_tax) / 100
            price = float_round(price, price_precision_digits)
            price = self._fix_discount_amount_rounding(price, taxes, price_precision_digits, order)
        return {
            'product_id': self.discount_product_id.id,
            'list_price': -price,
            'product_uom_qty': 1,
            'is_promotion_line': True,
            'name': self.discount_product_id.name,
            'product_uom': self.discount_product_id.uom_id.id,
            'tax_id': [(4, tax.id, False) for tax in taxes]
        }

    def _fix_discount_amount_rounding(self, price, taxes, precision_digits, order):
        """
        In this method we recompute the taxes for the given price to be sure
        that we don't have rounding issue.
        If the computed price to not match the expected discount amount, we try
        to fix the rounding issue by adding/removing the most significative
        amount according to the price decision while the computed price doesn't
        match the expected amount or the sign of the difference changes
        """
        expected_discount = self.discount_amount_currency_id.compute(
            from_amount=self.value,
            to_currency=order.currency_id)
        amount_type = 'total_included'
        if self.discount_type == "amount_tax_excluded":
            amount_type = 'total_excluded'
        price_amounts = taxes.compute_all(
            price,
            order.currency_id,
            1,
            product=self.discount_product_id,
            partner=order.partner_shipping_id)
        diff = float_compare(price_amounts[amount_type], expected_discount, precision_digits=precision_digits)
        if not diff:
            return price
        while diff:
            step = 1.0 / 10 ** precision_digits
            price += step * -diff
            price_amounts = taxes.compute_all(
                price,
                order.currency_id,
                1,
                product=self.discount_product_id,
                partner=order.partner_shipping_id)
            new_diff = float_compare(price_amounts[amount_type], expected_discount, precision_digits=precision_digits)
            if not new_diff:
                return price
            if new_diff != diff:
                # not able to fix the rounding issue due to current precision
                return price

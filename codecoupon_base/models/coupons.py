# -*- coding: utf-8 -*-
# © 2018 Comunitea - Pavel Smirnov <pavel@comunitea.com>
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

import string
import random
from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


def _default_website(self):
    return self.env['website'].search([], limit=1)


class Coupons(models.Model):
    _name = "codecoupon_base.coupons"

    # Set default code length
    website_id = fields.Many2one('website', string="Website to apply", default=_default_website, required=True)
    code_def_length = fields.Integer(related='website_id.codecoupon_length')

    # Generate random coupon code
    def code_generate(self):
        # Set minimum code length
        length = self.code_def_length
        characters = string.ascii_uppercase + string.digits
        return ''.join(random.choice(characters) for _ in range(length))

    _sql_constraints = [
        ("code_uniq", "unique (code)", "The coupon code must be unique!"),
    ]

    # General part
    code = fields.Char(string=_("Coupon code"), default=code_generate, required=True)
    name = fields.Char(string=_("Coupon name"), required=True)
    is_active = fields.Boolean(string=_("Is active?"), default=True)
    # Quantity
    is_counted = fields.Boolean(string=_("Is counted?"), default=False)
    total = fields.Integer(string=_("Balance of coupons"))
    # Type of application (weigh and objective)
    coupon_type = fields.Selection(
        selection=[
            ("all", _("All Products")),
            ("product", _("For any products")),
            ("category", _("For any categories")),
        ], string=_("Is applicable: "), default="all"
    )
    product_ids = fields.Many2many("product.product", string=_("Applicable products"),
                                   domain=[("active", "=", True), ("product_tmpl_id.website_published", "=", True)])
    category_ids = fields.Many2many("product.public.category", string=_("Applicable categories"))
    discount_type = fields.Selection([
        ("fixed", _("Fixed discount")),
        ("percentage", _("Percentage discount"))
    ], string=_("Discount type"), default="fixed", required=True)
    value = fields.Float(string=_("Discount value"), default=1, required=True)
    # Users/partners to apply
    partner_ids = fields.Many2many("res.partner", domain=[("active", "=", True)],
                                   string=_("List of Partners who can use this coupon"))
    # Date and cart weight settings
    start_date = fields.Date(string=_("Start Date"))
    end_date = fields.Date(string=_("End Date"))
    min_cart = fields.Integer(string=_("Minimum cart total"))
    max_cart = fields.Integer(string=_("Maximum cart total"))
    # Other
    note = fields.Html(string=_("Description note"))

    # Buttons action
    def activate_coupon(self):
        for r in self:
            r.write({'is_active': True})

    def deactivate_coupon(self):
        for r in self:
            r.write({'is_active': False})

    # Constraints and depends
    @api.constrains("value")
    def _check_coupon_value(self):
        for r in self:
            if r.value < 0 or r.value == 0:
                raise ValidationError(_("Coupon value must be positive"))

    @api.constrains("total")
    def _check_coupon_total(self):
        for r in self:
            if r.total < 0:
                raise ValidationError(_("Number of coupons must be positive"))

    @api.constrains("start_date", "end_date")
    def _check_coupon_dates(self):
        for r in self:
            if r.start_date > r.end_date:
                raise ValidationError(_("\"End date\" must be later then \"Start date\""))

    @api.constrains("min_cart", "max_cart")
    def _check_coupon_cart_total(self):
        for r in self:
            if r.min_cart < 0:
                raise ValidationError(_("\"Minimum cart total\" must be positive"))
            if r.max_cart < 0:
                raise ValidationError(_("\"Maximum cart total\" must be positive"))
            if r.min_cart > r.max_cart:
                raise ValidationError(_("\"Minimum cart total\" must be later then \"Maximum cart total\""))

    @api.constrains("code")
    def _check_coupon_code_length(self):
        for r in self:
            # Validation of code length
            if r.code:
                if len(r.code) < self.code_def_length:
                    raise ValidationError(_("Coupon code must have at least %d characters" % self.code_def_length))

    @api.multi
    def write(self, values):
        coupon_type = values.get('coupon_type', False)
        # If coupon type is "All" -> delete the values of associated products and categories
        if coupon_type == 'all':
            values.update({
                'product_ids': [[6, False, []]],
                'category_ids': [[6, False, []]]
            })
        if coupon_type == 'product':
            values.update({
                'category_ids': [[6, False, []]]
            })
        if coupon_type == 'category':
            values.update({
                'product_ids': [[6, False, []]]
            })
        # Write
        return super(Coupons, self).write(values)

# -*- coding: utf-8 -*-

from odoo import fields, models


class PaymentMode(models.Model):
    _inherit = 'payment.acquirer'

    payment_mode = fields.Many2one('account.payment.mode', string='Payment Mode',
                                   domain=[('payment_type', '=', 'inbound')])

# -*- coding: utf-8 -*-
#
# © 2018 Comunitea - Ruben Seijas <ruben@comunitea.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import _, api, fields, models
from odoo.addons.payment.models.payment_acquirer import ValidationError
from odoo.tools.float_utils import float_compare

import logging
import pprint

_logger = logging.getLogger(__name__)


class CashOnDeliveryPaymentAcquirer(models.Model):
    _inherit = 'payment.acquirer'

    provider = fields.Selection(selection_add=[('cash', 'Cash On Delivery')], default='cash')

    def cash_get_form_action_url(self):
        return '/payment/cash/feedback'

    def _format_cash_data(self):
        post_msg = _('''<div>
            <h3>Please use the following Cash On Delivery details:</h3>
            <h4><strong>Payment</strong></h4>
            <p>Payment will be made upon delivery of the order.</p>
            <h4><strong>Delivery</strong></h4>
            <p>Delivery will be made to the address of the delivery that has been designated in your order.</p>
            <h4><strong>Doubts</strong></h4>
            <p>You can contact us by email: <a href="mailto:info@nostrumsport.com" target="_blank">info@nostrumsport.com</a></p>
            <h4><strong>Gratitude</strong></h4>
            <p>Thanks for trusting us. Enjoy your purchase.</p>
            </div>''')
        return post_msg

    @api.model
    def create(self, values):
        """ Hook in create to create a default post_msg. This is done in create
        to have access to the name and other creation values. If no post_msg
        or a void post_msg is given at creation, generate a default one. """
        if values.get('provider') == 'cash' and not values.get('post_msg'):
            values['post_msg'] = self._format_cash_data()
        return super(CashOnDeliveryPaymentAcquirer, self).create(values)


class CashOnDeliveryPaymentTransaction(models.Model):
    _inherit = 'payment.transaction'

    @api.model
    def _cash_form_get_tx_from_data(self, data):
        reference, amount, currency_name = data.get('reference'), data.get('amount'), data.get('currency_name')
        tx = self.search([('reference', '=', reference)])

        if not tx or len(tx) > 1:
            error_msg = _('received data for reference %s') % (pprint.pformat(reference))
            if not tx:
                error_msg += _('; no order found')
            else:
                error_msg += _('; multiple order found')
            _logger.info(error_msg)
            raise ValidationError(error_msg)

        return tx

    def _cash_form_get_invalid_parameters(self, data):
        invalid_parameters = []

        if float_compare(float(data.get('amount', '0.0')), self.amount, 2) != 0:
            invalid_parameters.append(('amount', data.get('amount'), '%.2f' % self.amount))
        if data.get('currency') != self.currency_id.name:
            invalid_parameters.append(('currency', data.get('currency'), self.currency_id.name))

        return invalid_parameters

    def _cash_form_validate(self, data):
        _logger.info('Validated Cash On Delivery payment for tx %s: set as pending' % self.reference)
        return self.write({'state': 'done'})

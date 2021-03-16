# © 2018 Comunitea - Ruben Seijas <ruben@comunitea.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging
import pprint
import werkzeug

from odoo import http
from odoo.http import request
from odoo.addons.website_sale.controllers.main import WebsiteSale

_logger = logging.getLogger(__name__)


class Controller(http.Controller):
    _accept_url = '/payment/cash/feedback'

    @http.route(['/payment/cash/feedback'], type='http', auth='none', csrf=False)
    def cash_form_feedback(self, **post):
        _logger.info('Beginning form_feedback with post data %s', pprint.pformat(post))  # debug
        request.env['payment.transaction'].sudo().form_feedback(post, 'cash')
        return werkzeug.utils.redirect(post.pop('return_url', '/'))


class CashOnDeliveryController(WebsiteSale):
    """
    Controller del metodo de pago: Cash On Delivery.
    """

    @http.route('/shop/payment/validate', type='http', auth="public", website=True)
    def payment_validate(self, transaction_id=None, sale_order_id=None, **post):
        """
        Cash on Delivery order need to be confirmed and send mail.
        """

        if sale_order_id is None:
            order = request.website.sale_get_order()
        else:
            order = request.env['sale.order'].sudo().browse(sale_order_id)
            assert order.id == request.session.get('sale_last_order_id')

        super(CashOnDeliveryController, self).payment_validate(transaction_id=None, sale_order_id=None, **post)

        # Attention: Be carefully to create others payment methods
        if order.payment_acquirer_id.provider != 'transfer':
            order.with_context(send_email=True).action_confirm()

        return request.redirect('/shop/confirmation')

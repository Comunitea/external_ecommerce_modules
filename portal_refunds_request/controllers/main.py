# -*- coding: utf-8 -*-
# © 2019 Comunitea
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from odoo import http
from odoo.http import request

from odoo.addons.sale.controllers.portal import CustomerPortal


class CustomerPortalRefunds(CustomerPortal):

    @http.route(['/my/orders/refunds_form/order/<string:order>', ], type='http', auth='user', website=True)
    def refunds_contact_form(self, order=None, **post):

        # Check if website.refunds_contact is active
        website = request.website
        values = {
            'order': order,
        }
        if website.refunds_contact and order:
            return request.render("portal_refunds_request.multi_base_contact_us_content_template", values)
        else:
            return request.redirect("/my/orders")

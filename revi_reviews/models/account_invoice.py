# -*- coding: utf-8 -*-
# © 2019 Comunitea - Pavel Smirnov <pavel@comunitea.com> & Ruben Seijas <ruben@comunitea.com>
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

import json
import requests
import unicodedata
from odoo import api, fields, models, _
from odoo.http import request


class AccountInvoice(models.Model):
    _inherit = "account.invoice"

    revi_use = fields.Boolean(string=_("Use Revi service"), default=False)
    revi_state = fields.Selection([
        ('skip', _("Don't send")),
        ('waiting', _("Waiting for send")),
        ('error', _("Error of send")),
        ('sent', _("Already sent"))
    ], string=_("Opinion state"), default='waiting', help=_("Revi data state for this order"))

    @api.model
    def create(self, vals):
        website = request.env['website'].get_current_website()
        partner_id = vals.get('partner_id', False)
        partner = request.env['res.partner'].sudo().search([('id', '=', partner_id)], limit=1)

        def set_revi_state(use, state):
            return vals.update({
                'revi_use': use,
                'revi_state': state
            })

        # Check order type
        if website.revi_def_state != 'skip' and partner.revi_use and (
                vals.get('type', False) and vals['type'] == 'out_invoice'):
            set_revi_state(True, 'waiting')
        else:
            set_revi_state(False, 'skip')

        return super(AccountInvoice, self).create(vals)

    @api.multi
    def write(self, values):
        """
        We need to send invoice data to Revi only if state of invoice was changed and is OPEN.
        OR
        We need to send data if last attempt to send the data has FAILED (has state ERROR).
        """
        resp = super(AccountInvoice, self).write(values)
        website = request.env['website'].get_current_website()
        language = website.default_lang_id.iso_code
        root = request.httprequest.url_root

        if values.get('state', False) and values['state'] == 'open':
            for res in self:
                partner = res.partner_id
                # Generate order & order_line data to send
                if res.revi_use and ('waiting' in res.revi_state or 'error' in res.revi_state) \
                        and partner.revi_use and partner.email and website.revi_api_key:
                    # Set order data
                    order_data = {
                        'orders': [{
                            'id_order': '%s' % res.id,
                            'lang': language,
                            'customer_name': partner.name,
                            'email': partner.email,
                            'currency': res.currency_id.name,
                            'taxes': '%s' % res.amount_tax,
                            'total_products': '%s' % len(res.invoice_line_ids.filtered(
                                lambda x: x.product_id.type == 'product' or x.product_id.type == 'service')),
                            'total_paid': '%s' % res.amount_total,
                            'status': 'ready' if website.revi_auto_send else 'pending',
                            'order_date': res.create_date,
                            'date_status_upd': res.write_date
                        }]
                    }

                    def _gen_product_data(product):
                        return {
                            'id_product': product.id,
                            'price': product.lst_price,
                            'sku': product.default_code or '',
                            'locale': [{
                                'lang': language,
                                'name': unicodedata.normalize('NFKD', product.name).encode('ascii', 'ignore').decode(
                                    'ascii'),
                                'url': '%sshop/product/%d' % (root, product.id),
                                'photo_url': '%swebsite/image/product.template/%d/image/' % (root, product.id),
                                'description': ''
                            }]
                        }

                    # Set products data
                    product_data = {
                        'products': []
                    }
                    products_to_link = []

                    invoice_lines = res.invoice_line_ids.filtered(
                        lambda x: x.product_id.type == 'product' or x.product_id.type == 'service')
                    for line in invoice_lines:
                        product = line.product_id.product_tmpl_id
                        product_data['products'].append(_gen_product_data(product))
                        products_to_link.append({'id_product': '%d' % product.id})

                    # Set data for link products with order
                    link_data = {
                        'orders_products': [{
                            'id_order': '%s' % res.id,
                            'products': products_to_link
                        }]
                    }

                    headers = {
                        'Content-Type': 'application/json',
                        'Accept': 'application/json',
                        'X-API-KEY': website.revi_api_key
                    }

                    # Set API URL's
                    revi_hello_url = 'https://revi.io/api/v1/hello_world'
                    revi_order_url = 'https://revi.io/api/v1/orders'
                    revi_product_url = 'https://revi.io/api/v1/products'
                    revi_link_url = 'https://revi.io/api/v1/orders_products'

                    hello_data = {
                        'test': 'Hello Revi!'
                    }

                    def post_send(url, data, headers):
                        return requests.post(url, data=json.dumps(data), headers=headers)

                    def post_success(request):
                        code = request.status_code
                        if code in [200, 201]:
                            return True
                        else:
                            return False

                    # Test post call
                    hello_call = post_send(revi_hello_url, hello_data, headers)

                    # Send data
                    success = False
                    if post_success(hello_call):
                        # Send order
                        create_order = post_send(revi_order_url, order_data, headers)
                        if post_success(create_order):
                            # Send products (order_line)
                            create_products = post_send(revi_product_url, product_data, headers)
                            if post_success(create_products):
                                # Link products to orders
                                link_products = post_send(revi_link_url, link_data, headers)
                                if post_success(link_products):
                                    success = True

                    # Set new Revi state for changed account invoice
                    if success:
                        res.sudo().write({'revi_state': 'sent'})
                    else:
                        res.sudo().write({'revi_state': 'error'})

        return resp
